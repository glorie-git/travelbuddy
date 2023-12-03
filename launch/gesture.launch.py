from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition

# import os
# from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    image_topic = LaunchConfiguration('image_topic')
    image_topic_dec = DeclareLaunchArgument(
        'image_topic',
        default_value='/camera/image_raw/uncompressed',
        description='The name of the input image topic.')


    gesture_recognizer_node = Node(
            package='gesture_recognizer',
            executable='gesture_recognizer_node',
            remappings=[('/image_in',image_topic)],
         )

    return LaunchDescription([
        image_topic_dec,
        gesture_recognizer_node,  
    ])