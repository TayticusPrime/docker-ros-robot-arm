FROM osrf/ros:humble-desktop-full

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install common dev tools
RUN apt-get update && apt-get install -y \
    git \
    vim \
    nano \
    bash-completion \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# Install ROS 2 packages needed for the 6-DOF arm and RViz
RUN apt-get update && apt-get install -y \
    ros-humble-joint-state-publisher \
    ros-humble-joint-state-publisher-gui \
    ros-humble-robot-state-publisher \
    ros-humble-xacro \
    ros-humble-rviz2 \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init || true && rosdep update

# Set up ROS environment automatically
RUN echo "source /opt/ros/humble/setup.bash" >> /etc/bash.bashrc
