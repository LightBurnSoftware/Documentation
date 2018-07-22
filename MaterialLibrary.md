[Return to main page](README.md)
<a name="Material Library"></a>

# Material Library

LightBurn's Material Library provides a way to store and organize lots of cut presets, and have a way to quickly apply them.  This is entirely user-generated - You set up a cut layer however you like and save it to a Library.  You set a material type, thickness (if appropriate), and a short description.

![Library_UI.png](/img/MaterialLibrary/Library_UI.png)

Any Library setting can be applied to a cut layer by selecting the library entry and assign it to the layer. Settings are copied, so if you need to make edits to the setting you won't hurt the copy in your library - you can edit those independently.



## Understanding Material Library

Material Library is a simple yet powerful component of Lightburn intended to assist in the management of the laser cutting process.  The viedo below provides an overview of how to create, use and manage libraries.

[Video Tutorial #1: Using the Material Library](https://vimeo.com/257846436)

The first time you launch LightBurn, an empty Material Library is automatically set up and ready for new entries.  You can easily add to, edit and manage cut settings in this library.  Saved libraries can be loaded and shared from local or network accessed and even cloud based storage for convenience.  To get started, make sure you can see the Material Library window.

- In the top menu, select "Window" to ensure that "Library" is checked on.  If not, select it to turn the window on.  This will display the Material Library window in the lower-right of the display next to a box called "Laser".




## Create new from layer

LightBurn makes it easy to build out your library using the current cut settings assigned to any cut layer.  

1. Select one of your cut layers then click the *Create new from layer* button in the "Library" window.

![Library_new_Layer.png](/img/MaterialLibrary/Library_new_Layer.png)



2. Fill out the details sheet providing a *Name*, *Thickness* (if appropriate) and a short *Description* of the cut layer parameters.  Once completed, click the *Ok* button to save this new entry into your library.

![Library_new_Layer_details.png](/img/MaterialLibrary/Library_new_Layer_details.png)



3. Now you can use this new entry titled "Birch Ply" anytime in the future and easily assign it to a new cut layer.

![Library_new_Layer_result.png](/img/MaterialLibrary/Library_new_Layer_result.png)

There are several helpful ways to facilitate adding to and managing your library covered later in the "Manage existing Library" section below.



## Save a Library

As you fill out the Library with your favorite materials, it is always a good idea to periodically save your additions.  To do this, click the *Save* button.

![Library_Save.png](/img/MaterialLibrary/Library_Save.png)



## Assign Library settings to layer

Now that you have some entries added to your library, you can use them to quickly and easily apply these settings to your work.  Settings are copied, so if you need to make edits to the setting you have applied you won't hurt the originals in your library.

![Libary_Assign.png](/img/MaterialLibrary/Libary_Assign.png)



## New Library

Depending on your workflow, you may find it desirable to have several libraries to work from.  You can start a new Material Library anytime by clicking the *New* button at the lower-right corner of the "Library" window.  Now you are presented with a new, blank library ready to fill out and save.

![Library_New.png](/img/MaterialLibrary/Library_New.png)



## Load a Library

Selecting *Load* provides access to your previously saved Libraries.  Once clicked, a file finding window will open allowing you to point to a saved library.  Select library of choice and click the *Open* button.  Your chosen file will then become the active library for use.

![Library_Load.png](/img/MaterialLibrary/Library_Load.png)



## Manage existing Library

Existing Library entries can be managed in several helpful ways. Changing existing cut settings and discriptions, quickly duplicating entries, removing unwanted entries or producing copies of the entire library can be done in a snap. 

###### 	Note: These items are only selectable when "Description" is selected.

![Library_Edit.png](/img/MaterialLibrary/Library_Edit.png)



### Edit Cut

Click *Edit Cut* to open the "Cut Settings Editor".  This allows you to change any of the cut settings as you would normally and saves them back to the library.

### Edit Description 

Click *Edit Description* to modify the Name, Thickness and Description for the highlighted entry.

### Duplicate

Click *Duplicate* to create a copy of the highlighted entry.  This can be helpful in quickly adding to your library.  

###### Hint: Combined with *Edit Description* and *Edit Cut* you can keep the same "Material Name" and "Thickness" to create 'nested' entries (e.g. 3mm cut, scan and image).  Keeping just the "Name" while changing the "Thickness" allows nesting of different thicknesses of the same material. 

### Delete

Click *Delete* to remove a single cut setting entry from the library.

### Save As

Click *Save* As to create a complete copy of your active library and saves it under a new name of your choice.



## Advanced Usage

### Multiple machines/users access to shared Library

Multiple machines can access a single Material Library file hosted on a network drive or from cloud service storage (e.g. Dropbox, Google Drive, iCloud, OneDrive, etc.).  

1. Create a library on one machine and save it to your network or Google drive, DropBox, etc..  
2. Point to that saved library file after hitting 'Load' in the 'Library' screen of LB for each machine.
3. If you edit that library the changes will be there of both machines as they are pointing to the same file.
