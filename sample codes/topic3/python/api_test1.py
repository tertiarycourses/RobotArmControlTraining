#!/usr/bin/env python
 
# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math
 
rospy.init_node('test_api')
 
print "--- Start"
 
n = NiryoOne()
 
# Move
n.set_arm_max_velocity(30)
 
joint_target = [math.radians(45), -math.pi/4.0, math.pi/4.0, 1.57/2, 0.0, 0.0]
n.move_joints(joint_target)
 
print "--- End"


#Robot positions 
current_joints_array = n.get_joints()
print "\nCurrent joints: "
print current_joints_array
current_position = n.get_arm_pose()
print "\nCurrent pose: "
print current_position
