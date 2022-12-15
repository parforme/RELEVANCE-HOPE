# RELEVANCE-HOPE
This is the repository of HOPE, the computation and prediction framework for wireless communication.

If ROS 2 is used, then all the published topics can be found under the "hope" node.

# Pre-requisites

- HOPE requires ROS 2. Please visit the official ROS 2 wiki for installation guidelines.

# Compiling

- Open a console as described in the ROS 2 installation guidelines
- In the root of the HOPE workspace type: colcon build --merge-install

# Running the HOPE package (in devel mode)

- Open a console as described in the ROS installation guidelines
- Browse to <path-to-HOPE>/install and run local_setup.bat or setup.sh (on *nix systems source will also do the trick)
- In the root of the HOPE workspace run the package using ros2 and set the config files path run hope hopeMain.py _configFilesPath:= absolute-path-to-config-directory


