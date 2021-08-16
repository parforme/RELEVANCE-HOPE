# The databroker wraps the communication principles
# Currently we use ROS; but this could be easily changed

import rospy

def addService(serviceNameString, serviceName, functionHandle):
    return rospy.Service(serviceNameString, serviceName, functionHandle)

def waitForService(servicNameString):
    rospy.wait_for_serivce(servicNameString)

def addPublisher(publisherName, dataType, queueSize):
    return rospy.Publisher(publisherName, dataType, queue_size=queueSize)

def initComNode(moduleName):
    rospy.init_node(moduleName, anonymous=True)

def publish(publisher, data):
    publisher.publish(data)

def addListener(publisherName, dataType, callback):
    rospy.Subscriber(publisherName, dataType, callback)
