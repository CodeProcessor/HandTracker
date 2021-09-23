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
from state_machine import State


def main():
    _frame_count = 0
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
        _frame_count += 1
        print(_frame_count)
        cv2.imshow('MediaPipe Hands', out_image)
        char = cv2.waitKey(5)
        if char == 27:
          break

        hand_movements.detect(hands_info)
        if hand_movements.click_sm.get_state() == State.transit:
            if hand_movements.click_sm.get_previous_state() == State.on:
                sound.click()
            elif hand_movements.click_sm.get_previous_state() == State.off:
                sound.double_click()


if __name__ == '__main__':
    main()