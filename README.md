# Documentation
Documentation for LightBurn laser software

## Disclaimer
By using this software, the user accepts complete responsibility for each and every
aspect of safety associated with the use of the Laser machine, Laser system and
Lightburn Software.
***You agree that:***
1. You will not hold the author or contributors of LightBurn liable for any damage to
equipment or persons from the use of LightBurn.
2. You know the potential hazards in using high power lasers and high voltages.
3. You will wear professional laser-eye-protection when using a laser controlled by
LightBurn
4. You will use the LightBurn software in a legal and safe manner.
5. You relieve the author and contributors from any liability arising from the use or
distribution of the LightBurn software.
6. You are entirely operating at your own risk. Lasers can be lethally dangerous.


## Table of Contents
* [Prerequisites](PreReq.md)
* [Read Me](README.md)
  * [General Usage Notes](#generalUsage)
* [About LightBurn](AboutLightBurn.md)
* [Device Setup](DeviceWizard.md)
* [Working with Vectors](WorkingWithVectors.md)
  * [Creating New Vectors](CreatingNewVectors.md)
  * [Importing External Vectors](ImportingExternalVectors.md)
  * [Cut, Scan & Cut+Scan](Operations.md)
* [Working with Images](WorkingWithImages.md)
  * [Engraving Images](EngravingImages.md)
* [Laser Operation](LaserOperation.md)
* [G-Code](G-Code.md)
* [Hot Keys and Gestures](HotKeys.md)
<a name="generalUsage"></a>
## General Usage Notes
If you've never run LightBurn, the first thing you need to do is set up your machine layout (work area size and zero / origin) in the settings, and then add your device type in the devices box.  If you have more than one type of laser / device, you can add more than one and choose a default.  At present, the layout and page size aren't associated with the device, but I want to change that in the future.

If you need to reset your device connection, simply open the devices menu, then hit ok.  LightBurn does a full disconnect / reconnect cycle when you click ok in the devices menu.

If you don't know what a button / option does, hover the mouse over it.  I often add tool-tip help to things to explain them better.

Most feature hot-keys can be found next to the action in the menus.  I've tried to put everything in menus and toolbars to make it easier to use, but also to make the hotkeys for things visible.

If a button doesn't seem to do anything or ever enable, it's probably a feature that's not written or connected yet.  There are a few of those - I'm just one person.

The toolbars and windows can all be dragged around if you don't like the layout.  Whatever you end up with is saved when you quit.


