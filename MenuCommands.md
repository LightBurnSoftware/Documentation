[Return to main page](README.md)
<a name="MenuCommands"></a>
# Menu Commands

If you don't know what a button / option does, hover the mouse over it. Tool-tips are often added to help in explaining them better.

If a button doesn't seem to do anything or ever enable, it's probably a feature that's not written or connected yet.  There are a few of those - there is only one developer working on the coding at the moment.

The toolbars and windows can all be dragged around if you don't like the layout.  Whatever you end up with is saved when you quit.



----------------------------------

### [File Menu](#FileMenu)
### [Edit Menu](#EditMenu)
### [Tools Menu](#ToolsMenu)
### [Arrange Menu](#ArrangeMenu)
### [Window Menu](#WindowMenu)
### [Language Menu](#LanguageMenu)
### [Help Menu](#HelpMenu)

----------------------------------------------

<a name="FileMenu"></a>
## File Menu 

### New
Clicking "New" in the File Menu will clear any current project and create a new one.
You can also press "Ctrl + N" (Command + N on Mac).

### Open recent projects
This will open a list of the most recently opened files to choose from.

### Open
To open an existing or saved file, click on “Open” in the File menu or press "Ctrl + O" (Command + O on Mac).

### Import
You can import any supported LightBurn files into the file you are currently working on. Click on “Import” in the File menu or press “Ctrl – I” LightBurn supports importing the following file types: svg, ai, pdf, dxf, hpgl, plt, png, jpg, bmp.

### Save
To save a project click on “Save” in the File menu or press "Ctrl + S".  Type the name you want the file saved as in the dialog box that opens up. To save a file with changes, but still keep the original file intact, click on the “Save As” icon in the File menu.

### Export
To export a file to a different file format, click on “Export” in the File menu. LightBurn can export to SVG or AI format, though bitmaps and text are currently not exported.

### Exit 
To exit LightBurn, click on the “Exit" in the File menu or press “Ctrl – Q”.  You will be prompted to save your file if you have unsaved changes.

