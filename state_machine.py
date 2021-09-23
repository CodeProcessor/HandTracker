#!/usr/bin/env python3
"""
@Filename:    state_machine.py
@Author:      dulanj
@Time:        2021-09-23 18.51
"""
import enum


class State(enum.Enum):
    off = 0
    on = 1
    none = 2
    transit = 3


class StateMachine:
    def __init__(self, on_thresh, off_thresh):
        self._on_thresh = on_thresh
        self._off_thresh = off_thresh
        self._on_count = 0
        self._off_count = 0

        self._temp_state = State.none
        self._previous_state = State.none
        self._state = State.none

    def __str__(self):
        return f"ON:{self._on_count} OFF:{self._off_count} PRE:{self._previous_state} STATE:{self._state}"

    def get_state(self):
        return self._state

    def get_previous_state(self):
        return self._previous_state

    def update(self, switch):
        if switch:
            self._on_count += 1
            self._off_count = 0
        else:
            self._off_count += 1
            self._on_count = 0

        if self._state == State.transit:
            self._state = self._temp_state

        if self._temp_state != State.on and self._on_count > self._on_thresh:
            self._previous_state = self._state
            self._state = State.transit
            self._temp_state = State.on
            self._on_count = 0

        if self._temp_state != State.off and self._off_count > self._off_thresh:
            self._previous_state = self._state
            self._state = State.transit
            self._temp_state = State.off
            self._off_count = 0


if __name__ == '__main__':
    sm1 = StateMachine(on_thresh=3, off_thresh=3)

    for i in range(20):
        sm1.update(i < 10)
        print(sm1)
        # print(sm1.get_state())
