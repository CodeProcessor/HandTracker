#!/usr/bin/env python3
"""
@Filename:    sound.py
@Author:      dulanj
@Time:        2021-09-23 17.06
"""
import threading

from playsound import playsound


class Sound:
    def __init__(self):
        ...

    def click(self):
        # playsound('data/sound/switch-8.mp3')
        threading.Thread(target=playsound, args=('data/sound/switch-8.mp3',), daemon=True).start()

    def double_click(self):
        # playsound('data/sound/switch-8.mp3')
        threading.Thread(target=playsound, args=('data/sound/Flash-clicks-01.wav',), daemon=True).start()


if __name__ == '__main__':
    sound = Sound()
    sound.click()
    # sound.double_click()
