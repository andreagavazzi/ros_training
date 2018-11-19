#!/usr/bin/env python
import rospy

if __name__ == '__main__':
  rospy.init_node('node_name')
  rospy.loginfo('Node is up')
  rate = rospy.rate(10)
  
  while not rospy.is_shutdown():
    # main code ....
    rate.sleep()
