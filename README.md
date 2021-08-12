# RELEVANCE-HOPE
This is the repository of HOPE, the computation and prediction framework for wireless communication.

# Pre-requisites

i) HOPE requires ROS. Please visit the official ROS wiki for installation guidlines: http://wiki.ros.org/Installation/

# Compiling

i) Open a console as described in the ROS installation guidlines
ii) In the root of the HOPE workspace type: catkin_make

# Running the HOPE package (in devel mode)

i) Open a console as described in the ROS installation guidlines
ii) Browse to <path-to-HOPE>/devel and run setup.bat or setup.sh (on *nix systems source will also do the trick)
iii) In the root of the HOPE workspace type: rosrun hope hopeMain.py

# Creating an install package

i) Open a console as described in the ROS installation guidlines
ii) In the root of the HOPE workspace type: catkin_make install
iii) You will find the complete HOPE package ready to be deployed under <path-to-HOPE>/install