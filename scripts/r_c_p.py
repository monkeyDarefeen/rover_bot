#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import time
import sys, select, termios, tty, time
class RoverControl():
    def __init__(self):
        # Publisher
        self.rate = rospy.Rate(50)
        self.right_back = rospy.Publisher("/rover/right_back_wheel_controller/command", Float64, queue_size=1)
        self.left_back = rospy.Publisher("/rover/left_back_wheel_controller/command", Float64, queue_size=1)
        self.right_front = rospy.Publisher("/rover/right_front_wheel_controller/command", Float64, queue_size=1)
        self.left_front = rospy.Publisher("/rover/left_front_wheel_controller/command", Float64, queue_size=1)

        self.mainloop()


    def stop(self):
        self.right_back.publish(0.0)
        self.left_back.publish(0.0)
        self.right_front.publish(0.0)
        self.left_front.publish(0.0)
        time.sleep(1)
    def mainloop(self):
        print("\npress \n'w' to go forward \n's' to stop \n'a' to rotate \n'd' to go backward \n'q' to exit controller")
        while not rospy.is_shutdown():
            tty.setraw(sys.stdin.fileno())
            select.select([sys.stdin], [], [], 0)
            key = sys.stdin.read(1)
            if key=="w":
                self.stop()
                self.right_back.publish(0.5)
                self.left_back.publish(0.5)
                self.right_front.publish(0.5)
                self.left_front.publish(0.5)
            elif key=="s":
                self.stop()
            elif key=="a":
                self.stop()
                self.right_back.publish(-0.5)
                self.left_back.publish(0.5)
                self.right_front.publish(-0.5)
                self.left_front.publish(0.5)
            elif key=="d":
                self.stop()
                self.right_back.publish(-0.5)
                self.left_back.publish(-0.5)
                self.right_front.publish(-0.5)
                self.left_front.publish(-0.5)
            elif key=="q":
                rospy.signal_shutdown("adf") 
                exit()
            self.rate.sleep()
            
            




if __name__ == '__main__':
    rospy.init_node("newnode")
    RoverControl()
    rospy.spin()