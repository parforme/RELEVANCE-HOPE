from hsys import module
from hsys import databroker
from hope.msg import ferPredictionMsg
from hope.msg import ferPredictionMsgResult
import rospy
import json

class ferPrediction(module.Module):
    def __init__(self):
        super(ferPrediction, self).__init__()
     
    def callback(self, data):
        # TODO: implement producer consumer pattern, such that we can handle a lot of prediction requests at once!
        print("Got data: " + data.data)
        self.pub.publish(1.0)

    def initModule(self):
        print("Initializing simplified FER prediction module.")
        jf = open('pathLossModel.json')
        print("Loading path loss model parameters")
        self.modelParams = json.load(jf)
        jf.close()
        print(f"Model Parameters: Tx Power ({self.modelParams.transmitPower}), G0 ({self.modelParams.G0}), PLexp ({self.modelParams.exponent})")
        databroker.addListener("ferPrediction", ferPredictionMsg, self.callback)
        self.pub = databroker.addPublisher("predictedFer", ferPredictionMsgResult, 10)
        
