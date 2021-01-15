#!/usr/bin/env python
 
# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math
 
rospy.init_node('test_api9')
 
print "--- Start"

n = NiryoOne() 

''' if your robot is not calibrated, de-comment the next line ''' 
#n.calibrate_auto()

# Deactivate learning mode
 n.activate_learning_mode(False)

# Change tool 
n.change_tool(TOOL_GRIPPER_1_ID)

# move the robot to position P1
n.move_pose( -0.03, -0.156, 0.48, -0.58, -0.58, -0.145)

# open the gripper 
n.open_gripper(TOOL_GRIPPER_1_ID, 500) 
n.wait(1)

# close the gripper 
n.close_gripper(TOOL_GRIPPER_1_ID, 500)
n.wait(1)

# move the robot to position P2
n.move_pose( -0.136, -0.133, 0.255, -0.081, 0.744, -2.535)
n.wait(1)

# open the gripper 
n.open_gripper(TOOL_GRIPPER_1_ID, 500) 
n.wait(1)

#  return  to  the  initial  position  (you  can  define  yours)
n.move_pose( 0.231, -0.083, 0.417, -0.010, 0, -0.347)
n.wait(1) 

n.activate_learning_mode(True)

