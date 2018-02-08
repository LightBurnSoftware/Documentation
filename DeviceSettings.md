[Return to main page](README.md)
# Device Settings

After initial setup, you can access device settings under the Edit > Device Settings menu.



![Device Settings Window](/img/DeviceSettings.PNG)

<a name="WorkingSize">

### Working Size

This is the working size of your laser bed. Set this to the maximum X and Y travel for your laser. 

<a name="origin">

### Origin

This is the origin or 0,0 location for your laser. 

<a name="ScanningOffset">

### Scanning Offset Adjust

Scanning offset is useful when doing raster or vector scanning at high enough speeds that belt flex puts your laser head a little behind where it should be when it fires. (see the comparison below of RDWorks with the feature enabled vs LightBurn before it was available). You run several scans at different speeds, measure the distance between your horizontal scans on odd / even rows, and enter those measurements into the table. A minimum of two measurements are needed for it to work. Others are interpolated from those, but you can enter as many as you like.

![Scanning Offset Calibration](/img/ScanningOffsetCalibration.jpg)

<a name="FastWhitespace">

### Fast Whitespace Scan

When engraving an image, LightBurn normally moves at the same speed across the entire image. If you are engraving slowly to get a good burn, but the image contains a lot of empty space (white space), this takes a long time. With the Fast Whitespace switch enabled, LightBurn will boost the speed through blank areas to the speed you indicate, if it is faster than the current engraving speed. This can save significant time.

<a name="zaxis">

### Z Axis Controls