# -*- coding: utf-8 -*-
"""
        Game_Mode.py
"""

from Match import single_Player, multi_Player

class Game_Mode():
    def __init__(self, select_mode):
        self.__select_mode = select_mode
    def match_start(self):
        if self.__select_mode == "Single Player":
            return single_Player()
        elif self.__select_mode == "Multi Player":
            return multi_Player()
        else:
            print("Invalid Mode!")