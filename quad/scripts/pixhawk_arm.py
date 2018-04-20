#!/usr/bin/env python

import rospy
from roscopter.msg import RC
import time

channel = [0, 0, 0, 0, 0, 0, 0, 0]
last_time = rospy.Time()
val = 0

if __name__ == '__main__':
    rospy.init_node('pixhawk_arming')
    pub = rospy.Publisher('send_rc', RC, queue_size=10)
    channel = [1511, 1017, 1508, 2016, 1500, 2000, 1500, 1500]
    rate = rospy.Rate(10)
    current_time = rospy.Time.now()
    last_time = current_time
    val = (current_time - last_time).to_sec()
    print(val)
    while ((current_time - last_time).to_sec() <= 3):
        print(channel)
        current_time = rospy.Time.now()
        pub.publish(channel)
        rate.sleep()
    while not rospy.is_shutdown():
        channel = [1511, 1517, 1500, 1540, 1500, 2000, 1500, 1500]
        pub.publish(channel)
        rate.sleep()
