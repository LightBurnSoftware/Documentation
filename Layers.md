[Return to main page](README.md)

----

# Layers

LightBurn offers layering capability to allow different actions and settings for the various drawings or images of your job.

Layers are controlled by the color palette at the bottom of the LightBurn workspace.

![Layers Palette](/img/LayersPalette.PNG)



### Assigning layers manually

To use the layers palette, select an item in your workspace such as a shape or image and then select a color from the palette at the bottom of the screen. This color will now be assigned to a new layer that you will see in the cuts toolbox. Any item you assign to the same color will be placed in the same layer.

As seen in the image below, each shape and image is color coded to a different layer and each layer is capable of having a different set of instructions for your laser. 

![Layers Example](/img/LayersExample.PNG)



### Assigning layers automatically

LightBurn will look at your current drawing to identify colors and attempt to match them to a color in the layer palette. If an exact match is available it will assign it. Otherwise it will assign unmatched colors to the next available color in the palette.



### Layer options

You can adjust the order of operations across layers by changing the priority value in the cut info section below the list of layers. Moving a layer to 0 will make it the first layer to be acted on by your laser and it will proceed in order down the list. This is a powerful tool to control which parts of your job are completed first and which are last such as engrave and then cut.

As a drawing gets more complex it can become difficult to determine what is on a given layer. If you right click the layer in the cuts toolbox it will cause the items associated with that layer to flash on the screen. 

Also layers can be set to output or not by checking the Output checkbox. Turning this off will prevent the layer from being sent to your laser but will be recognized for current position or user job origination settings. Using this would allow you to place a representation of your work piece as a guide for alignment and setup while not actually burning. 

You can also hide a layer. This will turn the visibility on the screen on and off and can be helpful when working with complex drawings.



### Layer memory

Layer palette colors will retain a memory of the last setting used. If your last job used black for trace, red for scan and blue for cut with specific power and speed settings, LightBurn will remember that the next time you assign those colors to a layer. 