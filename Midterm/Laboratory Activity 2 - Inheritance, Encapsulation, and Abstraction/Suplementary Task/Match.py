# -*- coding: utf-8 -*-
"""
        Match.py
"""

from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Novice import Novice
import random

class Match: # Base class for the game
    def __init__(self):
        self.players = [] # Stores players in the game

    def add_player(self, player):
        self.players.append(player) # Adds players to the game

    def start_game(self):
        # Implement game logic here
        pass
    
    def make_move(self, player, move): # Displays the move made by a player
        print(f"{player} made a move: {move}")

class single_Player(Match): # Inherits from Match for single-player mode.
    def __init__(self):
        super().__init__()
        self.roles = ["Swordsman", "Archer", "Magician"]
        self.players = []
        self.player_health = 100
        self.monster_health = 100
        self.player_abilities = None # Player abilities, based on role
        self.wins = 0
        self.select_roles()

    def select_roles(self): # Default starting role is "Novice"
        self.players.append("Novice")
        self.player_abilities = Novice("Novice")

    def reduceHp(self, damage): # Reduces the players health by damage amount
        self.player_abilities.reduceHp(damage)

    def play_game(self):
        self.start_game() # Starts the game 
        game_active = True # Control flow for game loop
        while game_active:
            if isinstance(self.player_abilities, Novice):
                self.play_novice_game()
                if self.wins >= 2:
                    self.upgrade_role() # Upgrade role after 2 wins
                    self.play_game_with_new_role() # Continue with the new role
            else:
                self.play_game_with_new_role() 
                
    
        
    def check_game_end(self):
        if self.monster_health <= 0: # If monster is defeated.
            print("You win!")
            self.wins += 1 # Increment win count
            print(f"You have won {self.wins} time(s)!")
            return self.play_again_after_game()  # Check if player wants to play again
    
        if self.player_abilities.getHp() <= 0: # If player is defeated
            print("You lose!")
            return self.play_again_after_game()  # Return False if player doesn't want to continue
        return True 

    def play_novice_game(self):
        print(f"\n{self.players[0]}'s turn:")
        print(f"{self.players[0]}'s health: {self.player_abilities.getHp()}")
        print(f"Monster's health: {self.monster_health}")
        print("Available moves:")
        print("1. Attack")
        print("2. Defend")
        move = input("Enter your move (1/2): ")
        if move == "1":
            novice_damage = random.randint(5, 15) # Random attack damage
            self.monster_health -= novice_damage # Reduces monster's health
            print(f"Novice attacks monster for {novice_damage} damage!")
        elif move == "2":
            print(f"{self.players[0]} defends!")
        else:
            print("Invalid move. Please try again.")
        self.make_move(self.players[0], move)

        # Monster's turn
        if self.monster_health > 0: # If monster is still alive
            print("\nMonster's turn:")
            monster_damage = random.randint(5, 10) # Monster attacks
            self.player_abilities.reduceHp(monster_damage) # Reduce player health by monsters damage
            print(f"Monster attacks {self.players[0]} for {monster_damage} damage!")
            print(f"{self.players[0]}'s health: {self.player_abilities.getHp()}")

        # Check if game is over
        if self.monster_health <= 0: # If monster is defeated
            print("You win!")
            self.wins += 1
            print(f"You have won {self.wins} time(s)!")
            self.monster_health = 100 # Reset monster health
            self.player_abilities.setHp(100) # Reset player health
        elif self.player_abilities.getHp() <= 0: # If player is defeated
            print("You lose!")
            self.monster_health = 100
            self.player_abilities.setHp(100)

    def upgrade_role(self):
        print("You have won 2 times! You can now upgrade your role.")
        print("Choose a new role:")
        for j, role in enumerate(self.roles):
            print(f"{j+1}. {role}")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            self.players[0] = "Swordsman"
            self.player_abilities = Swordsman("Swordsman") # Assigns role abilities
            self.player_abilities.setHp(100)  # Reset players health after choosing new role
        elif choice == "2":
            self.players[0] = "Archer"
            self.player_abilities = Archer("Archer")
            self.player_abilities.setHp(100)  
        elif choice == "3":
            self.players[0] = "Magician"
            self.player_abilities = Magician("Magician")
            self.player_abilities.setHp(100)  
        else:
            print("Invalid choice.")
            
    def play_game_with_new_role(self):
        while True:
            if isinstance(self.player_abilities, Swordsman):
                self.play_game_swordsman()
            elif isinstance(self.player_abilities, Archer):
                self.play_game_archer()
            elif isinstance(self.player_abilities, Magician):
                self.play_game_magician()
            else:
                break

    def play_game_swordsman(self):
        game_active = True  # This flag will control the game loop
        
        while game_active and self.monster_health > 0 and self.player_abilities.getHp() > 0:
            print(f"\n{self.players[0]}'s turn:")
            print(f"{self.players[0]}'s health: {max(self.player_abilities.getHp(), 0)}")
            print(f"Monster's health: {max(self.monster_health, 0)}")
            print("Available moves:")
            print("1. Slash Attack")
            print("2. Defend")
            move = input("Enter your move (1/2): ")
            if move == "1":
                self.player_abilities.slashAttack(self)
                damage = max(self.player_abilities.new_damage, 0)  # Ensure no negative damage
                print(f"Swordsman performed Slash Attack! Damage: {damage}")
                self.monster_health -= damage
                print(f"Swordsman attacks monster for {damage} damage!")
            elif move == "2":
                print(f"{self.players[0]} defends!")
            else:
                print("Invalid move. Please try again.")
            
            self.make_move(self.players[0], move)
    
            # Monster's turn
            if self.monster_health > 0:
                print("\nMonster's turn:")
                monster_damage = random.randint(5, 10)
                self.player_abilities.reduceHp(monster_damage)
                print(f"Monster attacks {self.players[0]} for {monster_damage} damage!")
                print(f"{self.players[0]}'s health: {self.player_abilities.getHp()}")
    
            # Check if the game is over
            game_active = self.check_game_end()  # Update game_active based on player choice
            if not game_active:  # Break the loop if player chooses not to play again
                break

    def play_game_archer(self):
        game_active = True  
    
        while game_active and self.monster_health > 0 and self.player_abilities.getHp() > 0:
            print(f"\n{self.players[0]}'s turn:")
            print(f"{self.players[0]}'s health: {max(self.player_abilities.getHp(), 0)}")
            print(f"Monster's health: {max(self.monster_health, 0)}")
            print("Available moves:")
            print("1. Range Attack")
            print("2. Defend")
            move = input("Enter your move (1/2): ")
            if move == "1":
                self.player_abilities.rangeAttack(self)
                damage = max(self.player_abilities.new_damage, 0)  # Ensure no negative damage
                print(f"Archer performed Range Attack! Damage: {damage}")
                self.monster_health -= damage
                print(f"Archer attacks monster for {damage} damage!")
            elif move == "2":
                print(f"{self.players[0]} defends!")
            else:
                print("Invalid move. Please try again.")
    
            self.make_move(self.players[0], move)
    
            if self.monster_health > 0:
                print("\nMonster's turn:")
                monster_damage = random.randint(5, 10)
                self.player_abilities.reduceHp(monster_damage)
                print(f"Monster attacks {self.players[0]} for {monster_damage} damage!")
                print(f"{self.players[0]}'s health: {self.player_abilities.getHp()}")
    
            game_active = self.check_game_end()  
            if not game_active:  
                break



    def play_game_magician(self):
        game_active = True  
    
        while game_active and self.monster_health > 0 and self.player_abilities.getHp() > 0:
            print(f"\n{self.players[0]}'s turn:")
            print(f"{self.players[0]}'s health: {max(self.player_abilities.getHp(), 0)}")
            print(f"Monster's health: {max(self.monster_health, 0)}")
            print("Available moves:")
            print("1. Magic Attack")
            print("2. Defend")
            print("3. Heal")
            move = input("Enter your move (1/2/3): ")
            if move == "1":
                self.player_abilities.magicAttack(self)
                damage = max(self.player_abilities.new_damage, 0)  # Ensure no negative damage
                print(f"Magician performed Magic Attack! Damage: {damage}")
                self.monster_health -= damage
                print(f"Magician attacks monster for {damage} damage!")
            elif move == "2":
                print(f"{self.players[0]} defends!")
            elif move == "3":
                self.player_abilities.heal()
                print(f"Magician heals for {self.player_abilities.getInt()} health!")
            else:
                print("Invalid move. Please try again.")
            
            self.make_move(self.players[0], move)
    
            if self.monster_health > 0:
                print("\nMonster's turn:")
                monster_damage = random.randint(5, 10)
                self.player_abilities.reduceHp(monster_damage)
                print(f"Monster attacks {self.players[0]} for {monster_damage} damage!")
                print(f"{self.players[0]}'s health: {self.player_abilities.getHp()}")
    
            game_active = self.check_game_end()  
            if not game_active:  
                break

    def play_again_after_game(self):
        play_again = self.play_again()
        if not play_again:
            print("Exiting the game.")
            return False  # If false game should stop
        self.monster_health = 100
        self.player_abilities.setHp(100)
        return True  # If true game should reset and player can play again


    def play_again(self):
        while True:
            play_again = input("Do you want to play another match? (yes/no): ")
            if play_again.lower() == "y":
                return True
            elif play_again.lower() == "n":
                print("Thanks for playing!")
                return False
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

    
            
