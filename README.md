| <img src="https://github.com/LucaScheller/VFX-LYNX/blob/master/resources/LYNX_logo.svg" width="128"> |  <h2> LYNX  Free & OpenSource VFX Pipeline Tools </h2> |
|--|--|


## Overview

LYNX VFX Pipeline Tools are a collection of production proven open source tools to accelerate your workflows! 

Development Roadmap | [https://trello.com/b/f8Pgip7s/lynxpipeline](https://trello.com/b/f8Pgip7s/lynxpipeline) 

Have feedback? Want to help development? [Report a bug](https://github.com/LucaScheller/VFX-LYNX/issues) or [contact me](https://www.lucascheller.de/contact/) directly :)

Big thank you to Patrick Zeller, Philipp Engelhardt, Chris Kelch, Ryan Leasher, Hernan Santander, Bill Martin and Geoff Bailey for giving valuable feedback for improving the tools! 


## Getting Started

After downloading the tools (see the Installation Guide below), visit my [Blog](https://www.lucascheller.de/blog/)  and my [Vimeo Page](https://vimeo.com/lucascheller) for  tutorials and feature explanations.

To access the example files used in the tutorial videos, see the "examples" folder in the corresponding plugin directory.

All Houdini Assets have complete Houdini native documentation available.


## Houdini Tools

| Tools | Supported Houdini Versions | Features |
|--|--|--|
| LYNX_force_general | 17.5 and newer | Tweak your sims with this all purpose & intuitive force field. |
| LYNX_fabric        | 17.5 and newer | Create fabric/weave patterns with ease. |
| LYNX_velocity      | 17.5 and newer | Get control of your velocities via an intuitive UI or groom them for absolute fine tuned control.|
> **Note:**  While using the tools in older versions is possible, full feature support may be limited.


## Installation Guide:

### Step 1/2 | Download LYNX

> **Option 1 (For Git Users)**: 
	Navigate to the folder you want to contain LYNX, and from your terminal git clone https://github.com/LucaScheller/VFX-LYNX

> **Option 2 (For Non-Git Users)**: 
	Download the desired release directly from the [releases page](https://github.com/LucaScheller/VFX-LYNX/releases) and extract it to your hard drive or network share.

### Step 2/2 | Configuring Your Environment

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

### Alternative Installation | Quick Install
If you just want to get the tools to try them out, you can quick install certain parts of the toolset.
> **Houdini Assets**: 
	Just drop all the folders in the LYNX/plugins/SideFX/Houdini/otls folder into your /otls folder in the above described preferences location.


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