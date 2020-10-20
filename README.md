# Simple Image Editor
Maiden project using **python**. Opted for **tkinter** as gui and **pil** (pillow) for image processing.
Code written in **pycharm** ide (though **jupyter notebook** + **anaconda** are also good). Good intoduction on how to import python modules and work with widgets (sliders, buttons, checkboxes etc). 

Functionality include:
  - adjusting colour, brightness & contrast
  - image rotation
  - image resizing
  - applying filters (blur, median, emboss, poster etc.)
  - colour filters
 
You can convert the python code to **executable** (.exe file) to enable it to run as a standalone app - just make sure it is in the same folder as other dependent files!
**pyinstaller** was used to compile the python code - from a cmd window:
 
      pyinstaller -w -F -i "icon.ico" SIE.py

The executable will appear in the dist folder.

When running executable, if you receive "Failed to execute script pyi_rth_pkgres" error try to reinstall pyinstaller with the github version:

      pip uninstall pyinstaller<br/>
      pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip

Sample.<br>
![alt text](https://github.com/waiky8/simple-image-editor/blob/master/screenshots/screenshot1.png)
![alt text](https://github.com/waiky8/simple-image-editor/blob/master/screenshots/screenshot2.png)
![alt text](https://github.com/waiky8/simple-image-editor/blob/master/screenshots/screenshot3.png)
