

# Menu Commands

## File Menu

### New
Adding a new file
A new file can be added by clicking on the “New” icon in the File menu
or by pressing ctrl + N

### Open
Opening an existing file
To open a saved file. Click on the “Open” icon in the File menu or
press ctrl + O

### Import
Importing media into working file
You can import any supported LightBurn files into the file you are
currently working on. Click on the “Import” icon in the File menu
or press “ctrl – I” LightBurn supports importing the following file types:
svg, ai, pdf, jpg, bmp, dxf, dwg

### Save
To save a project click on the “Save” icon or press”ctrl – S) Type the name
you want the file saved as in the dialog box that opens up. To save a file
with changes, but still keep the original file intact, click on the “Save As”
icon in the File menu

### Export
To export a file to a different file format, click on the “Export” icon in the
File menu. LightBurn supports the exporting of the following file types:
svg, ai, pdf, jpg, bmp, dxf, dwg

### Exit 
To exit the LightBurn software, click on the “Exit Icon in the File
menu or press “ctrl – Q” Any work not saved will be lost.


## Edit Menu

### Undo
To undo the last editing action done on the current file, click on the "Undo" icon in the edit menu (or click ctrl + Z)
### Redo
To Redo the last editing action done on the current file, click on the "Redo" icon in the edit menu (or click  Shift + ctrl + Z)
### Select all
To select all objects in the current file click on the "Select all" icon in the edit menu (or click ctrl - A)
### Cut
To cut an object from the current file select it and click on the "Cut" icon in the edit menu (or click ctrl - X) This will put the object on the clipboard, removing it from the current file.
### Copy
To copy an object select it and click on the "Copy" icon in the edit menu (or click ctrl - C) This will put the object on the clipboard, but leaves the original object alone.
### Duplicate
To duplicate an object select it and click on the "Duplicate" icon in the edit menu (or click ctrl - D) This is an "in-place" copy and paste operation all in one, and bypasses the clipboard.
That means if you already have something on the clipboard, it'll still be there after using Duplicate, and the duplicate is placed directly on top of the original.
### Paste
To paste an object from the clipboard click on the "Paste" icon in the edit menu (or click ctrl - V) This will take the object from the clipboard and place it in the current file.
### Delete
To delete an object select it and click on the "Delete" icon in the edit menu.This will remove the object from the current file.
### Convert to path
This converts a "shape" object, like a rectangle, ellipse, or text, into lines and curves that can be edited. The original shape information is lost, so you won't be able to change text with the text tool after using this.
### Close path 
Click on the "Close path" icon (or click Alt + C)

### Auto join selected shapes
Looks at the start and end points of all the selected curves, and if any of them are close enough, connects them together into a single shape.
Useful when importing DXF files, which don't contain connectivity information. Click on the "Auto join selected shapes" icon ( or click Alt + J)
### Settings
Clicking on the "Settings" icon will open a [Dialog box](Settings.md) where you can enter information about your laser and default application settings.

### Debug drawing
This is mostly an internal tool for LightBurn developers that shows the bounds of shapes being drawn.
### Convert to cut
Also an internal tool for LightBurn developers - It converts the selected shapes into the cuts that would be sent to the laser, and makes a new shape from the result.
This is not how you produce gcode / cuts for your machine, it's just a debugging tool. Click on the "Convert to cut" icon (or click Ctrl + Shift + C)
## Tools Menu

## Arrange Menu

## Help Menu
