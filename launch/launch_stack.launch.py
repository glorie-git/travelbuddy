import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='travelbuddy' #<--- CHANGE ME

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','online_async_launch.py'
        )]), launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
    )


    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','navigation_launch.py'
        )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    # Launch joystick node
    joystick = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','joystick.launch.py'
        )])
    )

    # Republish image from compressed to raw
    image_transport = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','launch_image_transport.launch.py'
        )])
    )

    led_serial_node = Node(
        package='led_serial',
        executable='led_serial_node'
        )
    
    gesture_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','gesture.launch.py'
        )])
    )
    

    # ros2 launch travelbuddy range_filter_example.launch.py
    launch_filter = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','range_filter_example.launch.py'
        )])
    )

    launch_ball_tracker = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','ball_tracker.launch.py'
        )])
    )

    # Launch them all!
    return LaunchDescription([
        # slam,
        joystick,
        # nav2,
        image_transport,
        launch_filter,
        launch_ball_tracker,
        led_serial_node,
        gesture_node
        # minimal_timer_pub_node
    ])
