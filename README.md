# simple image editor
First attempt at **python** programming. Went with **tkinter** as gui platform and **pil** (pillow) for image processing.
Code written in **pycharm** ide (though **jupyter notebook** + **anaconda** are also good). Learned how to install and import python modules and work with widgets (sliders, buttons, checkboxes etc). Functionality include:
  - adjusting colour, brightness & contrast
  - image rotation
  - image resizing
  - applying filters (blur, median, emboss, poster etc.)
  - colour filters
 
You can convert the python code to **executable** (.exe file) to enable it to run as a standalone app - just make sure it is in the same folder as other dependent files. I used **pyinstaller** to compile the python code. So from a cmd window:
 
pyinstaller -w -F -i "icon.ico" SIE.py

The executable will be in the dist folder.

Note, the first time that I ran the executable I got "Failed to execute script pyi_rth_pkgres". To fix the problem I reinstalled pyinstaller with the github version.

pip uninstall pyinstaller<br/>
pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
