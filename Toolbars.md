[Return to main page](README.md)
<a name="Top"></a>
## Toolbars and Tool Windows

The workspace has may toolbar and tool windows to make working with files fairly easy and intuitive. Right clicking on the top bar of the app will allow you to toggle toolbars on or off, as will using the 'Window' menu in the main menu bar.

![Toolbars](/img/Toolbars.PNG)



### Manipulating Tool Windows and Tabs

You can undock a tool window and make it floating by dragging it away from the other tool windows. You can also click the min/max button in the upper right of the tool window to undock it.

You can dock the tool window by itself by dragging it to the right or left of the screen and dropping it in an area that highlights blue when you hover over it.

You can dock the tool window as a tab by dropping it on top of another docked tool window.

You can close a tool window by clicking the X in the upper right of the tool window or by turning it off in the toolbar context menu as seen in the [Tools and Toolbars](#toolbars) section above.

You can reorder tabs by clicking on the tab and dragging it left or right in the tab strip.

[Return to Top](#Top)

#### Tool Windows provide a grouped set of tools for various operations. 

* [Cuts](#cuts)
* [File List](#filelist)
* [Laser](#laser)
* [Move](#move)
* [Shape Properties](#shapeproperties)
* [Console](#console)  

#### Toolbars are similar to Tool Windows, but are a grouped set of icons for various types of operations.

* [Tools](#Tools)
* [Arrange](#Arrange)
* [Numeric Edits](#Numeric)
* [Text Edits](#Text)

[Return to Top](#Top)

<a name="cuts"></a>
### Cuts

The Cuts tool window is where you will configure most of your job. It contains layers of cut operations that can be reordered and have various machine operations configured.  Details of the possible Modes and settings are covered in the [Operations](Operations.md) section.

![Cut Tool WIndow](/img/CutsToolBox.PNG)

* A right click on a cut layer will cause the items that are on that cut layer to flash in the workspace. 
* Double clicking a cut layer will launch the full settings editor for that layer
* You can quickly select the Mode or set the layer Output and Hide options directly from the tool window
* You can quickly set the basic operation parameters in the *Cut Info* section
* Clicking the up or down arrows on the right side of the tool window will move the selected layer up or down in priority (as will editing the Priority value below)

[Return to Top](#Top)

<a name="filelist"></a>
### File List

This is currently for Ruida controllers, but will be implemented for Smoothie controllers as well. This window lets you manage the files hosted on your controller, if it supports this.

![FileListWindow](/img/FileListWindow.png)

Hit the Refresh button to query your controller for the list of hosted files. You can select a file and press Start to cut it, Delete to remove it from the controller, or Download to save it locally. Pressing Upload will let you choose a local cut file to send to the controller (this is not the same as the current job, which you can upload with the "Send" button in the Laser window - see the [Machine Instructions](MachineInstructions.md) page for more details)



[Return to Top](#Top)

<a name="laser"></a>
### Laser

The Laser tool window is used to interact with the connected device. 

![Laser Tool Window](/img/LaserToolBox.PNG)

This tool window provides most of the functions for interacting directly with your laser. The commands are covered in detail elsewhere in the documentation.

For a detailed explanation of the *Start From* options, see [Coordinates and Origin](CoordinatesOrigin.md)

[Return to Top](#Top)

<a name="move"></a>
### Move

The Move tool window is used primarily for Jog and Home functions

![Move Tool Window](/img/MoveToolBox.PNG)

Here you can manually jog your laser head to different positions by selecting one of the arrow buttons around the home button. This will move your head by the set distance, speed and power entered in the toolbox. 

You can also set or clear a custom origin or get the current reported position.

[Return to Top](#Top)

<a name="shapeproperties"></a>
### Shape Properties

Shape properties is used for setting a percentage of power for a given shape. This allows you to set different shapes within the same layer to a higher or lower laser power percentage without creating a new layer. This is especially useful for creating test patterns and is covered in detail in the Video [LightBurn progress demo #9 - Power Scaling](https://www.youtube.com/watch?v=ZiUAOv4tAGY)

![Shape Properties Tool Window](/img/ShapePropertiesToolBox.PNG)

[Return to Top](#Top)

<a name="console"></a>
### Console

On non-Ruida machines, a console toolbox is available for directly inputting commands. You can type a command in the text box and the console will output the results. Examples would be manual G-Code commands or retrieving configuration details from your connected device. 

Note, this is not available on some connected devices including Ruida.

![Console Tool Window](/img/ConsoleToolBox.PNG)

[Return to Top](#Top)

<a name="workspace"></a>
## Main Toolbar

[Return to Top](#Top)

<a name="Tools"></a>
## Tools Toolbar

On the left of the workspace in the default configuration, there is a tool bar with many of the commonly used tools. These are also duplicated in the tool menu at the top of the workspace. The tools are as follows:


### Select
Click on the "Select" icon to select objects in the workspace, or to access menus and toolbars.
### Draw Lines
Click on the "Draw Lines" icon to draw straight lines in the workspace.
### Rectangle Tool
Click on the "Rectangle" icon todraw rectangles in the workspace.
### Ellipse Tool
Click on the "Ellipse" icon to draw ellipses in the workspace.
### Edit Nodes
Click on the "Edit Nodes" icon to edit nodes of objects in the workspace.
### Edit Text
Click on the "Edit Text" icon to create or edit text in the workspace.
### Position Laser
Click on the "Position Laser" icon to allow clicking on the workspace to move the laser head to that location.
### Offset Vectors
Click on the "Offset Vectors" icon to createnew vectors that are an offset of the original vector selected.

[Return to Top](#Top)

<a name="Arrange"></a>
## Arrange Toolbar

[Return to Top](#Top)

<a name="Numeric"></a>
## Numeric Edits Toolbar

[Return to Top](#Top)

<a name="Text"></a>
## Text Options Toolbar

[Return to Top](#Top)


