# rover_bot
# 4 wheeled robot ROS/GAZEBO
This a simple 4 wheeled robot/rover example for those who are new to ROS or GAZEBO. The robot description is easy to understand and modify. I will go though it briefly here. The robot joints uses hardware_interface/VelocityJointInterface hardware interface and gazebo_ros_control to control the 4 wheels separately.

/urdf/materials.xacro includes color names which was not used.
/urdf/macros.xacro includes wheels descriptions also wheel joints and link wheel.
/urdf/rover.xacro contains the robots details and descriptions. The base links and position of laser and wheels.
/urdf/rover.gazebo has the plugins name.

/config/rover_control.yaml has control pid for joints to control the robot.

to run the simulation, download/clone the git, and catkin_make it:

```roslaunch rover_bot spawn.launch```

it will launch the control file as well.

to run the robot in desired position in gazebo like (1,1 or 5,4) or any run the below command, 

```~/catkin_ws/src/rover_bot/scripts $ python odo.py```

```~/catkin_ws/src/rover_bot/scripts $ python r_c_p.py```

See the r_c_p.py file and change the velocity or change the potition you want the robot to go.
Robot is configured in such way so when rotating, it rotates in the direction which will take less time to face the goal position.

Feel free to use it, update it or make suggestions.
