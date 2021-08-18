cmake_minimum_required(VERSION 2.8.3)
project(hope)

find_package(catkin REQUIRED COMPONENTS dynamic_reconfigure message_generation rosgraph_msgs rospy std_msgs)

catkin_python_setup()


add_message_files(
  FILES
  dummyMsg.msg
  ferPredictionMsg.msg
  ferPredictionMsgResult.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_install_python(PROGRAMS hopeMain.py 
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)