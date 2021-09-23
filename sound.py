#!/usr/bin/env python3
"""
@Filename:    sound.py
@Author:      dulanj
@Time:        2021-09-23 17.06
"""
from playsound import playsound


class Sound:
    def __init__(self):
        ...

    def click(self):
        playsound('data/sound/switch-8.mp3')


if __name__ == '__main__':
    sound = Sound()
    sound.click()
