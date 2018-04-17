# Troubleshooting

[Machine Connectivity](#connectivity)

[Workspace / UI](#workspace)

[GRBL Errors](#GrblErrors)

<a name="connectivity"></a>

------

## Machine Connectivity

### Reconnecting to a device

If you need to reset your device connection, from the Laser toolbox click the *Devices* button to open the devices menu, then hit ok. LightBurn does a full disconnect / reconnect cycle when you click ok in the devices menu

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

 "error:1"  : _("G-code words consist of a letter and a value. Letter was not found.")
 
 "error:2"  : _("Numeric value format is not valid or missing an expected value.")
 
 "error:3"  : _("Grbl '$' system command was not recognized or supported.")
 
 "error:4"  : _("Negative value received for an expected positive value.")
 
 "error:5"  : _("Homing cycle is not enabled via settings.")
 
 "error:6"  : _("Minimum step pulse time must be greater than 3usec")
 
 "error:7"  : _("EEPROM read failed. Reset and restored to default values.")
 
 "error:8"  : _("Grbl '$' command cannot be used unless Grbl is IDLE. Ensures smooth operation during a job.")
 
 "error:9"  : _("G-code locked out during alarm or jog state")
 
 "error:10" : _("Soft limits cannot be enabled without homing also enabled.")
 
 "error:11" : _("Max characters per line exceeded. Line was not processed and executed.")
 
 "error:12" : _("(Compile Option) Grbl '$' setting value exceeds the maximum step rate supported."),
 
 "error:13" : _("Safety door detected as opened and door state initiated."),
 
 "error:14" : _("(Grbl-Mega Only) Build info or startup line exceeded EEPROM line length limit."),
 
 "error:15" : _("Jog target exceeds machine travel. Command ignored."),
 
 "error:16" : _("Jog command with no '=' or contains prohibited g-code."),
 
 "error:20" : _("Unsupported or invalid g-code command found in block."),
 
 "error:21" : _("More than one g-code command from same modal group found in block."),
 
 "error:22" : _("Feed rate has not yet been set or is undefined."),
 
 "error:23" : _("G-code command in block requires an integer value."),
 
 "error:24" : _("Two G-code commands that both require the use of the XYZ axis words were detected in the block."),
 
 "error:25" : _("A G-code word was repeated in the block."),
 
 "error:26" : _("A G-code command implicitly or explicitly requires XYZ axis words in the block, but none were detected."),
 
 "error:27" : _("N line number value is not within the valid range of 1 - 9,999,999."),
 
 "error:28" : _("A G-code command was sent, but is missing some required P or L value words in the line."),
 
 "error:29" : _("Grbl supports six work coordinate systems G54-G59. G59.1, G59.2, and G59.3 are not supported."),
 
 "error:30" : _("The G53 G-code command requires either a G0 seek or G1 feed motion mode to be active. A different motion was a
 ctive."),
 
 "error:31" : _("There are unused axis words in the block and G80 motion mode cancel is active."),
 
 "error:32" : _("A G2 or G3 arc was commanded but there are no XYZ axis words in the selected plane to trace the arc."),
 
 "error:33" : _("The motion command has an invalid target. G2, G3, and G38.2 generates this error, if the arc is impossible to g
 enerate or if the probe target is the current position."),
 
 "error:34" : _("A G2 or G3 arc, traced with the radius definition, had a mathematical error when computing the arc geometry. T
 ry either breaking up the arc into semi-circles or quadrants, or redefine them with the arc offset definition."),
 
 "error:35" : _("A G2 or G3 arc, traced with the offset definition, is missing the IJK offset word in the selected plane to t
 race the arc."),
 
 "error:36" : _("There are unused, leftover G-code words that aren't used by any command in the block."),
 
 "error:37" : _("The G43.1 dynamic tool length offset command cannot apply an offset to an axis other than its configured axis. T he Grbl default axis is the Z-axis."),
 
 "error:38" : _("An invalid tool number sent to the parser"),

 "ALARM:1" : _("Hard limit triggered. Machine position is likely lost due to sudden and immediate halt. Re-homing is highly recommended."),
 
 "ALARM:2" : _("G-code motion target exceeds machine travel. Machine position safely retained. Alarm may be unlocked."),
 
 "ALARM:3" : _("Reset while in motion. Grbl cannot guarantee position. Lost steps are likely. Re-homing is highly recommended."),
 
 "ALARM:4" : _("Probe fail. The probe is not in the expected initial state before starting probe cycle, where G38.2 and G38.3 is not triggered and G38.4 and G38.5 is triggered."),
 
 "ALARM:5" : _("Probe fail. Probe did not contact the workpiece within the programmed travel for G38.2 and G38.4."),
 
 "ALARM:6" : _("Homing fail. Reset during active homing cycle."),
 
 "ALARM:7" : _("Homing fail. Safety door was opened during active homing cycle."),
 
 "ALARM:8" : _("Homing fail. Cycle failed to clear limit switch when pulling off. Try increasing pull-off setting or check wiring."),
 
 "ALARM:9" : _("Homing fail. Could not find limit switch within search distance. Defined as 1.5 * max_travel on search and 5 * pulloff on locate phases."),

 "Hold:0" : _("Hold complete. Ready to resume."),
 
 "Hold:1" : _("Hold in-progress. Reset will throw an alarm."),
 
 "Door:0" : _("Door closed. Ready to resume."),
 
 "Door:1" : _("Machine stopped. Door still ajar. Can't resume until closed."),
 
 "Door:2" : _("Door opened. Hold (or parking retract) in-progress. Reset will throw an alarm."),
 
 "Door:3" : _("Door closed and resuming. Restoring from park, if applicable. Reset will throw an alarm."),

