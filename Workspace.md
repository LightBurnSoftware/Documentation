[Return to main page](README.md)

# Workspace / User Interface

## Overview

![User Interface](/img/Desktop.png)

The user interface is grouped into several categories. 

* [Tools and toolbars](#toolbars)
* [Tool Windows and tabs](#toolboxes)
* [Workspace](#workspace)

Most tools and areas of the application have helpful tips if you hover over them. 

![ToolTips](/img/ToolTip.PNG)

<a name="toolbars"></a>

----

## Tools and Toolbars

The toolbars and the tools they contain will allow you to manipulate your work. The function of each tool is covered in the [Toolbars](Toolbars.md) section.

You can enable or disable toolbars by right clicking on any open space on a toolbar to bring up the context menu. This will allow you to turn on or off toolbars and toolboxes to fit your work style.

![Toolbars](/img/Toolbars.PNG)

<a name="toolboxes"></a>

----

## Tool Windows and Tabs

Tool Windows provide a grouped set of tools for various operations. Here you will find your [Cuts](#cuts), [File List](#filelist), [Laser](#laser), [Move](#move), [Shape Properties](#shapeproperties) and [Console](#console) toolboxes. 

### Manipulating Tool Windows and Tabs

You can undock a tool window and make it floating by dragging it away from the other tool windows. You can also click the min/max button in the upper right of the tool window to undock it.

You can dock the tool window by itself by dragging it to the right or left of the screen and dropping it in an area that highlights blue when you hover over it.

You can dock the tool window as a tab by dropping it on top of another docked tool window.

You can close a tool window by clicking the X in the upper right of the tool window or by turning it off in the toolbar context menu as seen in the [Tools and Toolbars](#toolbars) section above.

You can reorder tabs by clicking on the tab and dragging it left or right in the tab strip.

<a name="cuts"></a>
### Cuts

The Cuts tool window is where you will configure most of your job. It contains layers of cut operations that can be reordered and have various machine operations configured.  Details of the possible Modes and settings are covered in the [Operations](Operations.md) section.

![Cut Tool WIndow](/img/CutsToolBox.PNG)

* A right click on a cut layer will cause the items that are on that cut layer to flash in the workspace. 
* Double clicking a cut layer will launch the full settings editor for that layer
* You can quickly select the Mode or set the layer Output and Hide options directly from the tool window
* You can quickly set the basic operation parameters in the *Cut Info* section
* Clicking the up or down arrows on the right side of the tool window will move the selected layer up or down in priority

<a name="filelist"></a>
### File List

TODO: Content needed

<a name="laser"></a>
### Laser

The Laser tool window is used to interact with the connected device. 

![Laser Tool Window](/img/LaserToolBox.PNG)

This tool window provides most of the functions for interacting directly with your laser. The commands are covered in detail elsewhere in the documentation. 

For a detailed explaination of the *Start From* options, see [Coordinates and Origin](CoordinatesOrigin.md)

<a name="move"></a>
### Move

The Move tool window is used primarily for Jog and Home functions

![Move Tool Window](/img/MoveToolBox.PNG)

Here you can manually jog your laser head to different positions by selecting one of the arrow buttons around the home button. This will move your head by the set distance, speed and power entered in the toolbox. 

You can also set or clear a custom origin or get the current reported position.

<a name="shapeproperties"></a>
### Shape Properties

Shape properties is used for setting a percentage of power for a given shape. This allows you to set different shapes within the same layer to a higher or lower laser power percentage without creating a new layer. This is especially useful for creating test patterns and is covered in detail in the Video [LightBurn progress demo #9 - Power Scaling](https://www.youtube.com/watch?v=ZiUAOv4tAGY)

![Shape Properties Tool Window](/img/ShapePropertiesToolBox.PNG)

<a name="console"></a>
### Console

On non-Ruida machines, a console toolbox is available for directly inputting commands. You can type a command in the text box and the console will output the results. Examples would be manual G-Code commands or retrieving configuration details from your connected device. 

Note, this is not available on some connected devices including Ruida.

![Console Tool Window](/img/ConsoleToolBox.PNG)

<a name="workspace"></a>

-----

## Workspace

The workspace is a versatile interface for manipulating your drawings. Some ways to interact with the workspace include:

* Drag and drop supported files onto the workspace to import them
* Use the tools to draw vector shapes directly in the workspace
* Manipulate the size and rotation of shapes and images
* Move your laser head using the locator tool and clicking an area of the workspace
* Review your machine and job origin
* Type text

New features are being added quickly so this may not be a comprehensive list of all of the capabilities. Documentation will be added or updated as quickly as possible as new features are made available.

Many hot keys have been added to increase your productivity. See the [Hot Keys](HotKeys.md) section for details.
