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

    def _play(self, sound):
        threading.Thread(target=playsound, args=(sound,), daemon=True).start()

    def click(self):
        threading.Thread(target=playsound, args=('data/sound/click.mp3',), daemon=True).start()
        # self._play('data/sound/click.mp3')

    def double_click(self):
        threading.Thread(target=playsound, args=('data/sound/click2.mp3',), daemon=True).start()
        # self._play('data/sound/double_click.wav')


if __name__ == '__main__':
    sound = Sound()
    sound.click()
    # sound.double_click()
