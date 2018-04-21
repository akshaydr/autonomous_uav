#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

channel = [0, 0, 0, 0, 0, 0, 0, 0]

throttle = 0

def callback(msg):
    global channel
    throttle = data.linear.x *

if __name__ == '__main__':
    rospy.init_node('pixhawk_arming')
    pub = rospy.Publisher('send_rc', RC, queue_size=10)
    rospy.Subscriber('cmd_vel', Twist, callback)
    channel = [1511, 1017, 1508, 2016, 1500, 2000, 1500, 1500]
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        channel = [1511, 1517, 1500, 1540, 1500, 2000, 1500, 1500]
        pub.publish(channel)
        rate.sleep()
