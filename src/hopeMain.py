import modules
import hsys
import sys
import rospy

def main(argv):
    # init our communication node
    hsys.databroker.initComNode('hope')
    modules.loadModules()
    modules.initModules()
    print ("Loaded and initialized HOPE modules.")
    rospy.spin()

if __name__ == "__main__":
    main(sys.argv)