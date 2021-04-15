#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import math

rospy.init_node('move')
import utils

if __name__=='__main__':

    try:
        # look down a little
        utils.move_head_tilt(-0.4)
    except:
        rospy.logerr('fail to init')
        sys.exit()

    try:
        # move position
        utils.move_arm_init()
        # move in front of the long table
        utils.move_base_goal(1, 0.5, 90)
    except:
        rospy.logerr('fail to move')
        sys.exit()

    try:
        # neutral position
        utils.move_arm_neutral()
        # open hand
        utils.move_hand(1)
        # move hand toward (we need to detect object here)
        utils.move_wholebody_ik(0.9, 1.5, 0.2, 180, 0, 90)
        # lower down the hand
        utils.move_wholebody_ik(0.9, 1.5, 0.08, 180, 0, 90)
        # close hand
        utils.move_hand(0)
        # neutral position
        utils.move_arm_neutral()
    except:
        rospy.logerr('fail to grasp')
        sys.exit()

    try:
        # move position
        utils.move_arm_init()
        # move in front of the tray
        utils.move_base_goal(1.8, -0.1, -90)
        # neutral position
        utils.move_arm_neutral()
        # open hand
        utils.move_hand(1)
    except:
        rospy.logerr('fail to move')
        sys.exit()
