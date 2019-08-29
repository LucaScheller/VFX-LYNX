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

def enabled():
    enabled = 0

    # Check for host application
    with open(os.path.join(os.environ["HOUDINI_USER_PREF_DIR"], "hcommon.pref"), "r") as f:
        for line in f.readlines():
            if line.startswith("sendAnonymousStats"):
                if line.strip().strip(";").split(":=")[1].strip() == "1":
                    enabled = 1
                break
    enabled *= int(os.getenv("HOUDINI_ANONYMOUS_STATISTICS", 1))

    # Check for LYNX_analytics
    if("LYNX_ANALYTICS" in os.environ.keys()):
        enabled = int(os.environ["LYNX_ANALYTICS"])

    return enabled

def node_OnCreated(node):
    # Skip asset internal nodes
    if (node.isInsideLockedHDA()==True): return

    if enabled():
        node_hda_file_path = node.type().definition().libraryFilePath()
        LYNX_analytics.event_send(hou.applicationPlatformInfo(),hou.applicationName(),hou.applicationVersionString(),hou.licenseCategory().name(),"Plugin", "SideFX/Houdini/otls/"+os.path.split(node_hda_file_path)[-1], str(node.type().name()), 0)

