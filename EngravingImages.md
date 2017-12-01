# Engraving Raster Images

[Supported Image Files](#supported)

[Engraving Configuration](#configuration)

-----

![Engraving Image](img/EngravingImage.PNG)

LightBurn has the ability to engrave raster images (photo engrave) without additional effort.

<a name="supported"></a>
## Supported image files

* bmp (Bitmap)
* jpg and jpeg (Joint Photographic Exports Group)
* png (Portable Network Graphics) 
* gif (Graphics Interchange Format)
* tga (Truevision)

<a name="configuration"></a>
## Engraving Configuration

Double click on the cut layer in the Cuts tool window to launch the Cut Settings Editor window.

![Engraving Options](/img/EngravingOptions.PNG)

### Speed

See [Speed](/Operations.md#speed) under Operations

### Max Power

The maximum laser power for pure black. Setting this to a lower value will decrease the power of the laser when engraving absolute black. 

### Min Power

The minimum power of the laser for pure white. Increasing this value beyond your lasers firing threshold will allow the laser to fire for absolute white.

***TODO: Reword the next section***

*A note on Min/Max power:* This scale affects the entire range from white to black. If your image does not have absolute black or absolute white then it will not ever fire at the min/max settings. 

### Mode

Disabled for raster images

### Bi-Directional Scanning

See [Bi-Directional Scanning](/Operations.md#bidirectional) under Operations

### Negative Image

This will invert your image during engraving. Light becomes dark, dark becomes light.

### Overscanning

See [Overscanning](/Operations.md#overscanning) under Operations

### Line Interval

See [Line Interval](/Operations.md#lineinterval) under Operations

### Scan Angle

See [Scan Angle](/Operations.md#scanangle) under Operations

### DPI

Pixel density of the image to be engraved. This defaults to the DPI of the imported image.

### Image Mode

Changing the image mode will change the algorithm used to prepare the image for engraving

### Number of Passes

How many times to repeat the entire engraving process

