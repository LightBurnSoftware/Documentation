[Return to main page](README.md)

----

# Troubleshooting

[Machine Connectivity](#connectivity)

[Workspace / UI](#workspace)

[GRBL Errors](#GrblErrors)

<a name="connectivity"></a>

------

## Machine Connectivity

### Reconnecting to a device

If you need to reset your device connection, from the Laser toolbox, right-click the *Devices* button. LightBurn does a full disconnect / reconnect cycle when you right-click the *Devices* button, or when you click Ok from the devices menu.

<a name="workspace"></a>

---------

##  Workspace / UI Issues

### Lost toolbar

A common question is "Where did my Toolbar or Tool Window go?"

A right click on any open area of a toolbar will bring up the options to turn on or off any toolbar or tool window. Click on the missing item to return it to your workspace.

![Toolbar Options](/img/Toolbars.PNG)


<a name="GrblErrors"></a>

---------

##  GRBL Errors and what they mean

| Error | Description |
| ----- | ---- |
| error:1  | G-code words consist of a letter and a value. Letter was not found. |
| error:2  | Numeric value format is not valid or missing an expected value. |
| error:3  | Grbl '\$' system command was not recognized or supported. |
| error:4  | Negative value received for an expected positive value. |
| error:5  | Homing cycle is not enabled via settings. |
| error:6  | Minimum step pulse time must be greater than 3usec |
| error:7  | EEPROM read failed. Reset and restored to default values. |
| error:8  | Grbl '\$' command cannot be used unless Grbl is IDLE. Ensures smooth operation during a job. |
| error:9  | G-code locked out during alarm or jog state. |
| error:10 | Soft limits cannot be enabled without homing also enabled. |
| error:11 | Max characters per line exceeded. Line was not processed and executed. |
| error:12 | (Compile Option) Grbl '$' setting value exceeds the maximum step rate supported. |
| error:13 | Safety door detected as opened and door state initiated. |
| error:14 | (Grbl-Mega Only) Build info or startup line exceeded EEPROM line length limit. |
| error:15 | Jog target exceeds machine travel. Command ignored. |
| error:16 | Jog command with no '=' or contains prohibited g-code. |
| error:20 | Unsupported or invalid g-code command found in block. |
| error:21 | More than one g-code command from same modal group found in block. |
| error:22 | Feed rate has not yet been set or is undefined. |
| error:23 | G-code command in block requires an integer value. |
| error:24 | Two G-code commands that both require the use of the XYZ axis words were detected in the block. |
| error:25 | A G-code word was repeated in the block. |
| error:26 | A G-code command implicitly or explicitly requires XYZ axis words in the block, but none were detected. |
| error:27 | N line number value is not within the valid range of 1 - 9,999,999. |
| error:28 | A G-code command was sent, but is missing some required P or L value words in the line. |
| error:29 | Grbl supports six work coordinate systems G54-G59. G59.1, G59.2, and G59.3 are not supported. |
| error:30 | The G53 G-code command requires either a G0 seek or G1 feed motion mode to be active. A different motion was active. |
| error:31 | There are unused axis words in the block and G80 motion mode cancel is active. |
| error:32 | A G2 or G3 arc was commanded but there are no XYZ axis words in the selected plane to trace the arc. |
| error:33 | The motion command has an invalid target. G2, G3, and G38.2 generates this error, if the arc is impossible to generate or if the probe target is the current position. |
| error:34 | A G2 or G3 arc, traced with the radius definition, had a mathematical error when computing the arc geometry. Try either breaking up the arc into semi-circles or quadrants, or redefine them with the arc offset definition. |
| error:35 | A G2 or G3 arc, traced with the offset definition, is missing the IJK offset word in the selected plane to trace the arc. |
| error:36 | There are unused, leftover G-code words that aren't used by any command in the block. |
| error:37 | The G43.1 dynamic tool length offset command cannot apply an offset to an axis other than its configured axis. T he Grbl default axis is the Z-axis. |
| error:38 | An invalid tool number sent to the parser |

| Alarm | Description |
| ----- | ---- |
| ALARM:1 | Hard limit triggered. Machine position is likely lost due to sudden and immediate halt. Re-homing is highly recommended. |
| ALARM:2 | G-code motion target exceeds machine travel. Machine position safely retained. Alarm may be unlocked. |
| ALARM:3 | Reset while in motion. Grbl cannot guarantee position. Lost steps are likely. Re-homing is highly recommended. |
| ALARM:4 | Probe fail. The probe is not in the expected initial state before starting probe cycle, where G38.2 and G38.3 is not triggered and G38.4 and G38.5 is triggered. |
| ALARM:5 | Probe fail. Probe did not contact the workpiece within the programmed travel for G38.2 and G38.4. |
| ALARM:6 | Homing fail. Reset during active homing cycle. |
| ALARM:7 | Homing fail. Safety door was opened during active homing cycle. |
| ALARM:8 | Homing fail. Cycle failed to clear limit switch when pulling off. Try increasing pull-off setting or check wiring. |
| ALARM:9 | Homing fail. Could not find limit switch within search distance. Defined as 1.5 * max_travel on search and 5 * pulloff on locate phases. |

| Message | Description |
| ----- | ---- |
| Hold:0 | Hold complete. Ready to resume. |
| Hold:1 | Hold in-progress. Reset will throw an alarm. |
| Door:0 | Door closed. Ready to resume. |
| Door:1 | Machine stopped. Door still ajar. Can't resume until closed. |
| Door:2 | Door opened. Hold (or parking retract) in-progress. Reset will throw an alarm. |
| Door:3 | Door closed and resuming. Restoring from park, if applicable. Reset will throw an alarm. |
