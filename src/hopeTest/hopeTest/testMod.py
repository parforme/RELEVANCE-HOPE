from custom_msgs.msg import FerPredictionMsg as ferPredictionMsg
from custom_msgs.msg import FerPredictionMsgResult as ferPredictionMsgResult
import numpy
import json
import threading
import queue
import os
import sys
import rclpy
from rclpy.node import Node

class dummyModuleFER(Node, threading.Thread):
    def __init__(self):
        super().__init__("dummyModuleFER")
        threading.Thread.__init__(self)

    def initModule(self):
        print("Initializing dummy fer module.")
        # initialize a publisher
        self.pub = self.create_publisher(ferPredictionMsg,"FERPrediction", 10)
        # run the thread of this module
        self.start()
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
        self.pub.publish(myMsg)

def main():
    rclpy.init()
    dummyF = dummyModuleFER()
    dummyF.initModule()
    rclpy.spin(dummyF)

if __name__ == '__main__':
    main()
