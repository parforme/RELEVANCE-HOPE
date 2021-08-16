from hsys import module
from hsys import databroker
from msg import ferPredictionMsg
from msg import ferPredictionMsgResult
import rospy

class ferPrediction(module.Module):
    def __init__(self):
        super(ferPrediction, self).__init__()
     
    def callback(self, data):
        # TODO: implement producer consumer pattern, such that we can handle a lot of prediction requests at once!
        print("Got data: " + data.data)
        self.pub.publish(1.0)

    def initModule(self):
        print("Initializing simplified FER prediction module.")
        databroker.addListener("ferPrediction", ferPredictionMsg, self.callback)
        self.pub = databroker.addPublisher("predictedFer", ferPredictionMsgResult, 10)
        
