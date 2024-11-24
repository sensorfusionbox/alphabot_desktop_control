# alphabot_desktop_control

## Useful commands
ros2 run image_view image_view --ros-args -r image/compressed:=/left/image_raw/compressed -p image_transport:=compressed
ros2 run image_view image_view --ros-args -r image/compressed:=/right/image_raw/compressed -p image_transport:=compressed

ros2 run image_view disparity_view --ros-args -r image/:=/disparity

ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0  map camera

ros2 run image_view image_view --ros-args -r image/compressed:=/camera/image_raw/compressed -r image:=/camera/image_raw -p image_transport:=compressed

ros2 run rqt_graph rqt_graph
ros2 run tf2_tools view_frames

ros2 run teleop_twist_keyboard teleop_twist_keyboard

ros2 launch launch-display.py