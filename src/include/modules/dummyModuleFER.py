# This module is just for testing the FER prediction
from hsys import module
from hsys import databroker
from hope.msg import ferPredictionMsg
from hope.msg import ferPredictionMsgResult
import rospy

class dummyModuleFER(module.Module):
    def __init__(self):
        super(dummyModuleFER, self).__init__()
        print("Constructor of dummy fer module called.")
        
    def initModule(self, configFilesPath):
        print("Initializing dummy fer module.")
        # initialize a publisher
        self.pub = databroker.addPublisher("ferPrediction", ferPredictionMsg, 10)
        # run the thread of this module
        self.start()

    def run(self):
        # publish some
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            myMsg = ferPredictionMsg()
            myMsg.posx = 0.0
            myMsg.posy = 0.0
            myMsg.posz = 0.0
            myMsg.pointx = 10.0
            myMsg.pointy = 5.0
            myMsg.pointz = 0.0
            myMsg.obstructed = False
            rospy.loginfo(myMsg)
            self.pub.publish(myMsg)
            rate.sleep()
