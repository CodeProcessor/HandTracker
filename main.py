#!/usr/bin/env python3
"""
@Filename:    main.py
@Author:      dulanj
@Time:        2021-09-23 15.47
"""
import time

from hand_detect import HandDetector
import cv2

from hands_info import HandsInfo
from sound import Sound


def main():
    detector = HandDetector()
    sound = Sound()
    hand_movements = HandsInfo()
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        out_image, hands_info = detector.detect(image)
        cv2.imshow('MediaPipe Hands', out_image)
        char = cv2.waitKey(5)
        if char == 27:
          break

        hand_movements.detect(hands_info)
        if hand_movements.clicked_state:
            sound.click()
        print(hand_movements.clicked_state)
        time.sleep(0.02
        )


if __name__ == '__main__':
    main()