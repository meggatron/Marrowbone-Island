"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 9: Basic Game

Instructor: Meghan Thréinfhir
"""

import random
import time


# Global game data
weather = ["foggy", "rainy", "sunny"]
inventory = []


# Read the introduction from intro.txt.
def intro():
    with open("intro.txt", "r") as f:
        for line in f:
            print(line.strip())

    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")

    return name


# Record each room the player visits.
def log_room(location):
    with open("log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")

    print(
        f"\nYou are on a {random.choice(weather)} dock. "
        "Paths lead north to a trail."
    )

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

    if move == "east" or move == "go east":
        return "trail"

    else:
        print("Try typing 'east' or 'go east'.")
        return "forest"


def cliff():
    global player_name

    log_room("cliff")

    print(f"\n{player_name}, you arrive at the edge of a steep cliff.")

    # Boolean variables make the logic easier to read.
    has_map = "map" in inventory
    has_compass = "compass" in inventory

    if has_map and has_compass:
        print("The compass points toward the old cedar.")
        print("The map reveals a hidden path down the cliff.")
        print("Using both tools, you reach the buried treasure.")
        print(f"Congratulations, {player_name}! You win Marrowbone Island!")
        return "end"

    if has_map or has_compass:
        print("You have part of what you need, but not everything.")

        if not has_map:
            print("You still need to find the map in the forest.")

        if not has_compass:
            print("You still need to find the compass at the dock.")

        print("You return to the trail.")
        return "trail"

    print("You have neither the map nor the compass.")
    print("A damp note is wedged between two rocks.")
    print("'You seem to have lost your way. Ask the shrimp in the laundry room for life advice,' it reads.")
    print("You return to the trail.")

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
current_location = "dock"


# Main game loop.
while current_location != "end":
    current_location = locations[current_location]()