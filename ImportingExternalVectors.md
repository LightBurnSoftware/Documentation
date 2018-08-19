[Return to main page](README.md)

----

# Importing External Vectors

LightBurn supports the following external vector file formats
* .ai - Adobe Illustrator
* .pdf - Adobe Portable Document Format
* .dxf - Drawing Exchange Format
* .svg - Scalable Vector Graphics
* .hpgl / .plt - Plotter vector graphics

These files can be added either by using the File -> Import option in the main menu, clicking the Import button ![Import Button](/img/ImportButton.PNG) on the toolbar, or dragging the file into the work area.

When using drag & drop to import a file, the content of the file is placed exactly at the mouse location when you release the button.  If using the menu item or import button, the file is placed in the center of the work area.  If you want the file to drop to the same location it exists in the source document, hold the Shift key when you import.

Please note that each of these file formats is incredibly complex, and it's not feasible to support every option available in the packages used to create them.

Also note that embedded images are currently only supported in SVG files, though support is in progress for AI / PDF formats.  Text objects are also not imported, and will need to be converted to paths / curves in the source art package for importing into LightBurn.


## Importing Files with Layers and Colors
When importing, LightBurn assigns a different cut layer to each unique color it encounters in the source file, either fill or stroke.  If a shape is assigned both fill and stroke colors, the stroke color takes precedence.

LightBurn will attempt to match colors being imported to its internal palette. Any matching colors will be assigned first, and any unmatched colors will be assigned in order to the remaining colors in the palette.

