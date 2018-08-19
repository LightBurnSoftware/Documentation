[Return to main page](README.md)

----

# Using a camera with LightBurn

LightBurn includes a camera feature which allows a USB connected camera to be used in a couple of different ways:

- Monitoring your laser
- Positioning designs on material
- Tracing artwork directly from the bed of the laser



Using the camera as a monitor is simple - enable the Camera Control window (right-click on any window or toolbar and choose "Camera Control" from the pop-up).

You'll be presented with a window that looks like this:

![](/img/Camera/CameraControl.png)

If your system has a compatible USB camera connected, it will appear in the Camera drop-down box. Select the camera, and the view from the camera will appear in the window, as shown:

![](/img/Camera/CameraControl-Monitor.png)



The image from this camera is very distorted, because it is uses a fish-eye lens to achieve a very wide field of view, and it's mounted at an odd angle for use with the laser. LightBurn can counter both of these, and simulate a top-down view from nearly any camera. It takes a bit of effort to set up, but it's well worth it.

# Camera Calibration

In order to use the camera for work placement, it's necessary to "teach" LightBurn how to remove the distortion from your camera lens, and where your camera is in relation to the work area of your laser. The first part of this is accomplished in the Lens Calibration wizard.

You'll need to download and print the following image:

[Calibration-Circles.png](./img/Camera/Calibration-Circles.png)

