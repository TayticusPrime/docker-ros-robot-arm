from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    pkg_share = os.path.join(os.getcwd(), 'src', 'robot_arm')
    urdf_file = os.path.join(pkg_share, 'urdf', 'arm.urdf.xacro')
    rviz_config = os.path.join(pkg_share, 'rviz', 'config.rviz')

    return LaunchDescription([
        # Publish joint states (default zeros)
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': False}]
        ),

        # Publish robot transforms from URDF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': os.popen(f'xacro {urdf_file}').read()
            }]
        ),

        # Launch RViz with config
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        )
    ])
