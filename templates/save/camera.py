# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 10:06:53 2022

@author: Vitaly
"""

import cv2
import numpy as np


class Vitaly:

    def __init__(self, H_high=255, S_high=255, V_high=255,
                 H_low=0, S_low=0, V_low=0):

        """Filter options"""
        self.S_high = S_high
        self.H_high = H_high
        self.V_high = V_high
        self.H_low = H_low
        self.S_low = S_low
        self.V_low = V_low


        # Open video, choose the nbr change '0' to nbr of your webcam
        self.video = cv2.VideoCapture(0)
        # self.capture = cv2.VideoCapture("stream/app/static/video/app/video.mp4")



    def video_run(self):

        while (1):
            _, frame = self.video.read()
            # Не будет
            # cv2.imshow('Trackbar window', np.zeros((1, 512, 3), np.uint8))
            # ---------------------------------------------------------------

            _f = cv2.medianBlur(frame, 15)
            _f = cv2.cvtColor(_f, cv2.COLOR_BGR2HSV)  # To HSV

            # define range of color in HSV
            lower_bound = np.array([self.H_low, self.S_low, self.V_low])
            upper_bound = np.array([self.H_high, self.S_high, self.V_high])

            mask = cv2.inRange(_f, lower_bound, upper_bound)
            frame = cv2.bitwise_and(frame, frame, mask=mask)  # Comment this line if you won't show the frame later

            # Comment the one you won't need
            cv2.imshow('frame', frame)
            # cv2.imshow('mask',mask)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:  # press escape to exit
                break

        self.capture.release()  # Release the camera
        cv2.destroyAllWindows()  # Close all windows

Vitaly().video_run()