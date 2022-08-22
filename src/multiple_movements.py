#! /usr/bin/python3

import rospy
import sys
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest

rospy.init_node('service_set_joint_position_client')
rospy.wait_for_service('/goal_joint_space_path')
goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
goal_joint_space_path_request_object = SetJointPositionRequest()

# Inicio
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, 0.78, -0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Inicio...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# 1er Movimiento 
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [-0.78, -0.78, 0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Movimiento 1...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# Inicio
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, 0.78, -0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Inicio...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# 2do Movimiento 
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.78, -0.78, 0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Movimiento 2...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# Inicio
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, 0.78, -0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Inicio...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# 3er Movimiento 
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, -0.78, 0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Movimiento 3...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# Inicio
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, 0.78, -0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Inicio...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# 4to Movimiento 
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.78, -1.57, 1.57, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Movimiento 4...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(2)

# Inicio
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, 0.78, -0.78, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 1.0

rospy.loginfo("Inicio...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
