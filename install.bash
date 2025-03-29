#! /bin
# Update and install dependencies
apt update && apt-get install --no-install-recommends -y \
  gcc git openssh-client less curl \
  libxtst-dev libxext-dev libxrender-dev libfreetype6-dev \
  libfontconfig1 libgtk2.0-0 libxslt1.1 libxxf86vm1 \
  && rm -rf /var/lib/apt/lists/* 

# Install additional dependencies
apt update && apt install cmake build-essential cmake libglew-dev glew-utils qtbase5-dev \
    libsuitesparse-dev libsuitesparse-dev qtdeclarative5-dev qt5-qmake libqglviewer-dev-qt5 libsuitesparse-dev -y

apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa -y
add-apt-repository universe -y

pip install numpy==1.26.4

# unzip and install eigen
tar -xvjf eigen-eigen-5a0156e40feb.tar.bz2
cd eigen-eigen-5a0156e40feb
mkdir build
cd build
cmake ..
make install 
cd ../..

# build g2opy
mkdir build
cd build
cmake ..
make -j8
cd ..
# python setup.py install

cp ./lib/g2o.* ./pymodule_installer/g2opy/

cd ./pymodule_installer/
pip install .

cd ..
echo "Running tester.py"
python tester.py
