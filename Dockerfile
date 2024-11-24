
FROM osrf/ros:humble-desktop-full-jammy

RUN apt update && apt upgrade -y

RUN apt-get update && apt-get install -y \
    ros-humble-nav2-rviz-plugins \
    ros-humble-slam-toolbox

COPY ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod +x  /ros_entrypoint.sh
ENV ROS_DISTRO humble
ENV LANG en_US.UTF-8

SHELL ["/bin/bash", "-c"] 

USER $USERNAME
# terminal colors with xterm
ENV TERM xterm
RUN echo "export ROS_DOMAIN_ID=20" >> ~/.bashrc
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
CMD ["bash"]