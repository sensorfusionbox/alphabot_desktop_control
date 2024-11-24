
#!/bin/bash
set -e

id -u ros &>/dev/null || adduser --quiet --disabled-password --gecos '' --uid ${UID:=1000} --uid ${GID:=1000} ros

# setup ros environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
exec "$@"
