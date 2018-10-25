[Return to main page](README.md)

----

# Creating Vectors in LightBurn

LightBurn has a powerful set of tools for creating basic shapes directly in the workspace. These can be accessed via the Tools menu or via the Tools toolbar located along the left side of the default window.

## Basic shape creation

### Pen Tool ![Pen Tool Icon](/img/PenTool.PNG) 
[Video Tutorial #2: Pen Tool](https://www.youtube.com/watch?v=uzFsrUwONbw#t=6m26s)
* Lets you draw lines.
* Lines will automatically snap to existing vertices of objects as well as center points on shapes.
* Hold Ctrl (![Command icon](/img/key-command-16.png)on Mac) to bypass snapping behavior.

### Rectangle and Ellipse Tools ![Rectangle Tool Icon](img/RectangleTool.PNG) ![Ellipse Tool Icon](/img/EllipseTool.PNG)
[Video Tutorial #2: Rectangle and Ellipse](https://www.youtube.com/watch?v=uzFsrUwONbw#t=8m38s)
* Quickly draw rectangle or ellipse.
* Holding Shift locks the aspect to create squares or circles.
* Holding Ctrl (![Command icon](/img/key-command-16.png)on Mac) creates them from the center out.

#### Creating rounded corners on rectangles
You can create rounded corners on rectangles by selecting the shape and going to the Shape Properties tool window. In this window you can edit the base path properties including Width, Height and Corner Radius.

### Node Editing Tool ![Node Tool Icon](/img/NodeTool.PNG)
[Video Tutorial #2: Node Editing](https://www.youtube.com/watch?v=uzFsrUwONbw#t=9m15s)
* Allows you to move the vertices of a selected shape.
* Pressing the S key when hovering over a node will convert it to a smooth node, and if required, creates tangent handles that can be manipulated from it.
* Pressing S while hovering over a line will convert the line to a smooth curve, with tangent handles, but leaves the shape of the original line intact.
* Pressing L while hovering over a smooth curve will convert it back to a straight line.
* Pressing C while hovering over a node will convert it to a corner, allowing the two handles to be manipulated independently of each other.
* Pressing D when hovering over a node will delete it and connect the lines on either side together.
* Pressing D when hovering over a line will delete it and open or split the shape.
* Pressing I when hovering over a line or curve will insert a new node at that point along the line

### Text Tool ![Text Tool Icon](/img/TextTool.PNG)
[Video Tutorial #2: Text Tool](https://www.youtube.com/watch?v=uzFsrUwONbw#t=9m45s)

* Create text on the screen, or edit existing text by clicking within it.
* Quickly change font and size.
* Alignment (Left, Right, Top, Bottom, Center).

## Offset Tool ![Offset Tool Icon](/img/OffsetTool.PNG)

[Video Tutorial #2: Offset Tool](https://www.youtube.com/watch?v=uzFsrUwONbw#t=10m49s)

* Create an offset line around the selected objects.
* Can increase or decrease the offset distance, either outward or inward.
* Resulting shape is grouped automatically.
* You can ungroup and remove unwanted outline portions .
* Resulting shape can be auto-converted to splines.
* Can auto-delete the source shape(s) if desired.
* Pressing the Offset button with the Ctrl key pressed (![Command icon](/img/key-command-16.png)on Mac) executes with the last used options.


## Boolean Operations

Vector shapes can be modified using the [Boolean Tools](Boolean.md)
