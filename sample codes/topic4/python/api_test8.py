#!/usr/bin/env python
 
# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math
 
rospy.init_node('test_api7')
 
print "--- Start"
 
n = NiryoOne()

# Deactivate learning mode
 n.activate_learning_mode(False)
 print "Learning mode deactivated? "
 print n.get_learning_mode()
 
#End effector

# Test gripper
n.change_tool(TOOL_GRIPPER_2_ID)
print "\nCurrent tool id:"
print n.get_current_tool_id()
n.close_gripper(TOOL_GRIPPER_2_ID,500)
n.wait(0.2)
n.open_gripper(TOOL_GRIPPER_2_ID,500)

# Test vacuum pump
# n.change_tool(TOOL_VACUUM_PUMP_1_ID)
# n.pull_air_vacuum_pump(TOOL_VACUUM_PUMP_1_ID)
# time.sleep(1)
# n.push_air_vacuum_pump(TOOL_VACUUM_PUMP_1_ID)

# Test electromagnet on GPIO 2
# pin = GPIO_1A
# n.change_tool(TOOL_ELECTROMAGNET_1_ID) # Mount
# n.setup_electromagnet(TOOL_ELECTROMAGNET_1_ID, pin)
# n.activate_electromagnet(TOOL_ELECTROMAGNET_1_ID, pin)
# time.sleep(2)
# n.deactivate_electromagnet(TOOL_ELECTROMAGNET_1_ID, pin)

n.change_tool(TOOL_NONE) # Unmount

# Others
print "\nHardware status: "
print n.get_hardware_status()

#Robot positions 
current_joints_array = n.get_joints()
print "\nCurrent joints: "
print current_joints_array
current_position = n.get_arm_pose()
print "\nCurrent pose: "
print current_position

# Activate learning mode
n.activate_learning_mode(True)
print "Learning mode Activated? "
print n.get_learning_mode()


