# -*- coding: utf-8 -*-
"""
        Multi level inheretance
        *Archer*
"""

from Novice import Novice
import random

class Archer(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(10)
        self.setInt(10)
        self.setVit(5)
        self.setHp(self.getHp() + self.getVit())
        
    def rangeAttack(self, character):
        self.new_damage = self.getDamage() + random.randint(0, self.getInt())
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed Slash Attack! -{self.new_damage}")