[Return to main page](README.md)

----

# Installation

## Download 
Download the latest release version that matches your computer. 
* Windows 64-bit
* Windows 32-bit
* Mac OSX
* Linux 64-bit

## Windows Installation
![LightBurn Setup](/img/Setup-1.png)

1. Launch the installer executable
2. Windows may ask if you trust the software, as LightBurn is not currently digitally signed
3. Select if you would like to create a desktop icon
4. Click *Install*
5. Click *Finish*

That's it! Locate the LightBurn icon to launch the program



## Mac/OSX Installation

1. Download the Mac/OSX version
2. Double-click the .zip file to extract the DMG (disk-image) file
3. Double-click the LightBurn.dmg file to mount it
4. Drag the LightBurn application into your applications folder
5. Launch LightBurn from the launcher as normal
6. You can now eject the DMG file (drag it to the trash bin)

## Linux Installation

1. Open a terminal and run the following command:
   - `sudo adduser $USER dialout && sudo adduser $USER tty`
2. **IMPORTANT!** Log out and log back in (this refreshes the permissions we just added)
3. Download the Linux 64-bit version, either the `.run` file or the `.7z` file and follow the appropriate steps below:

#### `.run` installer

4. Open your terminal and `cd` to the directory you downloaded the file to.
5. Run `bash ./LightBurn-Linux64-v*.run`
6. It will now automatically install and create a program listing in your desktop environment.

#### `.7z` installer
4. Extract the folder wherever you want Lightburn to exist
5. Right click `AppRun` > Properties > Permissions > 'Allow executing file as program'
5. Double click `AppRun` inside your Lightburn folder

