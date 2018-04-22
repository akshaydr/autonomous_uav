#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import sys, os
import termios, fcntl
import select
import time

key = ""
prev_key = ""

if __name__ == '__main__':
    rospy.init_node('keyboard_entry')
    pub = rospy.Publisher('key_val', String, queue_size=10)
    rate = rospy.Rate(10)

    fd = sys.stdin.fileno()
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON
    newattr[3] = newattr[3] & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldterm = termios.tcgetattr(fd)
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    print "Type some stuff"

    while not rospy.is_shutdown():
        inp, outp, err = select.select([sys.stdin], [], [])
        key = sys.stdin.read()
        # pub.publish('p')
        if key == 'q':
            break
        # print key
        pub.publish(key)
        time.sleep(0.1)
        pub.publish('p')
        rate.sleep()

    # Reset the terminal:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
