#! usr/bin/python3
# Imports the Random Module
import random

# Variable Setup
chosen_Weapon = input("Select Rock, Paper or Sissors:\n")
los_Machina = random.randint(1,3)

# Main Game Function
def ingame_State():
    if chosen_Weapon == "Rock":
        if los_Machina == 1:
            print("It's a tie!")
        elif los_Machina == 2:
            print("Your opponent just balled you")
        else:
            print("You've crushed your opponent to smithereens")
    elif chosen_Weapon == "Paper":
        if los_Machina == 1:
            print("You've just balled your opponent to death")
        elif los_Machina == 2:
            print("It's a tie!")
        else:
            print("You got cut tf up")
    elif chosen_Weapon == "Shotgun":
        while los_Machina in [1,2,3]:
            print("You've killed your opponent, Me && the game. Nice.")
            break
    else:
        if los_Machina == 1:
            print("Your opponent has crushed you to death")
        elif los_Machina == 2:
            print("You've just sliced your opponent up")
        else: 
            print("It's a tie!")

while chosen_Weapon not in ["Rock","Paper","Sissors","Shotgun"]:
    print("Choose a proper weapon, fool")
    break
else:
    ingame_State()
