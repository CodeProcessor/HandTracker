#!/usr/bin/env python3
"""
@Filename:    main.py
@Author:      dulanj
@Time:        2021-09-23 15.47
"""
from hand_detect import HandDetector
import cv2


def main():
    detector = HandDetector()
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        out_image, hands = detector.detect(image)
        cv2.imshow('MediaPipe Hands', out_image)
        char = cv2.waitKey(5)
        if char == 27:
          break

        if hands.areAvailable:
            print(hands)


if __name__ == '__main__':
    main()