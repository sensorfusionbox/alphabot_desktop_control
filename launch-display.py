from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    default_rviz_config_path = '/workspaces/alphabot_desktop_control/rviz-config.rviz'
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path),
                                     description='Absolute path to rviz config file')

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    image_view_node = Node(
        package='image_view',
        executable='image_view',
        name='image_view',
        output='screen',
        remappings=[
            ('image/compressed', '/camera/image_raw/compressed'),
            ('image', '/camera/image_raw')
        ],
        parameters=[{'image_transport': 'compressed'}]
    )

    return LaunchDescription([
        rviz_arg,
        rviz_node,
        image_view_node
    ])
