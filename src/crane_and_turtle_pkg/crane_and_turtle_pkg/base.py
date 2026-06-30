#!/usr/bin/env python3

#
## base.py
#
#
#  This program defines the high-level interface for controlling the TurtleBot2 base.
#
#

import math
import time

from geometry_msgs.msg import Twist


class BaseController:

    def __init__(self, node):

        self.node = node

        self.cmd_pub = node.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        #
        # Default speeds
        #
        self.linear_speed = 0.20      # m/s
        self.angular_speed = 0.70     # rad/s

    ###################################################
    # Low-level movement
    ###################################################

    def stop(self):

        self.cmd_pub.publish(Twist())

    def drive(self, linear=0.0, angular=0.0):

        msg = Twist()

        msg.linear.x = linear
        msg.angular.z = angular

        self.cmd_pub.publish(msg)


    def forward(self, distance):

        duration = distance / self.linear_speed

        self.drive(linear=self.linear_speed)

        time.sleep(duration)

        self.stop()

    def backward(self, distance):

        duration = distance / self.linear_speed

        self.drive(linear=-self.linear_speed)

        time.sleep(duration)

        self.stop()

    def left(self, angle_deg):

        angle_rad = math.radians(angle_deg)

        duration = angle_rad / self.angular_speed

        self.drive(angular=self.angular_speed)

        time.sleep(duration)

        self.stop()

    def right(self, angle_deg):

        angle_rad = math.radians(angle_deg)

        duration = angle_rad / self.angular_speed

        self.drive(angular=-self.angular_speed)

        time.sleep(duration)

        self.stop()

    def wait(self, seconds):

        self.stop()

        time.sleep(seconds)