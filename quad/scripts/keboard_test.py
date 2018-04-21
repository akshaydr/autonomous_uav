#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from roscopter.msg import RC

import time

channel = [1511, 1517, 1008, 1540, 1500, 2000, 1500, 1500] #Channel initial values
# channel = [1511, 1017, 1508, 2016, 1500, 2000, 1500, 1500]

data = 0.0
prev_data = 0.0

def constrain (msg):
    if (msg < 1008):
        msg = 1008
    elif (msg >= 2006):
        msg = 2006
    return msg

def callback(msg):
    global data, prev_data, channel
    # rospy.loginfo(msg)
    data = msg.linear.x
    rospy.loginfo(data)
    if (data != prev_data):
        if data > 0:
            channel[2] = constrain(channel[2] + 28)
        else:
            channel[2] = constrain(channel[2] - 28)



if __name__ == '__main__':
    rospy.init_node('pixhawk_arming')
    pub = rospy.Publisher('send_rc', RC, queue_size=10)
    rospy.Subscriber('key_vel', Twist, callback)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(channel)
        rate.sleep()