The circles image will be approximately 148mm x 105mm (5.8" x 4.1"), and should have at least 6mm (1/4") of white space around the pattern.

Mount it to stiff card, foam-board, or wood, so the image remains very, very flat. If the image is curved, it will affect the calibration process and reduce the accuracy.

### The Camera Lens Calibration wizard

Camera Lens Calibration uses series of captured images of a known pattern. The software analyzes how the pattern appears in the images, and compares that against its internal knowledge of how the pattern should look. It determines the amount and shape of distortion produced by the lens of the camera, and computes an inversion for this distortion.

**Note:** This process is dependent **only** on the camera and lens, not on its placement in your machine - as long as the camera and calibration pattern are perfectly still, you do not need to mount the camera in the machine to perform the lens calibration. If the calibration image cannot be held at the appropriate distance to match the shown image in the display, you may shrink or enlarge the printed pattern.

It is best to have good, consistent lighting for the capture process, and the camera should be in focus. A fuzzy image, or shadows falling across the calibration pattern will make the process much harder, if not impossible.

Open the "Tools" menu and choose "Calibrate Camera Lens" from the menu.  You will be presented with a screen like the one below.

![](/img/Camera/CalibrateCameraLens.png)

Choose your camera in the list, and you'll see the view from the camera in the area to the left. With the correct camera selected, click Next.

The view will change to include a capture button, and a helper image to show you how to position the printed pattern for capture. For the first capture, place the pattern in the center of the field of view of the camera, with the printed face of the card pointed directly at the camera, as shown in the small view up top. If you cannot easily match your capture image with the suggested image, you may need to adjust the scale of your printed card, or leave the camera out of the machine for lens calibration.

![](/img/Camera/Calibration-Step1.png)



Click the Capture button (highlighted above) and you should see something like this:  (note that we've removed the camera from the machine for this one)

![](/img/Camera/Calibration-Step2.png)

Above the image on the right you see:

​	Image 1 (1600 x 1200) : Pattern found - Score: 0.09 - Great! Click Next

This tells you:

- The image was successfully captured
- The resolution of the captured image is 1600 x 1200 (higher is better)
- The calibration pattern was found in this image
- This image scored very well - Lower scores are better. In this image, after distortion removal, the positions of the dots in the image align with the positions of the real dots with an average error of only 0.09 pixels - That's very good, and well within our desired score of 0.3 pixels of error.

Notice that in the gray image that appears to the right, the pattern of circles is not distorted, though the image around them is considerably worse (look just above the dots). That is temporary, and the result of only having a single calibration image to work with. As you progress through the remaining calibration steps, you'll capture more images with the pattern in different parts of the camera view, filling in more information about how your lens distortion affects the image.

If the calibration pattern is not found, LightBurn will tell you so. Make sure the pattern card faces directly toward the camera, and occupies roughly the same amount of view area shown in the "suggestion" image.  The pattern card should be "aligned" with the sensor of the camera, as shown in the upper-left graphic in the capture window, though the pattern can be rotated within the view without affecting the calibration if this is easier, as shown here:

![](/img/Camera/Calibration-Step2-Alternate1.png)



As you advance through the captures, the suggestion image will update. The first five images are the center of view, followed by bottom, left, right, then top. If your camera has a very strong fisheye effect, it may be necessary for you to move the non-center images inward a little to get a successful capture. This is ok.

The final four images are the corners, and these can be difficult to capture with high-distortion cameras. If your first 5 images score very well (below 0.3) you are allowed to skip the final four images (the 'Next' button will shows as 'Skip' in this case).  If you are having trouble capturing the last four images and don't have the option to skip, you can place the card anywhere within the view and capture that instead - We don't verify that your placement matches what we're suggesting.

Even after only a few good captures, the image on the right should appear to be free of lens distortion, as shown here:

![](/img/Camera/GoodCalibration.png)

A poorly calibrated result will still show lens distortion, and may have other artifacts, like the "wobble" seen in the lower-left of the gray image below:

![](/img/Camera/PoorCalibration.png)

If you don't get it straight away, you can re-capture the current image, or just go back to the beginning and try again. It can take a few tries to get a feel for how to align the card with the camera to get the lowest score.

When you have advanced through all the steps, and you are satisfied that you have a good calibration result with a nicely undistorted image, click Finish to save the results. You can also click the "Align Camera" button in the final page to take you to the next wizard automatically.



# Aligning the Camera and Workspace

Now that the camera is calibrated, you can move on to the next step, camera alignment - telling LightBurn where your camera is in relation to the workspace of your machine. From this step forward, it is very important that the camera not move in relation to the machine. It is possible to mount the camera to a movable piece of your laser, like the cover, as long as the position of the camera is the same when you use it as it is when you calibrate the alignment. The camera should be firmly mounted pointing at the center of the machine work area, with a clear view.

#### Cutting the Alignment Markers

In the Tools menu, choose "Calibrate Camera Alignment" to start the alignment wizard. Choose the same camera you did in the Lens Calibration wizard.

After selecting the camera and verifying that you can see an image from it, click Next and you'll get to this screen:

![](img/Camera/CameraAlignmentWizard.png)

This page uses your laser to cut a target pattern onto a piece of material, such as card stock, paper, cardboard, or thin wood. The pattern that will be cut is shown on the right side of the display.

LightBurn supports many different types of laser, so we need you to specify how fast and at what power to do this cut. You should choose settings that will make a dark surface mark on the material, but not cut through it. The "Support Height" and "Material Thickness" values can be set to zero if you do not normally use these values when cutting.

Follow the directions in order - set the numbers appropriately, use the Frame button to check that the material is aligned with the cut, and click Start when you're ready. If the cut comes out incorrectly (too light, or too strong) change the settings and try again. Your results should look something like this:

![](/img/Camera/PrintedMarkers.jpg)

When you have a good result, click next.

#### Capturing the Target Marker Image

From this screen, you're going to capture the alignment image. *It is very important you do not move the target marker image after cutting it.* Use the jog or "send to corner" buttons here to move the laser out of the view of the camera. When the camera has a clear view of all four targets, click the Capture button. You should see an undistorted version of the camera view appear in the right side of the window, with all four corner targets visible, as shown below:

![](/img/Camera/CameraAlignmentCapture.png)



#### Marking the Targets

On this page you 'tag' each of the targets by double-clicking in the center of each one in order. You can pan and zoom around the image using the same controls as the LightBurn edit and preview windows. When you double-click, a red '+' mark will appear. Place a marker in the center of each of the four targets, in the order they are numbered (1, 2, 3, 4). If you place one incorrectly, you can double click near it to shift it around, or click "Undo Last" to remove it and try again.

![](/img/Camera/PlacingMarkers.png)



Place each marker as accurately as you can. You can see the ideal placement here:

![](/img/Camera/PlacingMarkers2.png)

When you have placed all four markers in sequence, zoom back out and verify that all four are visible and clearly centered on the targets, like this:

![](/img/Camera/FinalMarkerPlacement.png)

Click Next to finish the marker placement screen and click Finish to complete the process and store the results.  You're done!



Now that everything is aligned, open the Camera Control window again, and simply click "Update Overlay" to capture and project whatever happens to be in the camera view onto your workspace, as shown:

![](/img/Camera/AligningTheLaser.jpg)

Click the "Fade" button to dim the background image, or the "Show" button to toggle it off and on.

