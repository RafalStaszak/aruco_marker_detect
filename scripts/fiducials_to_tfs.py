#!/usr/bin/env python3

import rospy
from fiducial_msgs.msg import FiducialTransformArray
import tf

def callback(data):
    br = tf.TransformBroadcaster()

    parent = rospy.get_param('parent', 'map')
    for x in data.transforms:
        idx = x.fiducial_id
        t = x.transform.translation
        r = x.transform.rotation
        br.sendTransform([t.x, t.y, t.z], [r.x, r.y, r.z, r.w], rospy.Time.now(), 'marker_{}'.format(idx), parent)
    pass


if __name__ == '__main__':
    rospy.init_node('fiducials_to_tfs', anonymous=True)

    try:
        rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
