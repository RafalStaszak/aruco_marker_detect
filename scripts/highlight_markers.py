#!/usr/bin/env python3

import rospy
import numpy as np
from fiducial_msgs.msg import FiducialArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge



class Callbacks:
    def __init__(self):
        self.corners = None
        self.w, self.h = None, None
        self.image = None
        rospy.Subscriber("/fiducial_vertices", FiducialArray, self.vertices_callback)
        rospy.Subscriber("/kinect_head/hd/image_color", Image, self.image_callback)
        self.image_pub = rospy.Publisher('/marker_image', Image, queue_size=5)

    def vertices_callback(self, data):
        corners = list()
        for f in data.fiducials:
            x0 = f.x0
            x1 = f.x1
            x2 = f.x2
            x3 = f.x3
            y0 = f.y0
            y1 = f.y1
            y2 = f.y2
            y3 = f.y3
            corners.append([x0, y0, x1, y1, x2, y2, x3, y3])
        self.corners = corners
        print('fiducials')

    def image_callback(self, data):
        self.w = data.width
        self.h = data.height
        bridge = CvBridge()
        self.image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')

    def process(self):

        if self.corners is not None and self.image is not None:
            pass
            ### write your code here ###

            # bridge = CvBridge()
            # img_msg = bridge.cv2_to_imgmsg(new_image)
            # self.image_pub.publish(img_msg)


if __name__ == '__main__':
    rospy.init_node('highlight_markers')
    callbacks = Callbacks()
    try:
        rate = rospy.Rate(100)  # 100hz
        while not rospy.is_shutdown():
            callbacks.process()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
