#!/usr/bin/env python

import rospy
import numpy as np
import tf
from aruco_marker_detect.srv import TfPair


def distance_tf_pair(req):
    pass
    ### write your own code here ###
    ###listener = tf.TransformListener()
    ###(trans, rot) = listener.lookupTransform('tf_a', 'tf_b', rospy.Time(0))


def add_two_ints_server():
    rospy.init_node('distance_between_tfs_server')
    s = rospy.Service('distance_between_tfs', TfPair, distance_tf_pair)
    print "Ready to add two ints."
    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()
