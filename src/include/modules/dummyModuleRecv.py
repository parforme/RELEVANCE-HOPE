# This is an example HOPE module using rospy.
from hsys import module
from hsys import databroker
from std_msgs.msg import String
import rospy

class dummyModuleRecv(module.Module):
    def __init__(self):
        super(dummyModuleRecv, self).__init__()
    
    def callback(self, data):
        print("Got data: " + data.data)

    def initModule(self):
        print("Initializing dummy receiver module.")
        # initialize a listener node
        self.pub = databroker.addListener("dummyModule", String, self.callback)
    