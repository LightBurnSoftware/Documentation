[Return to main page](README.md)
# Creating a Power Scale Test Grid

Create a 15x15mm square. Set its speed to your lowest speed to test and set power to whatever 100% on your laser is (i.e. if your max Power should be set to 70% so as not to overpower your tube (i.e. go above the recommended MAX milliamps) then set power to 70%).

Now, use the grid tool to create a row of as many power levels as you want to test - let's say 10 for this example.

Now, select the left most square and open the Shape Properties tab. Set the Power Scale to your lowest test power - 10% to mimic what you have above. Note that Power Scale applies to the layer power, so 10% is 10% of 70% (if that's what you set above).

Select each square and simply increase its Power Scale by your increment - 10% in this case.

That was the hard part! Now, select the entire row and use the Grid tool to create the number of rows you need for the Speeds.

Select each row and put it on a new layer. Simply set the layer's Speed to your next lowest speed setting and make sure Min and Max powers are what you set for the very first square.

LightBurn "remembers" the Power Scale for each square from the original row. So you only need to set the layer speed and power.

Note that this will give you a test matrix that has power along X and speed along Y.

