
<a name="MenuCommands"></a>
# Menu Commands
### [Return to main page](README.md)
----------------------------------

### [File Menu](#FileMenu)
### [Edit Menu](#EditMenu)
### [Tools Menu](#ToolsMenu)
### [Arrange Menu](#ArrangeMenu)
### [Help Menu](#HelpMenu)


----------------------------------------------

<a name="FileMenu"></a>
## File Menu 
### [Return to top](#MenuCommands)

### New
Adding a new file
A new file can be added by clicking on “New” in the File menu
or press "ctrl + N"

### Open
Opening an existing file
To open a saved file. Click on “Open” in the File menu or
press "ctrl + O"

### Import
Importing media into working file
You can import any supported LightBurn files into the file you are
currently working on. Click on “Import” in the File menu
or press “ctrl – I” LightBurn supports importing the following file types:
svg, ai, pdf, jpg, bmp, dxf, dwg

### Save
To save a project click on “Save” in the File menu or press "ctrl – S" Type the name
you want the file saved as in the dialog box that opens up. To save a file
with changes, but still keep the original file intact, click on the “Save As”
icon in the File menu

### Export
To export a file to a different file format, click on “Export” in the
File menu. LightBurn supports the exporting of the following file types:
svg, ai, pdf, jpg, bmp, dxf, dwg

### Exit 
To exit the LightBurn software, click on the “Exit" in the File
menu or press “ctrl – Q” Any work not saved will be lost.

### [Return to top](#MenuCommands)
----------------------------------
<a name="EditMenu"></a>
## Edit Menu

### Undo
To undo the last editing action done on the current file, click on "Undo" in the Edit menu or press "ctrl + Z"
### Redo
To Redo the last editing action done on the current file, click on "Redo" in the Edit menu or press "shift + ctrl + Z"
### Select all
To select all objects in the current file click on "Select all" in the Edit menu or press "ctrl - A"
### Cut
To cut an object from the current file select it and click on "Cut" in the Edit menu or press "ctrl - X" This will put the object on the clipboard, removing it from the current file.
### Copy
To copy an object select it and click on "Copy" in the Edit menu or press "ctrl - C" This will put the object on the clipboard, but leaves the original object alone.
### Duplicate
To duplicate an object select it and click on "Duplicate" in the Edit menu or press "ctrl - D" This is an "in-place" copy and paste operation all in one, and bypasses the clipboard.
That means if you already have something on the clipboard, it'll still be there after using Duplicate, and the duplicate is placed directly on top of the original.
### Paste
To paste an object from the clipboard click on "Paste" in the Edit menu or press "ctrl - V" This will take the object from the clipboard and place it in the current file.
### Delete
To delete an object select it and click on "Delete" in the Edit menu.This will remove the object from the current file.
### Convert to path
This converts a "shape" object, like a rectangle, ellipse, or text, into lines and curves that can be edited. Click on "Convert to path" in the Edit menu. The original shape information is lost, so you won't be able to change text with the text tool after using this.
### Close path 
Click on "Close path" in the Edit menu or press "Alt + C"
### Auto join selected shapes
Looks at the start and end points of all the selected curves, and if any of them are close enough, connects them together into a single shape.
Useful when importing DXF files, which don't contain connectivity information. Click on "Auto join selected shapes" in the Edit menu or press "Alt + J"
### Settings
Clicking on "Settings" in the Edit menu will open a [Dialog box](Settings.md) where you can enter information about your laser and default application settings.
### Debug drawing
This is mostly an internal tool for LightBurn developers that shows the bounds of shapes being drawn.
### Convert to cut
Also an internal tool for LightBurn developers - It converts the selected shapes into the cuts that would be sent to the laser, and makes a new shape from the result.
This is not how you produce gcode / cuts for your machine, it's just a debugging tool. Click on "Convert to cut" in the Edit menu or press "Ctrl + Shift + C"
### [Return to top](#MenuCommands)
----------------------------------
<a name="ToolsMenu"></a>
## Tools Menu
### [Return to top](#MenuCommands)
----------------------------------
<a name="ArrangeMenu"></a>
## Arrange Menu
### [Return to top](#MenuCommands)
----------------------------------
<a name="HelpMenu"></a>
## Help Menu
