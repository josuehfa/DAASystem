#!/bin/bash
# ---  Start Inside Cloud9  ----
echo "------ Installing packages ------"
sudo apt-get install build-essential
sudo apt-get install libssl-dev
sudo apt-get install libboost-dev

echo "-----  Cloning Pybind11  -----"
cd "/home/ubuntu/environment/DAASystem/CoreSystem/lib/"
git clone https://github.com/pybind/pybind11.git

echo "-----  Installing CMake  -----"
cd "/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3"
sudo make install

echo "-----  Start Setup.py File -----"
cd  "/home/ubuntu/environment/DAASystem/CoreSystem"
python setup.py develop