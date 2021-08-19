
| <img src="https://github.com/LucaScheller/VFX-LYNX/blob/master/resources/LYNX_logo.svg" width="128"> |  <h2> LYNX  Free & OpenSource VFX Pipeline Tools </h2> |
|--|--|


## Overview

LYNX VFX Pipeline Tools are a collection of production proven open source tools to accelerate your workflows! 

[Development Roadmap](https://github.com/LucaScheller/VFX-LYNX/projects/1) | View the current development roadmap.

[Feedback/Suggestions/Bug Tracking](https://github.com/LucaScheller/VFX-LYNX/issues) | Have feedback? Want to help development? Found a bug? Let me know!

[Contact Us](https://www.lucascheller.de/contact/) | Have general questions regarding the project? Drop me a line :)

Big thank you to Patrick Zeller, Philipp Engelhardt, Chris Kelch, Ryan Leasher, Hernan Santander, Bill Martin and Geoff Bailey for giving valuable feedback for improving the tools! 


## Getting Started

After installing the tools (see the Installation Guide below), visit my [Blog](https://www.lucascheller.de/blog/)  and my [Vimeo Page](https://vimeo.com/lucascheller) for  tutorials and feature explanations.

To access the example files used in the tutorial videos, see the "examples" folder in the corresponding plugin directory.

All Houdini Assets have complete Houdini native documentation available.


## Houdini Tools

| Tools | Supported Houdini Versions | Features |
|--|--|--|
| LYNX_force_general | 17.5 and higher | Tweak your sims with this all purpose & intuitive force field. |
| LYNX_fabric        | 17.5 and higher | Create fabric/weave patterns with ease. |
| LYNX_velocity      | 17.5 and higher | Get control of your velocities via an intuitive UI or groom them for absolute fine tuned control.|
> **Note:**  While using the tools in older versions is possible, full feature support may be limited. You can download older releases that support previous versions of Houdini on the [Releases Page](https://github.com/LucaScheller/VFX-LYNX/releases).


## Installation Guide:

### Automatic Installation via LYNX_update (The official LYNX installer.)

The LYNX_update program is the most convenient way to install LYNX. All you have to do is restart the application after the installation is finished and you're good to go. It makes switching between different LYNX releases merely a click of a button. This installer is also available from the LYNX.shelf in Houdini in all releases 1.0.9 or higher. The installer essentially provides a UI for the below mentioned manual installation. It is compatible with Houdini 17.5 and higher and uses the packages installation workflow.

To execute the installer in Houdini, open the "Python Source Editor" (Windows>Python Source Editor) and paste and apply the following python snippet preferably in a clean Houdini session:

    import urllib,ssl
    LYNX_update_url = 'https://raw.githubusercontent.com/LucaScheller/VFX-LYNX/master/lib/LYNX_update.py'
    exec(urllib.request.urlopen(LYNX_update_url,context=ssl._create_unverified_context()).read(), globals(), locals())
    LYNX_update_manager_object = LYNX_update_manager()
    LYNX_update_manager_object.ui_LYNX_update_manager()

### Manual Installation 

#### Step 1/2 | Download LYNX

> **Option 1 (For Git Users)**: 
	Navigate to the folder you want to contain LYNX, and from your terminal git clone https://github.com/LucaScheller/VFX-LYNX

> **Option 2 (For Non-Git Users)**: 
	Download the desired release directly from the [releases page](https://github.com/LucaScheller/VFX-LYNX/releases) and extract it to your hard drive or network share.

#### Step 2/2 | Configuring Your Environment

Next up you have to edit your environment to include the package.

You have to edit files in the following location depending on your operating system:
- Windows: C:\Users\YourUserNameHere\Documents\houdini17.5
- Linux:   $HOME/houdini17.5
- Mac:     $HOME/Library/Preferences/houdini/houdini17.5

> **Option 1 (17.5 and newer)**: 
	Add a folder called "packages" and place the LYNX.json file, which can be found in your downloaded LYNX package under /plugins/SideFX/Houdini/packages/LYNX.json, into that folder. Then edit LYNX.json and change the "LYNX" variable to match the install path. The folder you point to should be the new folder you just extracted LYNX to.
	
> **Option 2**: 
	Edit your houdini.env file and create a variable called LYNX that points to the new folder you just extracted LYNX to. Then add $LYNX/plugins/SideFX/Houdini to your HOUDINI_PATH: 
	
	LYNX="/Path/To/LYNX/"
	HOUDINI_PATH=$HOUDINI_PATH;$LYNX/plugins/SideFX/Houdini;$OtherLibrary_A;$OtherLibrary_B;&

> **Note:**  On Linux and OSX, use : instead of ; to separate your paths. Also make sure that HOUDINI_PATH always ends in ;& so that Houdini's internal operators are loaded correctly.


## Analytics
For more information see the "Verwendung von Google Analytics" section in our [Privacy Policy](https://www.lucascheller.de/imprint-privacypolicy/). Any additions are described in detail below. 

> **What's the purpose of using analytics?**
When using LYNX, non personal data can be optionally collected via Google Analytics. This helps us get feedback and prioritize the development to give you the best possible version of our product in future releases.

> **What data is collected?**
The only information associated with an individual user is a randomized UUID that in no way contains any personal data like an IP address, name or location. The UUID is automatically generated on the first activation of analytics and saved into the /etc/LYNX.config file. It will remain unchanged indefinitely, unless the file or the corresponding entry inside the file are removed. This is similar to a cookie in a browser. All other types of data are user independent.
Examples of data collected include:
>- Randomized UUID
>- Application Platform/Name/Version/License (i.e., Houdini FX, Houdini Batch, Houdini Apprentice, etc.)
>- Usage information for different Houdini node types

> **How can data collection be enabled/disabled?**
If your user preference for data collection is not found, you will be asked to allow or reject data collection via a popup. This setting will be used accross all LYNX tools and plugins by default. You can override or change your preference as described below.
Whether data is being collected or not depends on the value of the "enabled" variable under "ANALYTICS" in your LYNX preferences file under /etc/LYNX.config. Additionally if the environment variable LYNX_ANALYTICS exists, its value will override the value found in the preferences. If neither preferences and nor environment variable are found, no data will be collected.
A value of 1 will enable data collection, a value of 0 will disable data collection. This means if you want to only locally enable analytics for let's say the Houdini plugin, you can add the variable to your Houdini environment by adding the following to your houdini.env file:

    LYNX_ANALYTICS=1

## Notice:
This software is provided AS-IS, with absolutely no warranty of any kind, express or otherwise. We disclaim any liability for damages resulting from using this software.
