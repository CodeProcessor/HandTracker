#!/usr/bin/env python3
"""
@Filename:    hands_info.py
@Author:      dulanj
@Time:        2021-09-23 16.19
"""
from hands import Hands


class HandsInfo:
    def __init__(self):
        self.click_thresh = 0.2
        self.clicked = False

    def detect(self, hands_info: Hands):
        if hands_info.areAvailable:
            right_hand = 1
            left_hand = 1

            if hands_info.right is not None:
                right_hand = (hands_info.right.index.tip - hands_info.right.thumb.tip)/max(hands_info.right.width, hands_info.right.height)

            if hands_info.left is not None:
                left_hand = (hands_info.left.index.tip - hands_info.left.thumb.tip)/max(hands_info.left.width, hands_info.left.height)

            min_dist = min(right_hand, left_hand)
            print(min_dist)
            self.clicked = min_dist < self.click_thresh
