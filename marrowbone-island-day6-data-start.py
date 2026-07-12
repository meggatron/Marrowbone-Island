"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 6: Dictionaries

Instructor: Meghan Thréinfhir
"""

# Start without dictionary class 6

import random
import time

weather = ["foggy", "rainy", "sunny"]
inventory = []

def intro():
    print("You disembark from a ferry onto Marrowbone Island.")
    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")
    return name

def dock():
    print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")

    move = input("Type 'north' to move. > ").lower()

    if move == "north":
        return "trail"
    else:
        print("You can only type 'north' for now.")
        return "dock"

def trail():
    print("\nYou begin walking up the trail.")
    print("Step 1...")
    time.sleep(0.5)
    print("Step 2...")
    time.sleep(0.5)
    print("Step 3...")
    time.sleep(0.5)

    print(f"You are on a {random.choice(weather)} trail. Paths lead west into a forest or south back to the dock.")

    move = input("Type 'west' or 'south'. > ").lower()

    if move == "west":
        return "forest"
    elif move == "south":
        return "dock"
    else:
        print("Type exactly 'west' or 'south'.")
        return "trail"

def forest()

def tidepools()

# New Dictionary for location names to map to functions
# dock refers to the function dock() calls the function
locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest,
    "tidepools": tidepools
}

# Start game
player_name = intro()
current_location = "dock"

# Main game loop
while True:
   current_location = locations[current_location]()

