import os, platform
import zipfile, shutil
import contextlib

import urllib, ssl
import json

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

### To-Do
# Make Installer General Purpose with optional application plugin installs
###
### Info ###
# Installer switches between install/unistall based on existance of "LYNX" env variable

# Temporary Code
import hou

# Execute Directly
# import urllib,ssl; exec (urllib.urlopen('https://raw.githubusercontent.com/LucaScheller/VFX-LYNX/master/lib/LYNX_update.py',context=ssl._create_unverified_context()).read(), globals(), locals()); LYNX_update_manager_object = LYNX_update_manager();LYNX_update_manager_object.ui_LYNX_update_manager();

LYNX_repo_url = 'https://api.github.com/repos/lucascheller/VFX-LYNX'


class QT_LYNX_update_manager(QWidget):
    def __init__(self, parent, LYNX_update_manager):
        super(QT_LYNX_update_manager, self).__init__(parent)

        # Window Settings
        self.setWindowTitle("LYNX Update Manager")
        self.setFixedWidth(300)
        self.setWindowFlags(Qt.Window)
        self.setStyleSheet("QWidget {background-color:hsl(0,0,60);} QGroupBox {border: 2px solid rgb(0,208,255);}")

        self.LYNX_update_manager = LYNX_update_manager
        self.lineEdit_directory = None
        self.comboBox_releases = None

        self.ui_main()

    def ui_main(self):

        ### Preferences
        groupBox_preferences = QGroupBox("Installation Preferences")

        # Directory
        layout_directory = QHBoxLayout()
        label_directory = QLabel("Directory:")
        self.lineEdit_directory = QLineEdit()
        self.lineEdit_directory.setPlaceholderText("Installation Directory")
        self.lineEdit_directory.editingFinished.connect(self.lineEdit_directory_editingFinished)
        button_directory_select = QPushButton("Browse")
        button_directory_select.clicked.connect(self.button_directory_select_clicked)

        layout_directory.addWidget(label_directory)
        layout_directory.addWidget(self.lineEdit_directory)
        layout_directory.addWidget(button_directory_select)

        # Release
        layout_releases = QHBoxLayout()
        label_releases = QLabel("Release:")
        self.comboBox_releases = QComboBox(self)
        self.comboBox_releases.currentTextChanged.connect(self.comboBox_releases_currentTextChanged)
        for release in sorted(list(self.LYNX_update_manager.release_data["release_production"].keys()), reverse=True)[:5]:
            self.comboBox_releases.addItem(release + " | Production Build")
        if (len(list(self.LYNX_update_manager.release_data["release_prerelease"].keys())) > 0):
            self.comboBox_releases.insertSeparator(5)
            for release in sorted(list(self.LYNX_update_manager.release_data["release_prerelease"].keys()),
                                  reverse=True)[:5]:
                self.comboBox_releases.addItem(release + " | Prerelease Build")

        layout_releases.addWidget(label_releases)
        layout_releases.addWidget(self.comboBox_releases)

        layout_preferences = QVBoxLayout()
        layout_preferences.addLayout(layout_directory)
        layout_preferences.addLayout(layout_releases)

        groupBox_preferences.setLayout(layout_preferences)

        # Install / Uninstall
        spacer = QLabel("")
        button_install = QPushButton("Install")
        button_install.clicked.connect(self.button_install_clicked)
        button_uninstall = QPushButton("Uninstall / Change Release")
        button_uninstall.clicked.connect(self.button_uninstall_clicked)
        button_uninstall.setVisible(False)

        # Main Layout
        layout = QVBoxLayout()
        layout.addWidget(groupBox_preferences)
        layout.addWidget(spacer)
        layout.addWidget(button_install)
        layout.addWidget(button_uninstall)
        self.setLayout(layout)

        # Switch functionality based on existance of "LYNX" env variable
        if os.getenv("LYNX", None) == None:
            self.lineEdit_directory.setText(os.path.expanduser("~/Documents") + "/" + "LYNX" + "/" + "LYNX_" + self.LYNX_update_manager.release_version)
        else:
            groupBox_preferences.setEnabled(False)
            self.lineEdit_directory.setText(os.environ["LYNX"])
            label_releases.setVisible(False)
            self.comboBox_releases.setVisible(False)
            button_install.setVisible(False)
            button_uninstall.setVisible(True)

    def lineEdit_directory_editingFinished(self):
        directory_path = self.lineEdit_directory.text()
        self.lineEdit_directory.setText(directory_path if directory_path[-1] != "/" else directory_path[:-1])

    def button_directory_select_clicked(self):
        directory_path = str(QFileDialog.getExistingDirectory(self, "Select Directory", self.lineEdit_directory.text()))
        if ("lynx_v" not in os.path.basename(directory_path).lower()):
            directory_path = directory_path + "/" + "LYNX_" + self.comboBox_releases.currentText()[:self.comboBox_releases.currentText().rfind(" | ")]
        self.lineEdit_directory.setText(directory_path)

    def comboBox_releases_currentTextChanged(self):
        directory_path = self.lineEdit_directory.text()
        if ("lynx_v" in os.path.basename(directory_path).lower()):
            self.lineEdit_directory.setText(
                os.path.dirname(directory_path) + "/" + "LYNX_" + self.comboBox_releases.currentText()[:self.comboBox_releases.currentText().rfind(" | ")])

    def button_install_clicked(self):
        os.environ["LYNX"] = self.lineEdit_directory.text()
        self.LYNX_update_manager.release_type = "production" if "production" in self.comboBox_releases.currentText().lower() else "prerelease"
        self.LYNX_update_manager.release_version = self.comboBox_releases.currentText()[
                                                   :self.comboBox_releases.currentText().rfind(" | ")]
        self.LYNX_update_manager.release_install()
        self.close()
        QMessageBox.information(self, "LYNX Update Manager | Install",
                                "Installation successfull. Please restart the application.")

    def button_uninstall_clicked(self):
        answer = QMessageBox.warning(self, "LYNX Update Manager | Uninstall",
                                     "The following folder will be removed: " + os.environ["LYNX"],
                                     QMessageBox.Ok | QMessageBox.Cancel)
        if answer == QMessageBox.Ok:
            self.LYNX_update_manager.release_uninstall()
            self.close()

            answer = QMessageBox.information(self, "LYNX Update Manager | Uninstall",
                                             "Uninstall successfull. Please restart the application.\nDo you want to alternatively reinstall a different release? ",
                                             QMessageBox.Yes | QMessageBox.Cancel)
            if answer == QMessageBox.Yes:
                self.LYNX_update_manager.ui_LYNX_update_manager()


