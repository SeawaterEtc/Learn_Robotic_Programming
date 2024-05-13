#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
  rospy.init_node("run_in_circle")
  rospy.loginfo("Node have been started.")

  pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)

  rate = rospy.Rate(2)

  while not rospy.is_shutdown():
    move_cmd = Twist()
    move_cmd.linear.x = 0.6
    move_cmd.angular.z = 0.9
    pub.publish(move_cmd)
    rate.sleep()
