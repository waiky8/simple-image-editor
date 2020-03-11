# simple image editor
First attempt at **python** programming. Went with **tkinter** as gui platform and **pil** (pillow) for image processing.
Code written in **pycharm** ide (though **jupyter notebook** + **anaconda** are also good). Learned how to install and import python modules and work with widgets (sliders, buttons, checkboxes etc). Functionality include:
  - adjusting colour, brightness & contrast
  - image rotation
  - image resizing
  - applying filters (blur, median, emboss, poster etc.)
  - colour filters
 
 Note that you can convert the python code to **executable** (.exe file) to enable it to run as a standalone using - I used **pyinstaller** from cmd window:
  "pyinstaller -w -F -i "icon.ico" SIE.py"
 
Note, first time that I ran the executable I got "Failed to execute script pyi_rth_pkgres". Reinstalled pyinstaller with github version to fix the problem:
  pip uninstall pyinstaller
  pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
 
