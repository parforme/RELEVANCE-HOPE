from hsys import module
from hsys import databroker
from hope.msg import ferPredictionMsg
from hope.msg import ferPredictionMsgResult
import numpy
import rospy
import json
import queue
import os

class ferPrediction(module.Module):
    def __init__(self):
        super(ferPrediction, self).__init__()
     
    def callback(self, data):
        self.queue.put(data)

    def initModule(self, configFilesPath):
        print("Initializing simplified FER prediction module for 802.11p, using QPKS and a coding rate of 1/2.")
        self.configFilesPath = configFilesPath
        jf = open(os.path.join(configFilesPath, 'pathLossModel.json'))
        print("Loading path loss model parameters...")
        self.modelParams = json.load(jf)
        jf.close()
        self.queue = queue.Queue(200)
        print(f"Found the following model Parameters: Tx Power ({self.modelParams['transmitPower']} dB), G0 ({self.modelParams['G0']} dB), PLexp ({self.modelParams['exponent']} dB), Sigmoid-a ({self.modelParams['sigA']}), Sigmoid-b ({self.modelParams['sigB']})")
        databroker.addListener("ferPrediction", ferPredictionMsg, self.callback)
        self.pub = databroker.addPublisher("predictedFer", ferPredictionMsgResult, 10)
        self.start()
    
    def run(self):
        while True:
            if not self.queue.empty():
                p = self.queue.get()
                d = numpy.sqrt((p.posx - p.pointx)**2 + (p.posy - p.pointy)**2 + (p.posz - p.pointz)**2)
                rxPower = float(self.modelParams['transmitPower']) - (float(self.modelParams['G0']) + 10*float(self.modelParams['exponent']) * numpy.log10(d))
                rospy.loginfo(rxPower)
                if p.obstructed == True:
                    rxPower -= 30
                fer = 1 - 1/(1+numpy.exp(-1*float(self.modelParams['sigA'])*(rxPower - float(self.modelParams['sigB']))))
                ferResult = ferPredictionMsgResult()
                ferResult.fer = fer
                rospy.loginfo(ferResult)
                self.pub.publish(fer)

