#! /usr/bin/env python

import rospy

from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix
import csv


def gps_fused_callback(msg):
    myData = [[msg.latitude, msg.longitude]]
    with open('./fused.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(myData)

def gps_raw_callback(msg):
    myData = [[msg.latitude, msg.longitude]]
    with open('./raw.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(myData)

# def imu_callback(msg):
#     msg.yaw = msg.yaw * 180 / math.pi
#     fusionEKF.process_IMU(msg)



if __name__ == '__main__':
    rospy.init_node('ros_sub', anonymous=True)
    rospy.Subscriber('/gps/filtered', NavSatFix, gps_fused_callback)
    rospy.Subscriber('/fix', NavSatFix, gps_raw_callback)
    # rospy.Subscriber('/CustomPub', rpy, imu_callback)

    # create FusionEKF object here
    # fusionEKF = FusionEKF()
    rospy.spin()
