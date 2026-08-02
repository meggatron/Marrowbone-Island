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

    # Only offer the compass if the player has not already taken it.
    if "compass" not in inventory:
        print("You see a compass resting on a post.")
        take = input("Take the compass? > ").lower()

        if take == "yes":
            inventory.append("compass")
            print("You tuck the compass into your coat.")
        else:
            print("You leave the compass resting on the post.")
    else:
        print("The post is empty. You already took the compass.")

    move = input("Where do you go? > ").lower()

    # Use or to accept two versions of the same command.
    if move == "north" or move == "go north":
        return "trail"

    else:
        print("Try typing 'north' or 'go north'.")
        return "dock"


def trail():
    log_room("trail")

    print("\nYou begin walking up the trail.")

    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.5)

    print(
        f"You are on a {random.choice(weather)} trail. "
        "Paths lead west into a forest, north to a cliff, "
        "or south back to the dock."
    )

    move = input("Where do you go? > ").lower()

    # Use or to accept two versions of each command.
    if move == "west" or move == "go west":
        return "forest"

    elif move == "south" or move == "go south":
        return "dock"

    elif move == "north" or move == "go north":
        return "cliff"

    else:
        print("Try 'west', 'north', or 'south'.")
        return "trail"


def forest():
    log_room("forest")

    print(
        f"\nYou step into a {random.choice(weather)} forest. "
        "The trees are thick and mossy."
    )

    # Only offer the map if the player has not already taken it.
    if "map" not in inventory:
        take = input("You find a crumpled old map. Take it? > ").lower()

        if take == "yes":
            inventory.append("map")
            print("You take the map and tuck it into your coat.")
        else:
            print("You leave the map in the tree hollow.")

    else:
        print("The forest is quiet. You've already taken the map.")

    move = input("Where do you go? > ").lower()

    # Use or to accept two versions of the same command.
    if move == "east" or move == "go east":
        return "trail"

    else:
        print("Try typing 'east' or 'go east'.")
        return "forest"


def cliff():
    global player_name

    log_room("cliff")

    print(f"\n{player_name}, you arrive at the edge of a steep cliff.")

    # Store the inventory checks as Boolean variables.
    has_map = "map" in inventory
    has_compass = "compass" in inventory

    # The player needs both items to win.
    if has_map and has_compass:
        print("The compass points toward the old cedar.")
        print("The map reveals a hidden path down the cliff.")
        print("Using both tools, you reach the buried treasure.")
        print(f"Congratulations, {player_name}! You win Marrowbone Island!")

        return "end"

    # If the player has at least one item, tell them what is missing.
    if has_map or has_compass:
        print("You have part of what you need, but not everything.")

        if not has_map:
            print("You still need to find the map in the forest.")

        if not has_compass:
            print("You still need to find the compass at the dock.")

        print("You return south to the trail.")

        return "trail"

    # If both Boolean variables are False, the player has neither item.
    print("You have neither the map nor the compass.")
    print("A damp note is wedged between two rocks.")
    print("'You seem to have lost your way. Ask the shrimp in the laundry room for life advice,' it reads.")
    print("You return south to the trail.")

    return "trail"


# Dictionary of location names mapped to functions.
locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest,
    "cliff": cliff
}


# Start the game.
player_name = intro()

# Keep track of where the player currently is.
current_location = "dock"


# Continue running the game until a location returns "end".
while current_location != "end":
    current_location = locations[current_location]()