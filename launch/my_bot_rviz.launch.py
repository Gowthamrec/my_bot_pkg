import os
<<<<<<< HEAD

from ament_index_python.packages import get_package_share_directory

=======
from ament_index_python.packages import get_package_share_directory
>>>>>>> 53bf3c24d03ebb6d8206773d5c9483e200264f5d
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro

<<<<<<< HEAD

def generate_launch_description():

    # Check if we're told to use sim time
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('my_bot_pkg'))
    xacro_file = os.path.join(pkg_path,'urdf_file','my_bot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    
    # Create a robot_state_publisher node
=======
def generate_launch_description():


    use_sim_time = LaunchConfiguration('use_sim_time')

 
    pkg_path = os.path.join(get_package_share_directory('my_bot_pkg'))
    xacro_file = os.path.join(pkg_path, 'urdf_file', 'my_bot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)

 
>>>>>>> 53bf3c24d03ebb6d8206773d5c9483e200264f5d
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )


<<<<<<< HEAD
    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        node_robot_state_publisher
    ])
=======



    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true', 
            description='Use sim time if true'
        ),
        node_robot_state_publisher,

    ])
>>>>>>> 53bf3c24d03ebb6d8206773d5c9483e200264f5d
