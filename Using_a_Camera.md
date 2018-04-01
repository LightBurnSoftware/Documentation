[Return to main page](README.md)

# Using a camera with LightBurn

LightBurn includes a camera feature which allows a USB connected camera to be used in a couple of different ways:

- Monitoring your laser
- Positioning your work
- Tracing artwork directly from the bed of the laser



Using the camera as a monitor is simple - enable the Camera Control window (right-click on any window or toolbar and choose "Camera Control" from the pop-up).

You'll be presented with a window that looks like this:

![](.\img\Camera\CameraControl.png)

If your system has a compatible USB camera connected, it will appear in the Camera drop-down box. Select the camera, and the view from the camera will appear in the window, as shown:

![](.\img\Camera\CameraControl-Monitor.png)



The image from this camera is very distorted, because it is uses a fish-eye lens to achieve a very wide field of view, and it's mounted at an odd angle for use with the laser. LightBurn can counter both of these, and simulate a top-down view from nearly any camera. It takes a bit of effort to set up, but it's well worth it.

# Camera Calibration

In order to use the camera for work placement, it's necessary to "teach" LightBurn how to remove the distortion from your camera lens, and where your camera is in relation to the work area of your laser. The first part of this is accomplished in the Camera Calibration window.

You'll need to download and print the following two images:

[Calibration-Circles.png](./img/Camera/Calibration-Circles.png)
[Calibration-Chess.png](./img/Camera/Calibration-Chess.png)

Do not resize them - The circles image will be approximately 148mm x 105mm (5.8" x 4.1"), and the chessboard will be approximately 210mm x 297mm (8.5" x 11").

Mount them on stiff card, foam-board, or wood, so the images remain very, very flat.

### The camera calibration screen

Position your laser head away from the working area of the machine and out of the field of view of the camera.  Make sure you do not have your camera selected in the Camera Control window, and choose "Tools -> Calibrate Camera" from the main menu.

You will enter the following screen:

![](.\img\Camera\CalibrateCamera.png)

Choose your camera in the drop-down, as before, and you'll see the view from the camera.

With your circles image printed on stiff card, place the card in the center of the field of view of the camera, with the printed face of the card pointed directly at the camera, similar to what you see here:

![](.\img\Camera\Calibration-Step1.png)

Click the Capture + Calibration button (highlighted above) and you should see something like this:

![](.\img\Camera\Calibration-Step2.png)

Below the image on the left you see "success - Image error: --- , average error: ---"  That's telling you that:

- The image was captured, and the calibration pattern was found
- After distortion removal, the positions of the dots in the image aligns with the known positions of the printed dots with an error of 0.13 pixels - That's very good.

Notice that in the gray image that appears to the right, the pattern of circles is not distorted, though the image around them is considerably worse. That is temporary, and the result of only having a single calibration image to work with. Move the circles image around the view of your camera, roughly in a tic-tac-toe board pattern, capturing an image of the circles in each of the corners of the camera, and the middle, at a minimum. At each capture, if the image error value exceeds 2.0, click "Remove Last Image" and try again. It's also possible that you'll see a "failure" message, if LightBurn was unable to find the circles pattern in the image. You may need to reposition the card away from the edge of the image, or light the card more uniformly.

In all, you're shooting for a final average error value of less than 1.0, with at least 6 images captured across the field of view of the camera.

When you have a good calibration, the image on the right should appear to be free of lens distortion, as shown here:

![](.\img\Camera\GoodCalibration.png)

A poorly calibrated result will still show lens distortion, and may have other artifacts, like the "wobble" seen in the lower-left of the gray image below:

![](.\img\Camera\PoorCalibration.png)

If you don't get it straight away, you can "Restore Default" and try again, or simply "Remove Last Image" to remove a bad one, and keep going. It can take a few tries to get the feel for it.

When satisfied that you have a good calibration result, with a nicely undistorted image, click OK to save the results.

# Aligning the Camera and Workspace

Now that the camera is calibrated, you can move on to the next step. Bring up the Camera Control window again and select your camera. You will see the bed of your machine through the camera as before. Place the printed chess-board image in the center of the workspace, and as straight as you can by eye, like so:

![](.\img\Camera\AlignedChessboard.jpg)

From the camera, it looks like this:

![](.\img\Camera\AlignedChessboard-FromCamera.jpg)

Click the "Get Chessboard" button, and if everything has gone well, you'll see something like this in the edit window of LightBurn:

![](.\img\Camera\BackgroundImage-Chessboard.png)

You're almost done - The chessboard will be placed in the exact center of the display, and should be quite close to "real world" position, but won't be exact. For example, if I jog my laser to this point in LightBurn:

![](.\img\Camera\Position-Calculated.png)

The laser is actually pointing here:

![](.\img\Camera\Position-Actual.jpg)



It's very close, but not quite right. The Camera Control window has Width / Height / Shift controls to adjust the position of the background image in the edit window to align it with the real-world positioning of the chessboard. Use those controls to adjust the image until the two align. It can take a bit of time, and it's something we're going to improve the process for in the near future - consider this version 1.0.

Once everything is aligned, you can remove the chessboard and simply click "Update Overlay" to capture and project whatever happens to be in the camera view, as shown:

![](.\img\Camera\AligningTheLaser.jpg)

Click the "Fade" button to dim the background image, or the "Show" button to toggle it off and on.

