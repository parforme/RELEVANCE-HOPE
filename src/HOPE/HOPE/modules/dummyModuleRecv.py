# This is an example HOPE module using rospy.
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class dummyModuleRecv(module.Module):
    def __init__(self):
        super().__init__("dummyModuleRecv")
    
    def callback(self, data):
        print("Got data: " + data.data)

    def initModule(self, configFilesPath):
        print("Initializing dummy receiver module.")
        # initialize a listener node
        self.subscription = self.create_subscription(String, "dummyModule", self.callback, 10)

    