class LYNX_update_manager(object):

    def __init__(self):
        self.env = []
        if (os.getenv("HOUDINI_VERSION", None) != None):
            self.env.append("HOUDINI")

        # Store Releases and Production Releases
        self.release_data = {"release_production": {}, "release_prerelease": {}}
        self.release_data_get()
        # Query Current Release
        self.release_type = "production"
        self.release_version = sorted(list(self.release_data["release_" + self.release_type].keys()))[-1]

    def release_data_get(self):
        """
        Release Data Lookup via GitHub API
        :parm none:
        :return self.release_data:
        """
        # Release Data Lookup via GitHub API
        data = "{}"
        try:
            with contextlib.closing(urllib.request.urlopen(urllib.request.Request(LYNX_repo_url + "/releases"),
                                                    context=ssl._create_unverified_context())) as response:
                data = response.read()
                data = "{}" if data == "" else data
        except:
            pass
        # Relase Data Parse
        data = json.loads(data.decode('utf-8'))
        for release in data:
            self.release_data["release_prerelease" if release["prerelease"] == True else "release_production"][
                release["tag_name"]] = {"url": release["zipball_url"]}

    def release_install(self):
        """
        Download and peform installation with set preferences.
        :parm none:
        :return none:
        """

        file_path = self.download_url(self.release_data["release_" + self.release_type][self.release_version]["url"])
        file_path = self.compress(file_path)

        # Houdini
        if ("HOUDINI" in self.env):
            packages_path = os.path.join(os.getenv("HOUDINI_USER_PREF_DIR"), "packages")
            if not os.path.exists(packages_path):
                os.makedirs(packages_path)

            # Configure Package
            file_path = packages_path + "/" + "LYNX.json"
            shutil.copy(os.environ["LYNX"] + "/" + "plugins/SideFX/Houdini/packages/LYNX.json", file_path)
            with open(file_path, 'r') as file:
                data = file.read()
            data = json.loads(data.decode('utf-8'))
            data["env"][0]["LYNX"] = os.environ["LYNX"]
            with open(file_path, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    def release_uninstall(self):
        """
        Peform uninstall.
        :parm none:
        :return none:
        """

        # Remove Release
        shutil.rmtree(os.environ["LYNX"])
        del os.environ["LYNX"]

        # Houdini
        if ("HOUDINI" in self.env):
            # Remove Packge .json file
            packages_path = os.path.join(os.getenv("HOUDINI_USER_PREF_DIR"), "packages")
            file_path = packages_path + "/" + "LYNX.json"
            if (os.path.isfile(file_path)):
                os.remove(file_path)

    def download_url(self, url):
        """
        Download file at url
        :parm url:
        :return file_path:
        """
        if not os.path.exists(os.environ["LYNX"]):
            os.makedirs(os.environ["LYNX"])
        file_path = os.environ["LYNX"] + "/" + "LYNX_" + os.path.basename(url) + ".zip"
        try:
            file_content = urllib.request.urlopen(url, context=ssl._create_unverified_context())
            with open(file_path, 'wb') as output:
                output.write(file_content.read())
        except:
            raise ValueError("Unable to download the package file :" + url)

        return file_path

    def compress(self, file_path, mode="extract", archive_type="zip"):
        """
        compress or decompress archive file
        :parm file_path, mode, archive_type:
        :return file_path:
        """
        if (mode == "extract"):
            if (archive_type == "zip"):
                # Extract Archive
                with zipfile.ZipFile(file_path, 'r', zipfile.ZIP_DEFLATED) as archive:
                    archive.extractall(os.path.dirname(file_path))
                    archive_path = os.path.dirname(file_path) + "/" + archive.namelist()[0][:-1]
                os.remove(file_path)
                # Move Files To Parent Directory
                for file in os.listdir(archive_path):
                    shutil.move(archive_path + "/" + file, os.path.dirname(file_path) + "/" + file)
                os.rmdir(archive_path)

                file_path = os.path.dirname(file_path)

        return file_path

    def ui_LYNX_update_manager(self):
        """
        Init UI
        :parm none:
        :return none:
        """
        # Currently binded to Houdini > Make this general purpose
        dialog = QT_LYNX_update_manager(hou.ui.mainQtWindow(), self)
        dialog.show()

