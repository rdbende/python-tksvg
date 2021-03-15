# tksvg for Python's Tkinter
[tksvg](https://github.com/oehhar/tksvg) is a package for Tcl/Tk that
adds support for SVG image files. Tkinter makes use of Tcl/Tk under the
hood, and thus can benefit from this addition. Note that SVG support 
has been included in Tk 8.7 and thus this package can be made obsolete 
in the future when Python gets distributed with Tk 8.7. This package is 
merely a repackaging of the `tksvg` library for Python with a modified
build system.

## Building and installation
This package makes use of the same build system as [`gttk`](https://github.com/TkinterEP/python-gttk)
and other Tcl C-extensions with CMake. This means that on both Windows
and Linux you will need a working CMake installation that can find the
Tcl development files. If you wish to build with Visual Studio, you can
build with the build system of the [upstream](https://github.com/oehhar/tksvg).

### Linux
Adapt the commands to your specific distribution. The commands given
here assume Ubuntu 20.04.
```bash
sudo apt install cmake build-essential tcl-dev tk-dev python3-tk
python -m pip install scikit-build
python setup.py install
```

### Windows
Due to the rolling-release type distribution of MSYS, no up-to-date 
build instructions are provided in this file. Please refer to the 
AppVeyor build configuration in `.appveyor.yml` to derive the latest 
build instructions. Some general pointers:
- The commands assume that you have a working [MSYS2](https://www.msys2.org/)
  environment. If you do not have this, you'll have to set it up to make 
  use of the Windows build system.
- Dependencies of the compiled binaries are detected and found using 
  [Dependencies](https://github.com/lucasg/Dependencies). Make sure it
  is available before running the `setup.py install` command.
- The AppVeyor configuration may have to work around bugs in MSYS that 
  you might not encounter if you're using a different version. If you're 
  confused by how the dependencies are installed, simply refer to the
  list found in [`setup.py`](https://github.com/TkinterEP/python-tksvg/blob/02cf680bf4b9c5471d6bff1508e9705648ef18cd/setup.py#L52).
  
## Usage
Using the library has been made as similar as possible to using a normal
`tk.PhotoImage`. Simply create an `SvgImage` instance and the `tksvg` 
library will automatically be loaded for you.
```python
import tkinter as tk
import tksvg

window = tk.Tk()
svg_image = tksvg.SvgImage(file="tests/orb.svg")
label = tk.Label(image=svg_image)
label.pack()
window.mainloop()
```

## License & Copyright
This repository merely provides a version of the original [tksvg](https://github.com/oehhar/tksvg)
for Python's Tkinter. The package is available under the BSD-like 
[Tcl License](https://github.com/TkinterEP/python-tksvg/blob/master/LICENSE.md).
The build system (`setup.py`, `.appveyor.yml` and `.travis.yml`) are 
available under the terms of [GNU GPLv3](http://www.gnu.org/licenses/gpl-3.0.en.html),
as any changes to these should be shared under permissive terms so as to
preserve the possibility of building these packages.
```
Copyright (C) 2002-2004 Maxim Shemanarev http://antigrain.com
Copyright (c) 2013-14 Mikko Mononen memon@inside.org
Copyright (c) 2018 Christian Gollwitzer auriocus@gmx.de
Copyright (c) 2018 Christian Werner https://www.androwish.org/
Copyright (c) 2018 Rene Zaumseil r.zaumseil@freenet.de
Copyright (c) 2020 Juliette Monsel
Copyright (c) 2021 RedFantom <redfantom@outlook.com>
```
