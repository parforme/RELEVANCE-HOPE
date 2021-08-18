# This is an example HOPE module using rospy.
from hsys import module
from hsys import databroker
from std_msgs.msg import String
import rospy

class dummyModule(module.Module):
    def __init__(self):
        super(dummyModule, self).__init__()
        print("Constructor of dummy module called.")
        
    def initModule(self, configFilesPath):
        print("Initializing dummy module.")
        # initialize a publisher
        self.pub = databroker.addPublisher("dummyModule", String, 1)
        # run the thread of this module
        self.start()

    def run(self):
        # publish some
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            self.pub.publish(hello_str)
            rate.sleep()
