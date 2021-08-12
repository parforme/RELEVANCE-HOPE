# RELEVANCE-HOPE
This is the repository of HOPE, the computation and prediction framework for wireless communication.

# Pre-requisites

- HOPE requires ROS. Please visit the official ROS wiki for installation guidlines: http://wiki.ros.org/Installation/

# Compiling

- Open a console as described in the ROS installation guidlines
- In the root of the HOPE workspace type: catkin_make

# Running the HOPE package (in devel mode)

- Open a console as described in the ROS installation guidlines
- Browse to <path-to-HOPE>/devel and run setup.bat or setup.sh (on *nix systems source will also do the trick)
- In the root of the HOPE workspace type: rosrun hope hopeMain.py

# Creating an install package

- Open a console as described in the ROS installation guidlines
- In the root of the HOPE workspace type: catkin_make install
- You will find the complete HOPE package ready to be deployed under <path-to-HOPE>/install