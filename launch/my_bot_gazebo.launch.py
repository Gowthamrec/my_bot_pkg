import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'my_bot_pkg'

<<<<<<< HEAD
    # Include RViz and state publisher launch
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'my_bot_rviz.launch.py')
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Launch Ignition Gazebo with a world file
    ignition_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_ign_gazebo'), 'launch', 'ign_gazebo.launch.py')
        ]),
        launch_arguments={
            'ign_args': f'{os.path.join(get_package_share_directory(package_name), "worlds", "empty.sdf")}'
        }.items()
    )

    # Explicitly add robot_state_publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'use_sim_time': True}],
        output='screen'
    )

    # Delayed spawn_entity for Ignition
    spawn_entity = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='ros_ign_gazebo',
                executable='create',
                arguments=['-topic', 'robot_description', '-name', 'my_bot'],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        rsp,
        ignition_gazebo,
        robot_state_publisher,
        spawn_entity,
    ])
=======


    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','my_bot_rviz.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

 
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')
    




    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,

    ])
>>>>>>> 53bf3c24d03ebb6d8206773d5c9483e200264f5d
