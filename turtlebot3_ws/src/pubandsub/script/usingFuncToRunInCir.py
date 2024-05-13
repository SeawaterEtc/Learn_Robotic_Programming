#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def draw_circle():
  rospy.init_node('draw_circle_node', anonymous=True)
  pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
  rate = rospy.Rate(10)

  move_cmd = Twist()
  move_cmd.linear.x = 0.6  
  # move_cmd.angular.z = 0.9  # Positive value for counter-clockwise turn (adjust for smoothness)

  while not rospy.is_shutdown():
    pub.publish(move_cmd)
    rate.sleep()

if __name__ == '__main__':
  try:
    draw_circle()
  except rospy.ROSInterruptException:
    pass
