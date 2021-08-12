cmake_minimum_required(VERSION 2.8.3)
project(HOPE)

find_package(catkin REQUIRED COMPONENTS dynamic_reconfigure message_generation rosgraph_msgs rospy std_msgs)

add_message_files(
  FILES
  dummyMsg.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_install_python(PROGRAMS hope.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)