[Return to main page](README.md)

----

# Laser Operations 

The basic operations of any device can be categorized in one of two ways: Cut and Scan. These two options combined with variations in power and speed can achieve a variety of results.

Settings will vary from machine to machine and acrosss different materials. It is recommended to test your settings on a scrap piece of the same material as your final work piece before your final run.

* [Common Settings](#common) 
* [Cut](#cut)
* [Scan](#scan)
* [Scan+Cut](#scancut)


<a name="common"></a>

-----------------
## Common Settings
![Common Cut Settings](/img/CutSettingsCommon.PNG)

### Output
Output is an on/off selection. By default this setting is on for a layer. This means that the laser will output the contents of the layer. Turning this setting off will skip creating instructions for the layer and the layer will be ignored. This is useful for alignment lines or other content that should not be in the end product.

### Air Assist
This is also an on/off selection. If your machine is capable of turning air assist on or off automatically, set this to on to enable your air assist or off to keep it off. If your air assist is always on or manually controlled, this will have no effect.
<a name="speed"></a>
### Speed (mm/sec)
Speed is the feed rate when the laser is firing. This does not affect the feed rate for rapid move (IE moves traversing between cuts).

### Max Power
This is the maximum percentage of power that the laser will produce during the cut.

### Min Power
For DSP devices (not GCode based controllers) this is the minimum percentage of power that the laser will produce during the cut. On Ruida machines, this is power setting that will be used during a cut when the machine slows down to reverse direction, or make a sharp corner.  You should normally set this number to just above the threshold where your laser fires.  Setting it the same as Max Power means the laser will not change power output as the speed varies, which will result in a poorer quality cut, particularly on thinner materials.


******Please note:  Ruida controllers have a “Start Speed” value in the controller that is the point where they start ramping power from Min to max. Below that they just use min power. If you’re cutting slow, set min/max to the same value.*******

### Mode
This can be used to choose the operation for the layer. Cut, Scan, or Scan+Cut

<a name="Cut"></a>

------------------
## Cut
Cut will trace the laser along the vector path. Depending on the power and feed rate settings, this can be used to cut through a material in single or multiple passes. Decreasing the power and/or increasing the speed can also allow you to simply mark the surface (engraving).

### Cut Settings

![Cut Mode Settings](/img/CutSettingsAdditional.PNG)

#### Enable "Cut-Through" Mode
This setting is only available for Ruida based machines. Enabling this setting will allow the laser to dwell in the same position after initially firing or before turning off based on the settings below, and is useful for piercing thick materials before the cut starts.

* Start pause time (ms): Number of milliseconds to fire the laser before moving
* End pause time (ms): Number of milliseconds to fire the laser at the end of a move
* Power (%): Percentage of laser power while paused


#### Passes
* Kerf offset: Allows you to shift the cut inward or outward from a closed shape to compensate for the diameter of the beam. This is useful when making parts like inlays or finger joins.
* Z Offset: Specifies an amount to offset the laser head (or bed) for this cut. Useful for defocusing, or pushing the focus point into deep materials for cutting.
* Number of Passes: The number of times the laser will trace the same path
* Z step per pass: Increase or decrease bed height for powered Z bed

<a name="scan"></a>

-------------------
## Scan
Scan will fill the interior of a vector similar to engraving a raster image. When you select Scan from the Mode options, the settings below will become available.

![Scan Settings](/img/ScanSettingsAdditional.PNG)
<a name="bidirectional"></a>
### Bi-Directional scanning
This is an on/off value. By default this will be on which enables the laser to fire on both the out and return stroke. Turning this off will result in your laser only firing on the outward stroke. The graphic shown will represent the expected output of your laser.

#### Bi-Directional *ON*
![Bi-Directional Scan](/img/Bi-Directional.PNG)

#### Bi-Directional *OFF*
![Bi-Directional Scan Off](/img/Bi-Directional-Off.PNG)
<a name="crosshatch"></a>
### Cross-Hatch
Cross hatch is an on/off value. By default this is off which means your laser will only burn in the direction you have chosen. By turning this setting on you will get a second operation that will burn lines at 90 degrees to the first set, creating a cross-hatch pattern as shown below.  This is mostly useful at higher interval settings as a way to give the appearance of a filled shape, while taking less time.

### Cross-Hatch Off
![Cross-Hatch Off](/img/CrossHatch-Off.PNG)

### Cross-Hatch On
![Cross-Hatch.PNG](/img/CrossHatch.PNG)
<a name="overscanning"></a>
### Overscanning

When engraving, the head is scanning back and forth. Because the laser has to accelerate and decelerate the head at the beginning and end of each line, on machines with limited power control this can cause darker edges than expected.

Overscanning generates extra moves, past the ends of each line, switching the laser off before it fully stops, or even before it begins to decelerate, allowing the entirety of the engraving to happen at the desired head speed and then decelerating while the laser is not burning. The overscan number is a percentage of your cut speed - the default setting is 2.5%, meaning a cut at 100mm/sec will move an additional 2.5mm past the last cut with the laser off.

Note, Overscan is applied automatically by Ruida hardware. This setting is only available for gcode based controllers.

<a name="lineinterval"></a>
### Line Interval (mm)
Line interval is the spacing between scan lines. The lower this value, the less space will be left between successive passes. Lowering this value can create a slight overlap causing the laser to slightly trace over the previous line. Setting a higher value will leave untouched material between passes leaving visible scan lines. This is roughly equivalent to stepover for a CNC.
<a name="scanangle"></a>
### Scan Angle
The default scan angle is 0. This will produce scan lines along the X path only. By introducing a scan angle, your laser head will track at the selected angle using both X and Y during operation. As you change this angle, the graphic will show you the expected result.

#### 0-degree scan angle
![0 Degree Scan Angle](/img/CrossHatch-Off.PNG)

#### 30-degree scan angle
![30 Degree Scan Angle](/img/Bi-Directional.PNG)

On Ruida hardware, scan angles that are multiples of 90 degrees are supported natively by the hardware and will automatically overscan for you.  Other angles are scanned using standard cutting commands.

### Z-Offset, Number of Passes, and Z-Step per pass

These options behave identically to their counterparts in a standard cut.

### Scan all shapes at once

This setting tells the scanner to group all shapes within a cut layer together and scan them all at once. In most cases this is faster than scanning individually, if your laser is fast.

### Scan shapes individually

This will scan each distinct shape in your layer one at a time.  For users with slower moving lasers, this will occasionally be faster than scanning shapes together.  For example, if you have two filled shapes on opposite sides of your work area, filling one, then the other is probably faster than continually scanning back and forth across the work area.

### Flood Fill Scanning

This option is intended for use with slower machines where traversing is more time consuming than reversing direction. It will prefer direction changes over long traversals, and will save scanning time if the machine has a slow rapid speed, or quick acceleration. This *can* be used with image scans as well, but the cost to compute the path can be very high - use sparingly, and only with very simple image modes like threshold.

<a name="scancut"></a>

--------------------
## Scan+Cut
Scan+Cut, as the name suggests, combines the scan and cut operations. In order of operations, the scan will happen first followed by the cut. This can be used to cut out a part once the scan is complete or simply emphasize the outline of the part before moving on to the next operation.

When you enable Scan+Cut you will get the additional settings below. See the [Cut](#cut) section for a description of each setting.

![Scan+Cut Settings](/img/CutAfterScanSettings.PNG)




