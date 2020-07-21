#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from std_msgs.msg import Float64
import math

class r_c_p():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0 
        self.theta = 0.0
        self.sub = rospy.Subscriber("/my_odom", Odometry, self.newOdom)
        self.right_back = rospy.Publisher("/rover/right_back_wheel_controller/command", Float64, queue_size=1)
        self.left_back = rospy.Publisher("/rover/left_back_wheel_controller/command", Float64, queue_size=1)
        self.right_front = rospy.Publisher("/rover/right_front_wheel_controller/command", Float64, queue_size=1)
        self.left_front = rospy.Publisher("/rover/left_front_wheel_controller/command", Float64, queue_size=1)
        self.speed = Twist()
        self.is_rotating = False
        self.anti_clk = 0.0
        self.clk = 0.0 
        self.r = rospy.Rate(4)

        self.goal = Point()
        self.lst = [[1,1],[5,4],[3,3],[6,7],[7,7],[0,0]]
        self.main()

    def newOdom(self,msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

        rot_q = msg.pose.pose.orientation
        (roll, pitch, self.theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])


    def rotate_clockwise(self):
        self.right_back.publish(-0.5)
        self.left_back.publish(0.5)
        self.right_front.publish(-0.5)
        self.left_front.publish(0.5)

    def rotate_anti_clockwise(self):
        self.right_back.publish(0.5)
        self.left_back.publish(-0.5)
        self.right_front.publish(0.5)
        self.left_front.publish(-0.5)


    def forward(self):
        self.right_back.publish(1.5)
        self.left_back.publish(1.5)
        self.right_front.publish(1.5)
        self.left_front.publish(1.5)

    def stop(self):
        self.right_back.publish(0.0)
        self.left_back.publish(0.0)
        self.right_front.publish(0.0)
        self.left_front.publish(0.0)
    def main(self):
        while not rospy.is_shutdown():
            for x in self.lst:
                while True:
                    if abs(x[0]-self.x)<0.1 and abs(x[1]-self.y)<0.1:
                        break
                    else:
                        self.inc_x = x[0] -self.x
                        self.inc_y = x[1] -self.y
                        self.angle_to_goal = atan2(self.inc_y, self.inc_x)
                        print(self.angle_to_goal-self.theta)
                        print("goal: ",x[0],x[1])
                        print("pos : ",self.x, self.y)
                        if abs(self.angle_to_goal - self.theta) > 0.3:
                            while abs(self.angle_to_goal - self.theta)>0.1:
                                self.rotation(self.angle_to_goal,self.theta)
                        else:
                            self.forward()
                            self.is_rotating = False
                        self.r.sleep()
            self.stop()
            print("path complete!!")
            break
             
    def rotation(self,x,y):
        if self.is_rotating == False:
            self.is_rotating = True
            x = (2*math.pi + x) % 2*math.pi
            y = (2*math.pi + y) % 2*math.pi
            if x<y:
                self.anti_clk = abs(y-x)
                self.clk =  2*math.pi - self.anti_clk
            else:
                self.clk = abs(y-x)
                self.anti_clk =  2*math.pi - self.clk
        else:
            #print("clk",clk)
            #print("anti clk",anti_clk)
            if self.clk > self.anti_clk:
                self.rotate_anti_clockwise()
            else:
                self.rotate_clockwise()
            


if __name__=="__main__":
    rospy.init_node("speed_controller")
    r_c_p()
    rospy.spin()