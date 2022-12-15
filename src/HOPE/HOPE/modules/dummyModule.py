import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading

class dummyModule(Node):
    def __init__(self):
        super().__init__("dummyModule")

        print("Constructor of dummy module called.")
        
    def initModule(self, configFilesPath):
        print("Initializing dummy module.")
        # initialize a publisher
        self.pub = self.create_publischer(String, "dummyModule", 1)
        self.timer = self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        # publish something
        hello_str = "hello world %s" % rospy.get_time()
        self.get_logger().info('msg: "%s"' % hello_str)
        self.pub.publish(hello_str)
