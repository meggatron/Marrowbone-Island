"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 8: Logic

Instructor: Meghan Thréinfhir
"""

# Use logic and other updates to finalize the game.

import random
import time


# Create a list of possible weather conditions.
weather = ["foggy", "rainy", "sunny"]

# Create an empty inventory list.
inventory = []


# Read the introduction from intro.txt.
def intro():
    with open("intro.txt", "r") as f:
        for line in f:
            print(line.strip())

    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")

    return name


# Append each location visit to log.txt.
def log_room(location):
    with open("log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")

    print(
        f"\nYou are on a {random.choice(weather)} dock. "
        "Paths lead north to a trail."
    )

    # NEW: Add a compass to the dock.
    #
    # Before asking the player where to move:
    # - check whether "compass" is not already in inventory
    # - tell the player they see a compass
    # - ask whether they want to take it
    # - append "compass" to inventory if they type "yes"
    # - otherwise, tell them they leave it behind
    #
    # Add an else statement for players who already have it.
    #
    # This should work like the map code in forest().

    move = input("Type 'north' to move. > ").lower()

    # NEW: Use the or operator so the player can type either:
    # - "north"
    # - "go north"
    #
    # Update the condition below without changing
    # what the function returns.

    if move == "north":
        return "trail"

    else:
        print("You can only type 'north' for now.")
        return "dock"


def trail():
    log_room("trail")

    print("\nYou begin walking up the trail.")

    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.5)

    # NEW: Update the description below.
    #
    # The trail should now lead:
    # - west into the forest
    # - north to the cliff
    # - south back to the dock

    print(
        f"You are on a {random.choice(weather)} trail. "
        "Paths lead west into a forest or south back to the dock."
    )

    move = input("Type 'west' or 'south'. > ").lower()

    # NEW: Use the or operator so players can type:
    # - "west" or "go west"
    # - "south" or "go south"
    #
    # Add another elif condition so players can also type:
    # - "north" or "go north"
    #
    # Moving north should return "cliff".
    #
    # Update the error message to include north.

    if move == "west":
        return "forest"

    elif move == "south":
        return "dock"

    else:
        print("Type exactly 'west' or 'south'.")
        return "trail"


def forest():
    log_room("forest")

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
        print("The forest is quiet. You've already taken the map.")

    print("You can go 'east' to return to the trail.")

    move = input("Type 'east' to return. > ").lower()

    # NEW: Use the or operator so the player can type either:
    # - "east"
    # - "go east"
    #
    # Update the condition below without changing
    # what the function returns.

    if move == "east":
        return "trail"

    else:
        print("You can only type 'east' for now.")
        return "forest"


# NEW: Create a function named cliff().
#
# The function should:
# - use global player_name
# - call log_room("cliff")
# - print a description using the player's name
#
# Inside the function, create two Boolean variables:
#
# has_map = "map" in inventory
# has_compass = "compass" in inventory
#
# Each variable will store either True or False.
#
# Use and, or, and not to decide what happens next.
#
# First condition:
# If has_map AND has_compass:
# - print the winning ending
# - congratulate the player by name
# - return "end"
#
# Second condition:
# If has_map OR has_compass:
# - tell the player they have only part of what they need
#
# Inside that section:
# - if NOT has_map, tell them to find the map in the forest
# - if NOT has_compass, tell them to find the compass at the dock
#
# Then return "trail".
#
# If neither condition is True:
# - tell the player they have neither item
# - give them the strange message about asking the shrimp
# - return "trail"


# Dictionary of location names mapped to functions.
locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest

    # NEW: Add "cliff" as a key.
    #
    # Its value should be the cliff function
    # without parentheses.
}


# Start the game.
player_name = intro()

# Keep track of where the player currently is.
current_location = "dock"


# NEW: Change the loop condition so the game continues
# only while current_location is not equal to "end".
#
# Replace while True with:
#
# while current_location != "end":
#
# Keep the dictionary lookup inside the loop.

while True:
    current_location = locations[current_location]()