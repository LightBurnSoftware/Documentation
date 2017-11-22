[Return to main page](README.md)

# Laser Operations 

The basic operations of any device can be categorized in one of two ways. Cut and Scan. These two options combined with variations in power and speed can achieve a variety of results.

Settings will vary from machine to machine and acrosss different materials. It is recommended to test your settings on a scrap piece of the same material as your final work piece before your final run.

![Common Cut Settings](/img/CutSettingsCommon.PNG)

## Common Settings

### Output
Output is a on/off selection. By default this setting is on for a layer. This means that the laser will output the contents of the layer. Turning this setting off will skip creating instructions for the layer and the layer will be ignored. This is useful for alignment lines or other content that should not be in the end product

### Air Assist
This is also an on/off selection. If your machine is capable of turning on or off air assist automatically, set this to on to enable your air assist or off to keep it off.

### Speed (mm/sec)
Speed is the feed rate when the laser is firing. This does not affect the feed rate for rapid move.

### Max Power
This is the maximum percentage of power that the laser will produce during the cut. 

### Min Power
This is the minimum percentage of power that the laser will produce during the cut. 

### Mode
This can be used to choose the opration for the layer. Cut, Scan and Scan+Cut

### Cut
Cut will trace the laser along the vector path. Depending on the power and feed rate settings, this can be used to cut through a material in single or multiple passes. Decreasing the power and/or increasing the speed can also allow you to engrave rather than cut. 

#### Additional Cut Settings

![Cut Mode Settings](/img/CutSettingsAdditional.PNG)

##### Enable "Cut-Through" Mode
This setting is used primarily for Ruida based machines. Enabling this setting will allow the laser to dwell in the same position after initially firing or before turning off based on the settings below.

* Start pause time (ms): Number of milliseconds to fire the laser before moving
* End pause time (ms): Number of milliseconds to fire the laser at the end of a move
* Power (%): Percentage of laser power while paused


##### Passes
* Number of Passes: The number of times the laser will trace the same path
* Z step per pass: Increase or decrease bed height for powered Z bed

## Scan

## Scan+Cut
