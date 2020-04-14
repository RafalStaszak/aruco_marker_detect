#!/usr/bin/env python

import rospy
import numpy as np
import tf
import geometry_msgs.msg
from std_msgs.msg import Float32

if __name__ == '__main__':
    rospy.init_node('show_distance')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('marker_64', 'kinect_head', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
    rate.sleep()
