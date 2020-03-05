# CoreSystem

## Structure
```
.
├── lib
│   ├── pybind11             
│   │   └── include
|   |       └── pybind11
|   |           └── pybind11.h
|   |
│   │
│   └── daidalus                       
│       └── include       
|           └── daidalus.h          
│   
├── src
│   |── wrapper
|   |   |── __init__.py
|   |   └── pybind11.h
|   |
|   └── py_src
|       |── __init__.py
|       └── code.py
|
|                           
├── CMakeLists.txt                             
└── setup.py                         
```

## Installing CMAKE:

Uninstall the default version provided by Ubuntu’s package manager:
`sudo apt-get purge cmake`
Go to the official CMake webpage, then download and extract the latest version. Update the version and build variables in the following command to get the desired version:
`version=3.x`
`build=3`
`mkdir ~/temp`
`cd ~/temp`
`wget https://cmake.org/files/v$version/cmake-$version.$build.tar.gz`
`tar -xzvf cmake-$version.$build.tar.gz`
`cd cmake-$version.$build/`
Install the extracted source by running:
`sudo apt-get install libssl-dev`
`./bootstrap`
`make -j4`
`sudo make install`
Test your new cmake version.
`cmake --version`
Results of cmake --version:
cmake version 3.10.X



## Install Daidalus:
`git clone https://github.com/nasa/WellClear.git`
`cd WellClear/DAIDALUS/C++`
`make`

## Install Pybind11 inside lib:
`git clone https://github.com/pybind/pybind11.git`