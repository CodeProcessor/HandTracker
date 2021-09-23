#!/usr/bin/env python3
"""
@Filename:    drawing.py
@Author:      dulanj
@Time:        2021-09-23 20.08
"""
import cv2


class Drawing:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def write(self, image, x, y, text, color, scale=0.5, thick=None):
        cv2.putText(image, text, org=(x,y), fontFace=self.font, fontScale=scale, color=color, thickness=thick)