[Return to top](#MenuCommands)

----------------------------------
<a name="EditMenu"></a>
## Edit Menu

### Undo
To undo the last editing action done on the current file, click on "Undo" in the Edit menu or press "Ctrl + Z".
### Redo
To Redo the last editing action done on the current file, click on "Redo" in the Edit menu or press "Shift + Ctrl + Z".
### Select all
To select all objects in the current file click on "Select all" in the Edit menu or press "Ctrl + A" (or Command + A on Mac).
### Cut
To one or more objects from the current file, select them and click on "Cut" in the Edit menu or press "Ctrl + X". This will put the object on the clipboard, and remove it from the current file.
### Copy
To copy one or more objects, select them and click "Copy" in the Edit menu or press "Ctrl + C" This will put the objects on the clipboard, but leave the original object alone.
### Duplicate
To duplicate a selection in place, select one or more objects and click "Duplicate" in the Edit menu or press "Ctrl + D".  This is an "in-place" copy and paste operation all in one, bypassing the clipboard.
This means if you already have something on the clipboard, it'll still be there after using Duplicate. The duplicate is placed directly on top of the original.
### Paste
To paste an object from the clipboard click "Paste" in the Edit menu or press "Ctrl - V". This will place a copy of the clipboard contents in the current file. Note that LightBurn can paste text or images copied to the clipboard from other software.
### Delete
To delete an object select it and click "Delete" in the Edit menu, or hit the Delete key.  This will remove the object from the current file.
### Convert to path
This converts a built-in "shape" object, like a rectangle, ellipse, or text, into lines and curves that can be edited. Click on "Convert to path" in the Edit menu. The original shape information is lost, so you won't be able to change text with the text tool after using this.
### Close path 
In order to "Scan" (Fill) a shape with your laser, the shape must be a closed loop, where the starting and ending point are the same.  If the start and end points are very close, but not quite connected, "Close Path" will move them together.  Click on "Close path" in the Edit menu or press "Alt + C"
### Auto join selected shapes
Looks at the start and end points of all the selected curves, and if any of them are close enough, connects them together into a single shape. Useful when importing DXF files, which don't contain connectivity information. Click on "Auto join selected shapes" in the Edit menu or press "Alt + J"
### Optimize Selected Shapes
Attempts to fit the selected shapes to arcs and lines within a specified error tolerance. Useful for reducing the point count in a shape, or recovering arcs from software that exports them as many small line segments.
### Delete Duplicates
This will delete duplicate items within the drawing, for example if two squares are identical and one on top of the other, this will delete the extra square. This helps to minimize erroneous moves and double-cuts.
### Select Open shapes
This will select all open shapes in the document.
### Select open shapes set to scan
This will select all the open shapes that are set to scan in the document.
### Select all shapes in current layer
This will select all the shapes that are set to cut in the current layer of the document. Note that if some of these shapes are grouped, the system may have to un-group them in order to select them.
### Settings
Clicking on "Settings" in the Edit menu will open a [Dialog box](Settings.md) where you can enter information about your laser and default application settings.
### Device Settings
After initial setup, you can access device settings by choosing "[Device Settings](DeviceSettings.md)".
### Debug drawing
This is mostly an internal tool for LightBurn developers that shows the bounds of shapes being drawn.
### Convert to cut
Also an internal tool for LightBurn developers - It converts the selected shapes into the cuts that would be sent to the laser, and makes a new shape from the result.
This is not how you produce gcode / cuts for your machine, it's just a debugging tool. Click on "Convert to cut" in the Edit menu or press "Ctrl + Shift + C"

[Return to top](#MenuCommands)

----------------------------------
<a name="ToolsMenu"></a>
## Tools Menu
Many of the tools in this menu are also available as icons in the tool toolbar that by default, is on the left side of the workspace.  See [Creating New Vectors](CreatingNewVectors.md) for more information.

### Select
Click on "Select" to select objects in the workspace, or to access menus and toolbars.
### Draw Lines
Click on "Draw Lines" or press "Ctrl + L" to draw straight lines in the workspace.
### Rectangle Tool
Click on "Rectangle" or press "Ctrl + R" to draw rectangles in the workspace.
### Ellipse Tool
Click on "Ellipse" or press "Ctrl + E" to draw ellipses in the workspace.
### Edit Nodes
Click on "Edit Nodes" or press "Ctrl + ~" to edit nodes of objects in the workspace.
### Edit Text
Click on "Edit Text" or press "Ctrl + T" to create or edit text in the workspace.
### Offset Shapes

Used to create new shapes that are offset from the current selection, inward or outward.

### Weld Shapes

Fuses multiple shapes together into a single outline.

### Trace Image

Opens a dialog box where you can trace the content of a bitmap image into vector graphics.  ([Read more here](TracingImages.md))

### Zoom In
Click on "Zoom In" or press "Ctrl + =" to zoom in the workspace.
### Zoom Out
Click on "Zoom In" or press "Ctrl + -" to zoom out in the workspace.
### Frame Selection

Zoom the view to completely contain the current selection.  (Ctrl + Shift + A)

### Position Laser
Click on "Position Laser" to allow clicking on the workspace to move the laser head to that location.
### Preview
Click on "Preview" or press "Alt + P" to open the preview window. It will show the current laser project and includes information on cut distance, rapid moves, and total time estimate. Cut lines are in black and traversal moves are red. You can toggle the display of traversal moves on or off, as well as shading by power level.

### Rotary
This will open the [rotary setup dialog](RotarySetup.md) box. Use this to set up your rotary attachment.

[Return to top](#MenuCommands)

----------------------------------
<a name="ArrangeMenu"></a>
## Arrange Menu
### Group
Click on "Group" or press "Ctrl + G" to group the selected objects in the workspace.
### Ungroup
Click on "Ungroup" or press "Ctrl + U" to ungroup the selected objects in the workspace.
### Flip Horizontal
Click on "Flip Horizontal" or press "Ctrl + Shift + H" to flip the selected objects in the workspace horizontaly.
### Flip Vertical
Click on "Flip Vertical" or press "Ctrl + Shift + V" to flip the selected objects in the workspace vertically.
### Align Left
Click on "Align Left" or press "Ctrl + Shift + Left arrow" to align the selected objects in the workspace to the left.
### Align Right
Click on "Align Right" or press "Ctrl + Shift + Right arrow" to align the selected objects in the workspace to the right.
### Align Top
Click on "Align Top" or press "Ctrl + Shift + Up arrow" to align the selected objects in the workspace to the top.
### Align Bottom
Click on "Align Bottom" or press "Ctrl + Shift + Down arrow" to align the selected objects in the workspace to the bottom.
### Align H-Center
Click on "Align H-Center" to align the selected objects in the workspace to the center of the horizontal plane.
### Align V-Center
Click on "Align V-Center" to align the selected objects in the workspace to the center of the vertical plane.
### Move to Page Center
Click on this to move selected objects to center of page
### Move to Upper Left
Click on this to move selected objects to Upper Left of page.
### Move to Upper Right
Click on this to move selected objects to Upper Right of page.
### Move to Lower Left
Click on this to move selected objects to Lower Left of page.
### Move to Lower Right
Click on this to move selected objects to Lower Right of page.
### Grid / Array
Click on "Grid / Array" to create an array or grid of objects in the workspace. A window will open allowing you to enter the parameters for the array or grid.
### Circular Array
Click on "Circular Array" to create an array or grid of objects in a circle in the workspace. A window will open allowing you to enter the parameters for the array.
### Push forward in draw order
Click on "Push forward in draw order" or use "Page up" key to move the selected object up one level in the draw order. Usefull when trying to see objects on the screen.
### Push backward in draw order
Click on "Push backward in draw order" or use "Page down" key to move the selected object down one level in the draw order. Usefull when trying to see objects on the screen.

[Return to top](#MenuCommands)

----------------------------------
<a name="WindowMenu"></a>
## Window Menu

### Reset to Default Layout
To arrange the windows and menus back to the original default layout, click on "Reset to Default Layout"
You can use the Window menu to toggle windows and menus on or off.

[Return to top](#MenuCommands)

---------------------------------

<a name="LanguageMenu"></a>
## Language Menu

Choose the language you would like to have LightBurn use in this menu.


[Return to top](#MenuCommands)

--------------------------------
<a name="HelpMenu"></a>
## Help Menu

### Quick Help and Notes
Click on "Quick Help and Notes" or press F1 to access hotkey list, general usage notes and version information.

### Online Documentation
Click on "Online Documentation to access the documentation for LightBurn.

### Online Video Tutorials
Click on "Online Video Tutorials" to access the tutorial videos.

### Check for Updates
Click on "Check for Upfates" to make sure you are on the most recent version.

### License Activation and Trial
Click on "License Activation and Trial" to launch the [license dialog](EnterLicense.md), where you can enter your license key, or see the status of your trial period or license.

### Enable Debug Log
This is for the developers, turn on the log by clicking on "Enable Debug Log".  The log file will be written to your "My Documents" folder on Windows, or Documents on Mac, and is cumulative - each time you enable the debug log it will append to any existing log, so it's a good idea to delete it after you're finished.

[Return to top](#MenuCommands)

