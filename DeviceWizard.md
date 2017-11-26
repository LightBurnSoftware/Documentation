[Return to main page](README.md)
# Device Setup

If you've never run LightBurn, the first thing you need to do is set up your machine layout (work area size and zero / origin) in the settings, and then add your device type in the devices box.  If you have more than one type of laser / device, you can add more than one and choose a default.  At present, the layout and page size aren't associated with the device, but this will be changed to that in the future.

## Adding a new device (Laser)
If you've never used LightBurn before, you'll need to tell it a couple things about your hardware to get going.

1. In the lower-right of the display is a box called "Laser" - on the bottom of it is a button called "Devices". Click it.

![Laser Module](/img/LaserToolBox.PNG)

2. Click the *New Device* button (highlighted in red, below):

![Device Wizard Empty](/img/DeviceWizardEmpty.PNG)

3. Choose a device that matches the one in your laser. Don't worry if you have more than one laser. Start with one for now, and add the others later.

![Devices Wizard](/img/DevicesWizard.PNG)

4. Choose your connection method. Serial/USB, Network, etc...

![Device Wizard Connection](/img/DeviceWizardConnection.PNG)

5. Choose a distinct name and set your machine bed size for X and Y

![Device Wizard Dimensions](/img/DeviceWizardDimensions.PNG)

6. Choose the 0,0 origin point that matches your machine

![Device Wizard Origin](/img/DeviceWizardOrigin.PNG)

7. Click *Finish* to save your laser setup

![Device Wizard Finish](/img/DeviceWizardFinish.PNG)

If your laser is connected to the computer, LightBurn will try to establish communication.  For some systems this will home the laser, for others it will simply show "Ready" in the status box at the top of the laser tab, or the bottom status bar, depending on your system.

If you are adding multiple devices, repeat the steps above for each machine. When you are done, you can set the default connection by clicking on the name in the device list and clicking the *Make Default* button. 

You may also edit or remove devices by clicking the device and choosing the appropriate button.
