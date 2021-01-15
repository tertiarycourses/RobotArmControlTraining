#!/usr/bin/env python
 
# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math
 
rospy.init_node('test_api4')
 
print "--- Start"
 
n = NiryoOne()
 
# Calibrate robot first
n.calibrate_auto()
#n.calibrate_manual()
print "Calibration finished !\n"
 
#Robot positions
saved_positions = n.get_saved_position_list()
print "\nSaved positions: "
print saved_positions
 
current_joints_array = n.get_joints()
print "\nCurrent joints: "
print current_joints_array
current_position = n.get_arm_pose()
print "\nCurrent pose: "
print current_position
 
