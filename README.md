# rover_bot

This a simple 4 wheeled robot/rover example for those who are new to ROS or GAZEBO. The robot description is easy to understand and modify. I will go though it briefly here. The robot joints uses hardware_interface/VelocityJointInterface hardware interface and gazebo_ros_control to control the 4 wheels separately.

/urdf/materials.xacro includes color names which was not used.
/urdf/macros.xacro includes wheels descriptions also wheel joints and link wheel.
/urdf/rover.xacro contains the robots details and descriptions. The base links and position of laser and wheels.
/urdf/rover.gazebo has the plugins name.

/config/rover_control.yaml has control pid for joints to control the robot.

to run the simulation, download/clone the git, and catkin_make it:

```roslaunch rover_bot spawn.launch```

it will launch the control file as well.

to run controller.py, 

```~/catkin_ws/src/rover_bot/scripts $ python r_c_p.py```

See the r_c_p.py file and change the velocity or make a new one.

if you want to send velocity/data from command line, use following line to send:

```rostopic pub  /rover/right_back_wheel_controller/command std_msgs/Float64 -r 10 "data: 0.5"```

```rostopic pub  /rover/left_back_wheel_controller/command std_msgs/Float64 -r 10 "data: 0.5"```

```rostopic pub  /rover/right_front_wheel_controller/command std_msgs/Float64 -r 10 "data: 0.5"```

```rostopic pub  /rover/left_front_wheel_controller/command std_msgs/Float64 -r 10 "data: 0.5"```


Feel free to use it, update it.
