| <img src="https://github.com/LucaScheller/VFX-LYNX/blob/master/LYNX_logo.svg" width="128"> |  <h2> LYNX  Free & OpenSource VFX Pipeline Tools </h2> |
|--|--|


## Overview

LYNX VFX Pipeline Tools are a collection of production proven open source tools to accelerate your workflows! 

Development Roadmap | [https://trello.com/b/f8Pgip7s/lynxpipeline](https://trello.com/b/f8Pgip7s/lynxpipeline) 

Have feedback? Want to help development? [Report a bug](https://github.com/LucaScheller/VFX-LYNX/issues) or [contact me](https://www.lucascheller.de/contact/) directly :)

Big thank you to Patrick Zeller, Philipp Engelhardt, Ryan Leasher, Hernan Santander, Bill Martin and Geoff Bailey for giving valuable feedback for improving the tools! 

## Getting Started

After downloading the tools (see the Installation Guide below), visit my [Blog](https://www.lucascheller.de/blog/)  and my [Vimeo Page](https://vimeo.com/lucascheller) for  tutorials and feature explanations.

To access the example files used in the tutorial videos, see the "examples" folder.

All Houdini Assets have complete Houdini native documentation available.



## Houdini Tools

| Tools | Supported Houdini Versions | Features |
|--|--|--|
| LYNX_force_general | 17.5 * | Tweak your sims with this all purpose & intuitive force field. |
| LYNX_fabric        | 17.0 and newer | Create fabric/weave patterns with ease. |
| LYNX_velocity      | 17.0 and newer | Get control of your velocities via an intuitive UI or groom them for absolute fine tuned control.|
> **Note:**  While using it in older versions is possible, full feature support may be limited.



## Installation Guide:

### Step 1/2 | Download LYNX

> **Option 1 (For Git Users)**: 
	Navigate to the folder you want to contain LYNX, and from your terminal git clone https://github.com/LucaScheller/VFX-LYNX

> **Option 2 (For Non-Git Users)**: 
	Download the desired release directly from the [releases page](https://github.com/LucaScheller/VFX-LYNX/releases) and extract it to your hard drive or network share.

### Step 2/2 | Configuring Your Environment

You have to edit files in the following location depending on your operating system:
- Windows: C:\Users\YourUserNameHere\Documents\houdini17.5
- Linux:   $HOME/houdini17.5
- Mac:     $HOME/Library/Preferences/houdini/houdini17.5

> **Option 1 (17.5 and newer)**: 
	Add a folder called "packages" and place the LYNX.json file into that folder. The LYNX.json file can be found in your downloaded LYNX package under HOUDINI/HSITE/packages/LYNX.json. Then edit LYNX.json and change the "path" variable to match the install path. The folder you point to should be the one that contains "otls" and "examples".
	
> **Option 2**: 
	Edit your houdini.env file and create a variable called LYNX that points to the new folder you just extracted LYNX to. The folder you point to should be the one that contains "otls" and "examples". Then add it $LYNX to your HOUDINI_PATH: 
	
	LYNX="/path/to/LYNX/HOUDINI/HSITE"
	HOUDINI_PATH= $HOUDINI_PATH;$LYNX;$OtherLibrary_A;$OtherLibrary_B;&

> **Note:**  On Linux and OSX, use : instead of ; to separate your paths. Also make sure that HOUDINI_PATH always ends in ;& so that Houdini's internal operators are loaded correctly.

### Alternative Installation | Quick Install
If you just want to get the tools to try them out, the quickest way is to just drop all the folders in the LYNX/HOUDINI/HSITE/otls folder into your /otls folder in the above described preferences location.


## Notice:
This software is provided AS-IS, with absolutely no warranty of any kind, express or otherwise. We disclaim any liability for damages resulting from using this software.