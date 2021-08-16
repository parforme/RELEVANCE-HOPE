from hsys import module
from hsys import databroker
from msg import ferPredictionMsg
import rospy

class ferPrediction(module.Module):
    def __init__(self):
        super(ferPrediction, self).__init__()
     
    def callback(self, data):
        print("Got data: " + data.data)

    def initModule(self):
        print("Initializing simplified FER prediction module.")
        # initialize a publisher
        self.pub = databroker.addListener("ferPrediction", ferPredictionMsg, self.callback)
        # run the thread of this module
        self.start()

