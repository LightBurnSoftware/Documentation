[Return to main page](README.md)

----

# Rotary Attachment Setup

### This will walk you through setting up and using your rotary attachment

Click on the Tools menu, Rotary Setup link and it will open the rotary setup dialog box.

![Rotary Setup Window](/img/rotary.png)

1. If using a Ruida controller, disconnect the Y axis stepper connection and connect the rotary attachment to the Y axis. If using Smoothie or Grbl, C3D, or Smoothieware controllers, click the "A" axis selection.  (See below on how to configure your controller steps before you proceed)
2. Choose whether you have a chuck style or roller attachment.
3. Tick the enable rotary check box.
4. In the steps per revolution box, enter the number of steps it takes your attachment to make one full revolution.
5. Enter either the diameter of the object to be engraved or it's circumference, the other value will be automatically calculated.
6. Align your object under the laser head in a position where the X axis will start and rotate the object in the rotary attachment to the point where you want the Y axis to start engraving.
7. When using the rotary, it's generally a good idea to use "current position" as the "Start From" setting.
8. Click start and watch the magic happen.
9. ***Remember to uncheck the use rotary attachment check box once you are finished*** so that you do not mess up your next regular project.

Some general notes on using a rotary attachment:

If the object slips on the rollers of a roller type attachment, wrap the rollers with some sort of non-slip material or even rubber bands.

You can also try placing some weights inside the object such as ball bearings or other small round objects, this will help press the object against the rollers.



#### Notes for C3D, Smoothieware or GRBL users:

Before configuring the above, you will likely need to set up the rotary axis on your controller.  LightBurn sends rotary moves as angle values, and the GCode controller translates those angles into actual movements. To do this, it needs to know the correct number of motor steps to take for one degree of movement on the rotary motor.

If you have a Cohesion3D, Smoothieboard, or other common GCode based controller, the number is usually 200 times your microstepping multiplier (usually 8 or 16) times any gear reduction, divided by 360.

For a Cohesion3D or HolgaMods rotary, this is usually

3200 steps (200 x 8 micro steps x 2x reduction) / 360 = 8.88888888 steps per degree
6400 steps (400 x 8 micro steps x 2x reduction) / 360 = 17.7777778 steps per degree

The steps per degree number, along with acceleration and maximum speed will need to be set in the appropriate location for the controller.  With Smoothieware, it would be the 'delta' settings in the config.txt file on the controller.  For GRBL, it can be accessed in Edit > Machine Settings in LightBurn, under vendor settings for the A Axis.

