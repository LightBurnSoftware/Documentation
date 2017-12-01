[Return to main page](README.md)

**[Common Settings](#common) | [Cut](#cut) | [Scan](#scan) | [Scan+Cut](#scancut)**

----

# Laser Operations 

The basic operations of any device can be categorized in one of two ways. Cut and Scan. These two options combined with variations in power and speed can achieve a variety of results.

Settings will vary from machine to machine and acrosss different materials. It is recommended to test your settings on a scrap piece of the same material as your final work piece before your final run.

<a name="common"></a>

-----------------
## Common Settings
![Common Cut Settings](/img/CutSettingsCommon.PNG)

### Output
Output is a on/off selection. By default this setting is on for a layer. This means that the laser will output the contents of the layer. Turning this setting off will skip creating instructions for the layer and the layer will be ignored. This is useful for alignment lines or other content that should not be in the end product

### Air Assist
This is also an on/off selection. If your machine is capable of turning on or off air assist automatically, set this to on to enable your air assist or off to keep it off. If your air assist is always on or manually controled, this will have no affect.
<a name="speed"></a>
### Speed (mm/sec)
Speed is the feed rate when the laser is firing. This does not affect the feed rate for rapid move.

### Max Power
This is the maximum percentage of power that the laser will produce during the cut. 

### Min Power
This is the minimum percentage of power that the laser will produce during the cut. 

### Mode
This can be used to choose the opration for the layer. Cut, Scan and Scan+Cut

<a name="Cut"></a>

------------------
## Cut
Cut will trace the laser along the vector path. Depending on the power and feed rate settings, this can be used to cut through a material in single or multiple passes. Decreasing the power and/or increasing the speed can also allow you to simply mark the surface (engraving).

### Cut Settings

![Cut Mode Settings](/img/CutSettingsAdditional.PNG)

#### Enable "Cut-Through" Mode
This setting is used primarily for Ruida based machines. Enabling this setting will allow the laser to dwell in the same position after initially firing or before turning off based on the settings below.

* Start pause time (ms): Number of milliseconds to fire the laser before moving
* End pause time (ms): Number of milliseconds to fire the laser at the end of a move
* Power (%): Percentage of laser power while paused


#### Passes
* Number of Passes: The number of times the laser will trace the same path
* Z step per pass: Increase or decrease bed height for powered Z bed

<a name="scan"></a>

-------------------
## Scan
Scan will fill the interior of a vector simililar to engraving a raster image. When you select Scan from the Mode options, the settings below will become available.

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
Cross hatch is an on/off value. By default this is off wich means your laser will only burn in the direction you have chosen. By turning this setting on you will get a second operation that will burn lines in parallel to the first creating a cross-hatch as shown below.

### Cross-Hatch Off
![Cross-Hatch Off](/img/CrossHatch-Off.PNG)

### Cross-Hatch On
![Cross-Hatch.PNG](/img/CrossHatch.PNG)
<a name="overscanning"></a>
### Overscanning

When engraving, the head is scanning back and forth. Because we have to accelerate and decelerate the head at the beginning and end of each line this can cause darker edges than intended.

Overscanning allows the head move past the ends of each line before it starts to decelerate allowing the entirety of the engraving to happen at the desired head speed and then decelerating while the laser is not burning. 

<a name="lineinterval"></a>
### Line Interval (mm)
Line interval is the spacing between scan lines. The lower this value, the less space will be left between successive passes. Lowering this value can create a slight overlap causing the laser to slightly trace over the previous line. Setting a higher value will leave untouched material between passes leaving visible scan lines. This is roughly equivelant to stepover for a CNC.
<a name="scanangle"></a>
### Scan Angle
The default scan angle is 0. This will produce scan lines along the X path only. By introducing a scan angle, your laser head will track at the selected angle using both X and Y during operation. As you change this angle, the graphic will show you the expected result.

#### 0-degree scan angle
![0 Degree Scan Angle](/img/CrossHatch-Off.PNG)

#### 30-degree scan angle
![30 Degree Scan Angle](/img/Bi-Directional.PNG)

### Scan all shapes at once

### Scan shapes by group

### Scan shapes individually

<a name="scancut"></a>

--------------------
## Scan+Cut
Scan+Cut as the name suggests combines the scan and cut operations. In order of operations, the scan will happen first followed by the cut. This can be used to cut out a part once the scan is complete or simply provide an outline of the part before moving on to the next operation.

When you enable Scan+Cut you will get the additional settings below. See the [Cut](#cut) section for a description of each setting.

![Scan+Cut Settings](/img/CutAfterScanSettings.PNG)