class multi_Player(Match):
    def __init__(self):
        super().__init__()
        self.roles = ["Swordsman", "Archer", "Magician"]
        self.players = []
        self.player_health = [100, 100] # Health for two players
        self.player_abilities = [None, None] # Abilities for both players
        self.wins = [0, 0] # Wins for both players.

    def select_roles(self):
        self.players = []  # Clear previous players
        self.player_abilities = [None, None]  # Reset player abilities
        
        for i in range(2): # Loop for each player to choose a role
            print(f"Player {i+1}, choose a role:")
            for j, role in enumerate(self.roles):
                print(f"{j+1}. {role}")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                self.players.append("Swordsman")
                self.player_abilities[i] = Swordsman(f"Player {i+1}")
            elif choice == "2":
                self.players.append("Archer")
                self.player_abilities[i] = Archer(f"Player {i+1}")
            else:
                self.players.append("Magician")
                self.player_abilities[i] = Magician(f"Player {i+1}")

    def play_game(self):
        play_again = True
        while play_again:
            self.select_roles()  # Select new roles each time the game starts

            print("\nStarting the match!")  
            while True:
                # Randomize the turns of each player
                players = [0, 1]
                random.shuffle(players)
                for i in players:
                    print(f"\n{self.players[i]}'s turn:")
                    print(f"{self.players[i]}'s health: {self.player_abilities[i].getHp()}")
                    print("Available moves:")
                    if isinstance(self.player_abilities[i], Swordsman):
                        print("1. Slash Attack")
                        print("2. Defend")
                        move = input("Enter your move (1/2): ")
                    elif isinstance(self.player_abilities[i], Archer):
                        print("1. Range Attack")
                        print("2. Defend")
                        move = input("Enter your move (1/2): ")
                    elif isinstance(self.player_abilities[i], Magician):
                        print("1. Magic Attack")
                        print("2. Defend")
                        print("3. Heal")
                        move = input("Enter your move (1/2/3): ")

                    # Perform move based on input
                    if move == "1":
                        if isinstance(self.player_abilities[i], Swordsman):
                            self.player_abilities[i].slashAttack(self.player_abilities[(i+1)%2])
                        elif isinstance(self.player_abilities[i], Archer):
                            self.player_abilities[i].rangeAttack(self.player_abilities[(i+1)%2])
                        elif isinstance(self.player_abilities[i], Magician):
                            self.player_abilities[i].magicAttack(self.player_abilities[(i+1)%2])
                    elif move == "2":
                        print(f"{self.players[i]} defends!")
                    elif move == "3" and isinstance(self.player_abilities[i], Magician):
                        self.player_abilities[i].heal()
                    else:
                        print("Invalid move. Please try again.")

                    self.make_move(self.players[i], move)

                # Check if game is over
                if self.player_abilities[0].getHp() <= 0: # If player is 0 hp
                    print(f"{self.players[1]} wins!")
                    self.wins[1] += 1 # Increment win count
                    print(f"Current wins: {self.players[0]} - {self.wins[0]}, {self.players[1]} - {self.wins[1]}")
                    break
                elif self.player_abilities[1].getHp() <= 0:
                    print(f"{self.players[0]} wins!")
                    self.wins[0] += 1
                    print(f"Current wins: {self.players[0]} - {self.wins[0]}, {self.players[1]} - {self.wins[1]}")
                    break

            # Ask if players want to play again
            while True:
                play_again_input = input("Do you want to play another match? (yes/no): ").lower()
                if play_again_input == 'y':
                    play_again = True
                    break  # Restart the loop to select roles and start a new match
                elif play_again_input == 'n':
                    play_again = False
                    print("Thanks for playing!")
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")