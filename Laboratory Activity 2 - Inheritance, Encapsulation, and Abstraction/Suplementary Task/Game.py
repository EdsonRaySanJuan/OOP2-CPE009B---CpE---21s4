# -*- coding: utf-8 -*-
"""
        Game.py
"""
from Game_Mode import Game_Mode

class Game:
    def __init__(self):
        self.modes = ["Single Player", "Multi Player"]
        self.matches = []

    def select_mode(self, mode):
        if mode not in self.modes:
            raise ValueError("Invalid game mode")
        self.current_mode = Game_Mode(mode)

    def start_new_match(self):
        match = self.current_mode.match_start()
        self.matches.append(match)
        return match