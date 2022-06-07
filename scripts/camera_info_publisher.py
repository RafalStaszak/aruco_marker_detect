#!/usr/bin/env python3

import rospy
from fiducial_msgs.msg import FiducialTransformArray
from sensor_msgs.msg import CameraInfo


def create_message():
    frame_id = rospy.get_param('frame_id')
    w = rospy.get_param('image_width')
    h = rospy.get_param('image_height')
    fx = rospy.get_param('fx')
    fy = rospy.get_param('fy')
    cx = rospy.get_param('cx')
    cy = rospy.get_param('cy')

    distortion_model = rospy.get_param('distortion_model')
    distortion_coefficients = rospy.get_param('distortion_coefficients')
    distortion_coefficients = [float(x) for x in distortion_coefficients.split(' ')]

    message = CameraInfo()
    message.header.stamp = rospy.Time.now()
    message.header.frame_id = frame_id
    message.width = w
    message.height = h
    message.distortion_model = distortion_model
    message.D = distortion_coefficients

    message.K[0 * 3 + 0] = fx
    message.K[0 * 3 + 2] = cx
    message.K[1 * 3 + 1] = fy
    message.K[1 * 3 + 2] = cy
    message.K[2 * 3 + 2] = 1

    message.P[0 * 4 + 0] = fx
    message.P[0 * 4 + 2] = cx
    message.P[1 * 4 + 1] = fy
    message.P[1 * 4 + 2] = cy
    message.P[2 * 4 + 2] = 1

    message.R[0] = 1
    message.R[4] = 1
    message.R[8] = 1

    return message


if __name__ == '__main__':
    rospy.init_node('aruco_marker_detect')
    try:
        message = create_message()

        pub = rospy.Publisher('/camera_info', CameraInfo, queue_size=10)
        rate = rospy.Rate(10)  # 10hz
        while not rospy.is_shutdown():
            pub.publish(message)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
