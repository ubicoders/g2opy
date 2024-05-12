# for ubuntu 16 and python3
#! /bin

# install cmake
# install eigen 3.3.4 only: http://eigen.tuxfamily.org/index.php?title=News:Eigen_3.3.4_released!


# system
apt update
apt install python3-dev cmake libglew-dev glew-utils qtbase5-dev libsuitesparse-dev libsuitesparse-dev qtdeclarative5-dev qt5-qmake libqglviewer-dev-qt5 libsuitesparse-dev -y

# # unzip and install eigen
# tar -xvjf eigen-eigen-5a0156e40feb.tar.bz2
# cd eigen-eigen-5a0156e40feb
# mkdir build
# cd build
# cmake ..
# make install 
# cd ../..

# build g2opy
mkdir build
cd build
cmake ..
make -j8
cd ..
# python setup.py install

