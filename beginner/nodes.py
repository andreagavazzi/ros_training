#!/usr/bin/env python             # Sempre necessario
import rospy                      # Importa le librerie ROS

if __name__ == '__main__':
  rospy.init_node('node_name')    # Inizializza il nodo
  rospy.loginfo('Node is up')     # Comunica al log che il nodo è partito
  
  rate = rospy.rate(10)
  
  while not rospy.is_shutdown():
    # main code ....
    rate.sleep()
