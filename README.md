# Follow-bot
Husky follow bot that follows human face\


**Dependencies:**\
-ros-melodic\
-ubuntu 18.04.\
-python 2.7.\
-catkin directory\
-husky gazebo simulator\
-usb_cam ros node


**How to run program:**\
-use multiple terminal windows

**Term1:**\
Run command $roscore

**Term2:**\
-Position yourself in main catkin directory\
-Run command $source devel/setup.bash\
-Run command $roslaunch husky_gazebo husky_empty_world.launch

**Term3:**\
-Run command $rosrun usb_cam usb_cam_node _camera_name:='usb_cam' _camera_frame_id:='usb_cam'

**Term4:**\
-Position yourself in main catkin directory\
-Run command $source devel/setup.bash\
-Run command $rosrun *name of your project* camera_subscriber.py
