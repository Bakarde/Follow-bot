#! /usr/bin/env python

import time
import rospy
from sensor_msgs.msg import Image, CompressedImage

from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
import cv2
from cv_bridge import CvBridge
from gazebo_msgs.msg import ModelStates
import os
import math
from FuzzySystem import *

PATH = os.path.dirname(__file__)
RobotPose = [0,0,0]

def GetPose(state):
	angle = state.pose[1].orientation.z
	x = state.pose[1].position.x
	y = state.pose[1].position.y
	
	global RobotPose
	RobotPose = [x,y,angle]

def DetectFaces(image):
	br = CvBridge()
	frame = br.imgmsg_to_cv2(image, "bgr8")
	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	haar_cascade = cv2.CascadeClassifier(os.path.join(PATH, "haarcascade_frontalface_default.xml"))
	faces_rect = haar_cascade.detectMultiScale(gray_img)

	height, width, depth = frame.shape #trazimo dimenzije web kamere

	global RobotPose

	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	for (x, y, w, h) in faces_rect:
		frame = cv2.rectangle(frame, (x, y), (x+w, y+h), color=(255,0,0), thickness=2)

		bb_center_x = (x + x + w)/2.0 #trazimo x koordinatu centra bounding boxa
		bb_center_y = (y + y + h)/2.0 #trazimo y koordinatu centar boundinx boxa

		img_center_x = width/2.0 #x koordinata centra slike
		img_center_y = height/2.0 #y koordinata centra slike

		povrsina = (float)(w*h)/1000
		mid_x = (x+x+w)/2

		start = time.time()	
		#conclude
		conclusion = rule_base_angular(mid_x, povrsina)
		conclusion2 = rule_base_linear(povrsina)

		linear = conclude_linear(conclusion2)
		angular = -1*conclude_angular(conclusion)

		end = time.time()

		#print("elapsed time..." + str(end-start))

		print("kutna brzina..." + str(angular))	
		print("linearna brzina... " + str(linear))

		#legal_offset = 40 #n pixelx dozvoljeno odstupanje od centra
		move = Twist()
		move.angular.z = angular
		move.linear.x = linear*math.cos(RobotPose[2]) #robot pose 2 je kut
		move.linear.y = linear*math.sin(RobotPose[2])

		pub.publish(move)
					
		
	cv2.imshow("image",frame)
    	cv2.waitKey(10)

node = rospy.init_node("face_detector")

#pokusaj dohvacanja podataka sa topica gazebo/model_states
sub_state = rospy.Subscriber('/gazebo/model_states', ModelStates, GetPose, queue_size=1, buff_size=2**24)
sub = rospy.Subscriber('/usb_cam/image_raw', Image, DetectFaces, queue_size=1, buff_size=2**24)
rospy.spin()
