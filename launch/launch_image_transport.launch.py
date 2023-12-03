import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node



def generate_launch_description():

    # image_transport = Node(
    #     package='image_transport',
    #     executable='republish',
    #     name='image_transport',
    #     parameters=[{'in_transport': 'compressed'}, {'out_transport': 'raw'}],
    #     remappings=[('in/compressed','/camera/image_raw/compressed'), ('out','/camera/image_raw_uncompressed')]
    # )

    # ros2 run image_transport republish compressed raw --ros-args -r in/compressed:=/camera/image_raw/compressed -r out:=/camera/image_raw_uncompressed
    image_transport = ExecuteProcess(
        cmd=[[
            'ros2 run image_transport republish ',
            'compressed raw ',
            '--ros-args ',
            '-r in/compressed:=/camera/image_raw/compressed ',
            '-r out:=/camera/image_raw/uncompressed '
        ]],
        shell=True
    )

    return LaunchDescription([
        image_transport
    ])
