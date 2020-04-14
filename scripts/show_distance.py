#!/usr/bin/env python

import sys
import rospy
from aruco_marker_detect.srv import TfPair


def show_distance_client(x, y):
    ### write your own code here ###
    pass


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print 'Too few arguments'
        sys.exit(1)

    # print distance between tf.a and tf.b
