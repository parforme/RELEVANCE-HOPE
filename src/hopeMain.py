import modules
import hsys
import sys
import rospy

def main(argv):
    # init our communication node
    hsys.databroker.initComNode('hope')
    print(argv)
    configFilesPath = rospy.get_param('~configFilesPath')
    modules.loadModules()
    modules.initModules(configFilesPath)
    print ("Loaded and initialized HOPE modules.")
    rospy.spin()

if __name__ == "__main__":
    main(sys.argv)