[Return to main page](README.md)

# Frequently Asked Questions

### Q: I just paid, how long until my license arrives?

A: Sometimes as long as 12 hours. The license process is manual, and we occasionally require sleep.

### Q: How is the license key delivered?

A: It is sent to the email address you provided when you paid, or your PayPal email address, if you purchased with PayPal.

### Q: If I update, do I need to re-apply my license, or lose my trial?

A: No, the license system stores a digital fingerprint independent of the software. You are free to update as long as either your trial or license have not expired. When your license expires, the version you have will continue to work, but you will not be able to run any version created after your license expired. You can renew to gain access to updates for another year. We’re hoping to make the renewal fee $25.

### Q: Does LightBurn work with the stock K40 board?

A: No. Please get a real controller that allows control of power through software. Even a lowly Arduino running Grbl can do this. We recommend a Cohesion3D Mini (Laser Upgrade Bundle) though – it’s a drop-in replacement that takes about 5 to 10 minutes to install.

### Q: Does LightBurn work with (strong LED flashlight they called a laser) that I bought from HappySunshine888 on EBay?

A: It might. You’ll need to find out what kind of controller it has, and if it uses Grbl, Smoothieware, or something proprietary. If it’s one of the first two, it will probably work, though you may have to update the firmware or change some of the settings. We can’t tell you how to do this, but Google or another forum member probably can.

### Q: Does LightBurn support Epilog, Trotec, Universal, Full Spectrum, or GCC Lasers?

A: Sorry, no. We’re a very small company, and don’t have the financial resources to buy one of these high priced wonders in the hope that we can reverse engineer the control protocols, and they don’t return our calls. If enough of their customers poke them, perhaps that will change. (If you have one of these and are technical enough to help with traffic captures, we’d love to talk to you)

### Q: Do you have a list of supported features somewhere?

A: Sort of – our documentation is available online if you’re one of those rare unicorns who reads such things. Writing a real list of supported features would take a long time, and would constantly be out of date – we update **very** often. (<https://github.com/LightBurnSoftware/Documentation/blob/master/README.md>)

### Q: What does “ALARM 2” mean?

A: It means your GRBL controller tried to go out of bounds. (<http://grblminicnc.blogspot.com/2017/04/grbl-error-list.html>)

### Q: When I hit the home button it just says “error: 5” – why?

A: You don’t have homing enabled on your GRBL controller. (<http://grblminicnc.blogspot.com/2017/04/grbl-error-list.html>)

### Q: I hit the thing but it didn’t do the thing.

A: This is not a question, and does not contain any useful information whatsoever. Please try to be descriptive when you post questions – we’re here to help, but we’re not clairvoyant.

### Q: I have suggestions – should I post them here?

A: You should post them to our suggestion site. Other people can vote on suggestions, we read it regularly, and it helps us prioritize feature development. It’s here: <https://lightburn.fider.io/>

### Q: I imported an SVG file but only get Image options for Mode

A: SVG files do not automatically imply vector drawings. It is possible to have a bitmap/raster image embedded in an SVG file and LightBurn will treat it as any other bitmap and give you the Image engraving options. If you are trying to create vector tracing, you will need to use the Trace Image (ALT+T or Tools > Trace Image) function in LightBurn or another application to create line art of the image. 