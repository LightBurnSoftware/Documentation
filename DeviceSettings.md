[Return to main page](README.md)

----

# Device Settings

After initial setup, you can access device settings under the Edit > Device Settings menu.



![Device Settings Window](/img/DeviceSettings.PNG)

<a name="WorkingSize">

### Working Size

This is the working size of your laser bed. Set this to the maximum X and Y travel for your laser. 

<a name="origin">

### Origin

This is the origin or 0,0 location for your laser. If you have a GCode based system, this is almost always at the front left, regardless of the location of your limit switches.  If you have a DSP laser, like Ruida or Trocen, the origin is usually where the limit switches are placed.

<a name="ScanningOffset">

### Scanning Offset Adjust

Scanning offset is useful when doing raster or vector scanning at high enough speeds that delays in your power supply cause the firing point to be a little behind where it should be. See the help for [Scanning Offset Adjustment here](ScanningOffsetAdjustment.md).

<a name="FastWhitespace">

### Fast Whitespace Scan

When engraving an image, LightBurn normally moves at the same speed across the entire image. If you are engraving slowly to get a good burn, but the image contains a lot of empty space (white space), this takes a long time. With the Fast Whitespace switch enabled, LightBurn will boost the speed through blank areas to the speed you indicate, if it is faster than the current engraving speed. This can save significant time.

**A note for Marlin users:** Since Marlin treats G0 and G1 moves identically, this value is used to specify the speed for rapid moves. If you do not set this value, LightBurn will use the same speed as the G1 moves.

<a name="SValueMax">

### S-Value Max

GRBL and Smoothieware use the S-Value (spindle speed setting) to control the PWM power output to the laser.  This setting is the number that corresponds to 100% power in LightBurn.  Smoothieware typically uses a value from 0 to 1 and supports fractional numbers in between.  GRBL defaults to 0 to 1000 for newer versions of GRBL, or 0 to 255 for older ones.  The S-Value Max setting in LightBurn must match your controller setting, or you'll either get not enough power output (if LightBurn's setting is lower) or very small power numbers will set your laser to full power (if LightBurn's setting is higher).



<a name="zaxis">

### Z Axis Controls

**Enable Z Axis:** turn this on to allow LightBurn to control the Z axis of your machine, IE the height of the laser above the workpiece.

**Note:** enabling Z control means that LightBurn will **always** emit Z values for a running job, and therefore requires that you set *either* the "Relative Z moves only" toggle below, *or* a material height value on the main cut panel.  *If you to not set relative mode, and do not set a material height, the default of 0 may cause LightBurn to raise your bed to a point where the workpiece could contact the head of your laser.*

**Reverse Z Direction:** Most DSP systems have 0 as the highest point, with positive numbers moving the laser head further from the bed, however some systems reverse this.  Toggle this switch to change the overall direction for Z moves.

**Relative Z moves only:** This setting tells LightBurn to read the height of the machine when the job starts, and uses that height as the starting point for all Z moves, ignoring any specified material height. This is the simplest way to work, as you just set your focus manually, and LightBurn will perform all moves relative to whatever height your machine is at when the job starts.  **Note:** for DSP systems this requires that you are connected to the machine.