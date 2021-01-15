#!/usr/bin/env python
 
# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math
 
rospy.init_node('test_api7b')
 
print "--- Start"
 
n = NiryoOne()
 
# deactivate the learning mode 
n.activate_learning_mode(False) 

for i in range(1,4) :
	# move the robot to the position P1
	n.move_pose( -0.03, -0.156, 0.48, -0.58, -0.58, -0.145)
	time.sleep(3)
	pose_actuel_1 = n.get_arm_pose() 
	print pose_actuel_1
	# move the robot to the position P2
	n.move_pose( -0.136, -0.133, 0.255, -0.081, 0.744, -2.535)
	time.sleep (3)
	pose_actuel_2 = n.get_arm_pose() 
	print pose_actuel_2

# activate the learning mode 
n.activate_learning_mode(True)

 