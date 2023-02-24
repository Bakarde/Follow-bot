#! /usr/bin/env python
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

node = rospy.init_node("drive")
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(10)

move = Twist()
move.linear.x = 0.5
move.angular.z = 0.5

while not rospy.is_shutdown():
	pub.publish(move)
	rate.sleep()
