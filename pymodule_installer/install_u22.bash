pip install .
pybind11-stubgen g2opy

cp stubs/g2opy/g2o/* g2opy/g2o
pip uninstall g2opy -y 
pip install .