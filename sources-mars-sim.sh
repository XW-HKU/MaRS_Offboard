#!/bin/bash

cd $(pwd)/src
if [ ! -d "VTOL-FC" ]; then
  git clone https://github.com/XW-HKU/VTOL-FC.git
fi
cd VTOL-FC
git pull
cd ../..

source $(pwd)/devel/setup.bash

source $(pwd)/src/setup_gazebo.bash $(pwd) $(pwd)

echo -e "ROS_PACKAGE_PATH $ROS_PACKAGE_PATH"
