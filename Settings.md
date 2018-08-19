### [Return to main page](README.md)

This is the main LightBurn settings page.

![Settings Dialog Box](/img/Settings.png)



There are a few different sections here, all related to different settings:

- [Display / Graphics](#Display_Graphics)
- [Units / Grid](#Grid_Units)
- [DXF Import Settings](#DXF_Import_Settings)
- [Shape Move Increments](#Shape_Move_Increments)
- [Output Settings](#Output_Settings)

<a name="Display_Graphics"></a>

## Display / Graphics

These settings affect only the visual display quality of LightBurn - changing these does not affect the generated output to your machine.

##### Curve Quality

This controls the level of precision that LightBurn outputs splines. If you look closely at the comparison below, you can see the right image is made of straight lines, about 1/8" (4mm) long. The left image is also made of line segments, just many more of them, so the effect is imperceptible. This extra quality comes with a slight cost in speed. You'll only likely notice it in files with thousands of curved shapes.

![Curves-High-vs-Low](img/Curves-High-vs-Low.png)

##### Anti-aliasing

Aliasing is commonly called "jaggies" - in our case, it's the visible appearance of pixels when drawing 2d shapes. Anti-aliasing draws shaded pixels on either side of the drawn lines to give the appearance of higher resolution and a smoother result. The image below compares the two - The difference is very apparent, however this comes with a moderate performance penalty. If you are running an older machine, turning off antialiasing may improve the interactivity of LightBurn on dense scenes.

![Antialiasing-vs-Normal](/img/Antialiasing-vs-Normal.png)

##### Invert mouse wheel zoom direction

I'm a PC guy, with a Mac, and the scroll wheel always feels backwards to me, so this switch changes the direction you scroll when zooming. If you're a Mac person stuck on a PC, this is also for you.

##### Use System Clipboard

Enabling this makes copy and paste operations slightly slower, but allows LightBurn to:

- Copy and paste across different runs of LightBurn, or between two running copies of the app
- Paste images copied from other software or web browsers
- Paste text directly into the edit window, auto-creating a text object for you

<a name="Grid_Units"></a>

## Units & Grid

##### Inches / mm

LightBurn internally operates in millimeters, but can display in either millimeters or inches. Speeds can be represented as either units per second or units per minute. Users with diode lasers will likely prefer the units per minute setting, whereas CO2 lasers generally express speeds using units per second.

##### Visual Grid Spacing

The visual grid is set to 10mm by default. Note that this is independent of the Grid Snap setting below.

##### Grid Snap Distance

Positioning of lines and other primitives will snap to the Grid Snap distance unless overridden using the Ctrl key. The default for this is 1mm.

##### Click Selection Tolerance

This is how close you have to be to a line or vertex, in screen pixels, to click it.  Increase this number if you have trouble selecting things, decrease it if you find yourself selecting things you didn't mean to.

##### Object Snap Distance

Controls how close, in screen pixels, your cursor has to be to an object vertex or center to engage the object snapping behavior.

##### Snap to Objects / Snap to Grid

LightBurn has two snapping behaviors which can be enabled / disabled here. Snap to Objects will snap your pointer location to the nearest object center or vertex when creating new objects, or drawing lines, making it easier to connect and align shapes.  Snap to Grid will snap your cursor position to the nearest grid location, as specified by the Grid Snap value.  Note that the Grid Snap and the Visual Grid do not have to be the same.

##### <a name="DXF_Import_Settings"></a>

## DXF Import Settings

##### Units

DXF files do not store the measurement system that was used to create them. If you create an object that is 5 inches wide, it might import as 5mm wide, because LightBurn can only see the '5'. Similarly, if your object was created in microns, it might import huge. Set this value as appropriate before importing DXF files to ensure correct scaling.

##### Auto Close Tolerance

DXF files are often saved as a collection of discrete pieces, instead of continuous paths. The Auto-Close Tolerance value tells LightBurn to connect any lines or curves that are on the same layer and closer together than this value.

<a name="Shape_Move_Increments"></a>

## Shape Move Increments

When moving objects with the cursor keys in the edit window, these values control the distance to move the selection, when using the arrow keys by themselves or with the Control or Shift modifiers.

<a name="Output_Settings"></a>

## Output Settings

These two settings affect the output sent to the laser.

##### Job Origin

This setting controls where LightBurn assumes your laser position to be relative to the graphics in your project when using a "Start From" value of "Current Position" or "User Origin".  This is explained in more detail in the [Coordinates and Origin](Coordinates_and_Origin.md) settings page.

##### Curve Tolerance

This setting is similar to the Curve Quality setting above, except that it controls the quality of output to the laser. The number is a measure of how much error to allow in the output.  A value of 0 would be "perfect", but would create very dense data, as some lasers can only process line segments.

![OutputTolerance](./img/OutputTolerance.png)

In the above image, the blue curve between the two points is the ideal shape. The black line is a straight line between them, and the red line shows the error (how far the line is from the curve). LightBurn measures this error, and if it's equal to or lower than the Curve Tolerance value, it outputs the straight line. If not, the curve is subdivided into two linear segments and the process repeats with each new segment. Those segments are shown below in violet, along with their new error values.  You can see that the two new lines do a much better job of approximating the original curve.

![OutputTolerance-SubDiv](./img/OutputTolerance-SubDiv.png)

Most people will probably never need to change this - the default is 0.05mm, which is about 1/2 the width of a typical beam.  Note that this is the *maximum* error value allowed, so typical output will be better than this, and this only affects curves, not straight lines or vertices, which are exact.