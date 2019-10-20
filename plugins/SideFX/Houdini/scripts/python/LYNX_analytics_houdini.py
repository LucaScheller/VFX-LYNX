'''
#### To Do ####
- class based approach
'''

# Dependencies
import os,sys
import hou

# Load LYNX_analytics module >> This raises an error if the variable doens't exist
sys.path.append(os.environ["LYNX"]+"/lib/")
import LYNX_analytics

  
def node_OnCreated(node):
    # Skip asset internal nodes
    if (node.isInsideLockedHDA()==True): return

    if LYNX_analytics.enabled(lambda : int(1-hou.ui.displayMessage(title="LYNX | Analytics",text="We use Google Analytics to collect data about our tools. \n You can find out more about what data is collected on the LYNX GitHub Page. \n Do you want to enable data collection?", buttons=("Yes", "No")))):
        node_hda_file_path = node.type().definition().libraryFilePath()
        LYNX_analytics.event_send(hou.applicationPlatformInfo(),hou.applicationName(),hou.applicationVersionString(),hou.licenseCategory().name(),"Plugin", "SideFX/Houdini/otls/"+os.path.split(node_hda_file_path)[-1], str(node.type().name()), 0)

