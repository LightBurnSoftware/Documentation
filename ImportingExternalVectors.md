[Return to main page](README.md)

# Importing External Vectors

LightBurn supports the following external vector file formats
* .ai - Adobe Illustrator
* .pdf - Adobe Portable Document Format
* .dxf - Drawing Exchange Format
* .svg - Scalable Vector Graphics

These files can be added either by using the File -> Import option in the main menu, clicking the Import button ![Import Button](/img/ImportButton.PNG) on the toolbar, or dragging the file into the work area.

When using drag & drop to import a file, the content of the file is placed exactly at the mouse location when you release the button.  If using the menu item or import button, the file is placed in the center of the work area.  If you want the file to drop to the same location it exists in the source document, hold the Shift key when you import.

Please note that each of these file formats is incredibly complex, and it's not feasible to support every option available in the packages used to create them.


## Importing Files with Layers and Colors
When importing, LightBurn assigns a different cut layer to each unique color it encounters in the source file, either fill or stroke.  If a shape is assigned both fill and stroke colors, the stroke color takes precedence.

LightBurn currently does not match colors being imported to its internal palette, though this is planned for future development.

