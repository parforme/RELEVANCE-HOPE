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

class ferPrediction(Node, threading.Thread):
    def __init__(self):
        super().__init__("FERPrediction")
        threading.Thread.__init__(self)
        self.declare_parameter('configFilesPath', 'world')

     
    def callback(self, data):
        self.queue.put(data)

    def initModule(self):
        print("Initializing simplified FER prediction module for 802.11p, using QPKS and a coding rate of 1/2.")
        self.configFilesPath =  self.get_parameter('configFilesPath').get_parameter_value().string_value
        jf = open(os.path.join('.\\config\\', 'pathLossModel.json'))
        print("Loading path loss model parameters...")
        self.modelParams = json.load(jf)
        jf.close()
        self.queue = queue.Queue(200)
        print(f"Found the following model Parameters: Tx Power ({self.modelParams['transmitPower']} dB), G0 ({self.modelParams['G0']} dB), PLexp ({self.modelParams['exponent']} dB), Sigmoid-a ({self.modelParams['sigA']}), Sigmoid-b ({self.modelParams['sigB']})")
        
        self.subscription = self.create_subscription(ferPredictionMsg, "FERPrediction", self.callback, 10)
        self.publisher = self.create_publisher(ferPredictionMsgResult,"predictedFER", 10)
        self.start()
    
    def run(self):
        while True:
            if not self.queue.empty():
                p = self.queue.get()
                d = numpy.sqrt((p.posx - p.pointx)**2 + (p.posy - p.pointy)**2 + (p.posz - p.pointz)**2)
                rxPower = float(self.modelParams['transmitPower']) - (float(self.modelParams['G0']) + 10*float(self.modelParams['exponent']) * numpy.log10(d))
                fer = 1 - 1/(1+numpy.exp(-1*float(self.modelParams['sigA'])*(rxPower - float(self.modelParams['sigB']))))
                ferResult = ferPredictionMsgResult()
                ferResult.fer = fer
                self.get_logger().info('FER: "%f"' % ferResult.fer)
                self.publisher.publish(ferResult)

def main(args=None):
    rclpy.init()
    print(sys.argv)
    FERPred = ferPrediction()
    FERPred.initModule()
    rclpy.spin(FERPred)

if __name__ == '__main__':
    main()
