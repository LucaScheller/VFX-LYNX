'''
#### To Do ####
- class based approach
'''

# Dependencies
import os, uuid, json, httplib, urllib

### All functions assume that the environ var LYNX is valid

GA_TRACKING_ID = "UA-146460993-2"

LYNX_config_file_path = os.environ["LYNX"]+"/etc/LYNX.config"

# Check if analytics are enabled
def enabled():
    enabled = 0

    # Check preference file
    with open(LYNX_config_file_path, 'r') as f:
        content = json.load(f)
        enabled = content.get('ANALYTICS', {}).get('enabled', 0)

    # Check LYNX_ANALYTICS environment variable
    if("LYNX_ANALYTICS" in os.environ.keys()):
        enabled = int(os.environ["LYNX_ANALYTICS"])

    return enabled

# Create/Save/Load tracking id
def uuid_get():
    
    tracking_id = None

    if not os.path.exists(LYNX_config_file_path):
        tracking_id = str(uuid.uuid4())
        file_content = {"ANALYTICS": {"UUID":tracking_id}}
        with open(LYNX_config_file_path, 'w') as f:
            json.dump(file_content, f, indent=4, sort_keys=True)
    else:
        with open(LYNX_config_file_path, 'r') as f:
            content = json.load(f)
            tracking_id = content.get('ANALYTICS', {}).get('UUID')
        if tracking_id == None:
            tracking_id = str(uuid.uuid4())
            content.setdefault("ANALYTICS",{})["UUID"] = tracking_id
            with open(LYNX_config_file_path, 'w') as f:
                json.dump(content, f, indent=4, sort_keys=True)

    return str(tracking_id)

def event_send(application_platform,application_name,application_version,application_license,category, action, label, value=0):
    # Google Analytics using Measurement Protocol.
    data = {
        'v'    : '1',                         # API Version.
        'tid'  : GA_TRACKING_ID,              # Tracking ID / Property ID.
        'cid'  : uuid_get(),                  # UUID
        'ua'   : str(application_platform),   # Application Platform / User Agent
        'an'   : str(application_name),       # Application Name
        'av'   : str(application_version),    # Application Version
        'aiid' : str(application_license),    # Application Installer Id > License
        't'    : 'event',                     # Event hit type.
        'ec'   : str(category),               # Event category.
        'ea'   : str(action),                 # Event action.
        'el'   : str(label),                  # Event label.
        'ev'   : value,                       # Event value, must be an integer
        'aip'  : '1',                         # Anonymize ip
        #'dt'   : action,                     # Document Title
    }

    params = urllib.urlencode(data)
    connection = httplib.HTTPConnection('www.google-analytics.com')
    connection.request('POST', '/collect', params)