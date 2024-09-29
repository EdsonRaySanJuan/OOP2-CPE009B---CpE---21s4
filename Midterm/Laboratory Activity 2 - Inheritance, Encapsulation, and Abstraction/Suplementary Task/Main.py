# -*- coding: utf-8 -*-
"""
        Main.py
"""

from Game import Game
from Match import single_Player, multi_Player

def main():
    game = Game()
    print("Select a mode:")
    print("1. Single player")
    print("2. Player vs Player")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        game = single_Player()
        game.play_game()
    elif choice == "2":
        game = multi_Player()
        game.play_game()
    else:
        print("Invalid choice. Exiting game.")

if __name__ == "__main__":
    main()


