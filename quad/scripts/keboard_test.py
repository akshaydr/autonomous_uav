#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from roscopter.msg import RC
from std_msgs.msg import String
import time

channel = [1511, 1517, 1008, 1540, 1500, 2000, 1500, 1500] #Channel initial values
# channel = [1511, 1017, 1508, 2016, 1500, 2000, 1500, 1500]

data = "a"
prev_data = ""
prev_data2 = ""

def constrain (msg, low_val, high_val):
    if (msg < low_val):
        msg = 1008
    elif (msg >= high_val):
        msg = 2006
    return msg

def callback(msg):
    global data
    # rospy.loginfo(msg)
    data = msg.data
    # data = msg.linear.x
    # rospy.loginfo(data)
    # if (data != prev_data):
    #     if data > 0:
    #     else:
    #         channel[2] = constrain(channel[2] - 28)
def send_rc_val():
    global data, prev_data, prev_data2, channel
    if data != prev_data:
        if data == 'u':
            channel[2] = constrain((channel[2] + 20), 1017, 2017)
        elif data == 'j':
            channel[2] = constrain((channel[2] - 20), 1017, 2017)
        elif data == 'w':
            channel[3] = constrain((channel[3] + 20), 1063, 2016)
        elif data == 's':
            channel[3] = constrain((channel[3] - 20), 1063, 2016)
        elif data == 'a':
            channel[1] = constrain((channel[1] + 20), 1017, 2017)
        elif data == 'd':
            channel[1] = constrain((channel[1] - 20), 1017, 2017)
        elif data == 'h':
            channel[0] = constrain((channel[0] + 20), 1011, 2011)
        elif data == 'k':
            channel[0] = constrain((channel[0] - 20), 1011, 2011)
        elif data == 'o':
            channel = [1511, 1517, 1008, 1540, 1500, 2000, 1500, 1500]
        prev_data = data
    print channel

if __name__ == '__main__':
    rospy.init_node('pixhawk_arming')
    pub = rospy.Publisher('send_rc', RC, queue_size=10)
    rospy.Subscriber('key_val', String, callback)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # callback(key)
        send_rc_val()
        pub.publish(channel)
        rate.sleep()
