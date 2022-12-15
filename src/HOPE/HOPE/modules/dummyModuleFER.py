# This module is just for testing the FER prediction
from custom_msgs.msg import FerPredictionMsg as ferPredictionMsg
from custom_msgs.msg import FerPreductionMsgResult as ferPredictionMsgResult
import rclpy
from rclpy.node import Node


class dummyModuleFER(Node):
    def __init__(self):
        super().__init__("dummyModuleFER")
        print("Constructor of dummy fer module called.")
        
    def initModule(self, configFilesPath):
        print("Initializing dummy fer module.")
        # initialize a publisher
        self.publisher = self.create_publisher(ferPredictionMsgResult,"predictedFER", 10)
        # run the thread of this module
        self.timer = self.create_timer(1, self.timer_callback)
        
    def timer_callback(self):
        myMsg = ferPredictionMsg()
        myMsg.posx = 0.0
        myMsg.posy = 0.0
        myMsg.posz = 0.0
        myMsg.pointx = 10.0
        myMsg.pointy = 5.0
        myMsg.pointz = 0.0
        myMsg.obstructed = False
        self.publisher.publish(myMsg)
