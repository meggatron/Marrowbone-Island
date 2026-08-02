"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 7: Reading & Writing Files

Instructor: Meghan Thréinfhir
"""

import random
import time


# Create a list of possible weather conditions.
weather = ["foggy", "rainy", "sunny"]

# Create an empty inventory list.
inventory = []


# NEW: Update the intro() function so the introduction
# is read from a text file instead of printed directly.
#
# Create a file named intro.txt in the same project folder.
#
# Inside intro(), use:
# - with open()
# - "r" mode
# - a for loop
# - .strip()
#
# Delete the introduction print statement below and replace it
# with code that reads and prints each line from intro.txt.
#
# Keep the name input, welcome message, and return statement.

def intro():
    print("You disembark from a ferry onto Marrowbone Island.")

    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")

    return name


# NEW: Create a function named log_room().
#
# The function should:
# - have one parameter named location
# - open a file named log.txt
# - use append mode: "a"
# - write the location name to the file
# - include \n so each room visit appears on a new line
#
# Example:
#
# def log_room(location):
#     with open("log.txt", "a") as log:
#         log.write(f"Entered {location}\n")


def dock():

    # NEW: Call log_room() at the beginning of this function.
    #
    # Pass the name of this location as the argument.
    #
    # Example:
    # log_room("dock")

    print(
        f"\nYou are on a {random.choice(weather)} dock. "
        "Paths lead north to a trail."
    )

    move = input("Type 'north' to move. > ").lower()

    if move == "north":
        return "trail"
    else:
        print("You can only type 'north' for now.")
        return "dock"


def trail():

    # NEW: Call log_room() at the beginning of this function.
    #
    # Pass the name of this location as the argument.

    print("\nYou begin walking up the trail.")

    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.5)

    print(
        f"You are on a {random.choice(weather)} trail. "
        "Paths lead west into a forest or south back to the dock."
    )

    move = input("Type 'west' or 'south'. > ").lower()

    if move == "west":
        return "forest"
    elif move == "south":
        return "dock"
    else:
        print("Type exactly 'west' or 'south'.")
        return "trail"


def forest():

    # NEW: Call log_room() at the beginning of this function.
    #
    # Pass the name of this location as the argument.

    print(
        f"\nYou step into a {random.choice(weather)} forest. "
        "The trees are thick and mossy."
    )

    if "map" not in inventory:
        take = input(
            "You find a crumpled old map. "
            "Type 'yes' to take it. > "
        ).lower()

        if take == "yes":
            inventory.append("map")
            print("You take the map and tuck it into your coat.")
        else:
            print("You leave the map in the tree hollow.")

    else:
        print(
            "The forest is quiet. "
            "You've already taken the map."
        )

    print("You can go 'east' to return to the trail.")

    move = input("Type 'east' to return. > ").lower()

    if move == "east":
        return "trail"
    else:
        print("You can only type 'east' for now.")
        return "forest"


# Dictionary of location names mapped to functions.
locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest
}


# Start the game.
player_name = intro()

# Keep track of where the player currently is.
current_location = "dock"


# Use the locations dictionary to look up and call
# the function for the player's current location.
while True:
    current_location = locations[current_location]()