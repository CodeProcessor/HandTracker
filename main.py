#!/usr/bin/env python3
"""
@Filename:    main.py
@Author:      dulanj
@Time:        2021-09-23 15.47
"""
import time

from data.drawing import Drawing
from hand_detect import HandDetector
import cv2

from hands_info import HandsInfo
from sound import Sound
from state_machine import State


def main():
    _frame_count = 0
    _draw_count = 0
    draw_click = ""
    detector = HandDetector()
    sound = Sound()
    draw = Drawing()
    hand_movements = HandsInfo()
    cap = cv2.VideoCapture(0)
    _start_time = time.time()
    _grab_time = time.time()

    while cap.isOpened():
        cap.grab()
        while time.time() - _grab_time > 0.1:
            _grab_time = time.time()
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue
            out_image, hands_info = detector.detect(image)
            _frame_count += 1
            # print(_frame_count)]
            draw.write(out_image, 10, 20, f"frame:{_frame_count}", color=(255, 255, 255))
            if _frame_count % 10 == 0:
                _time_spend = (time.time() - _start_time)
                print(f"FPS: {10/_time_spend} - {_time_spend}")
                _start_time = time.time()

            hand_movements.detect(hands_info)
            if hand_movements.click_sm.get_state() == State.transit:
                if hand_movements.click_sm.get_previous_state() == State.on:
                    sound.click()
                    draw_click = "Clack"
                    _draw_count = 3
                elif hand_movements.click_sm.get_previous_state() == State.off:
                    sound.double_click()
                    draw_click = "Click"
                    _draw_count = 3

            if draw_click == "Clack":
                if _draw_count > 0:
                    _draw_count -= 1
                    draw.write(out_image, 20, 100, f"Clack", color=(0, 0, 255), scale=2, thick=3)
            elif draw_click == "Click":
                if _draw_count > 0:
                    _draw_count -= 1
                    draw.write(out_image, 20, 100, f"Click", color=(0, 255, 0), scale=2, thick=3)

            cv2.imshow('MediaPipe Hands', out_image)
            char = cv2.waitKey(5)
            if char == 27:
                cap.release()





if __name__ == '__main__':
    main()