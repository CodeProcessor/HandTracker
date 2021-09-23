#!/usr/bin/env python3
"""
@Filename:    HandCoords.py
@Author:      dulanj
@Time:        2021-09-23 15.32
"""


class Point:
    def __init__(self, point):
        self.x = point.x
        self.y = point.y
        self.z = point.z


class Finger:
    def __init__(self, landmarks):
        self.tip = Point(landmarks[3])
        self.dip = Point(landmarks[2])
        self.pip = Point(landmarks[1])
        self.mcp = Point(landmarks[0])


class Hand:
    def __init__(self, hand_lmk):
        landmarks = hand_lmk.landmark
        self.thumb = Finger(landmarks[1:5])
        self.index = Finger(landmarks[5:9])
        self.middle = Finger(landmarks[9:13])
        self.ring = Finger(landmarks[13:17])
        self.pinky = Finger(landmarks[17:21])
        self.palm = Point(landmarks[0])


class Hands:
    def __init__(self, results):
        self.left = None
        self.right = None
        self.areAvailable = False
        if results.multi_hand_landmarks:
            for handType, handLms in zip(results.multi_handedness, results.multi_hand_landmarks):
                if handType.classification[0].label == "Right":
                    self.left = Hand(handLms)
                else:
                    self.right = Hand(handLms)
                self.areAvailable = True


if __name__ == '__main__':
    hand = Hand()
    print(hand.ring.pip)
