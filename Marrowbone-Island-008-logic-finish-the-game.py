"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 8: logic

Instructor: Meghan Thréinfhir
"""
# Use logic and other updates to finalize the game

# read
# write

import random
import time

weather = ["foggy", "rainy", "sunny"]
inventory = []


def intro():
    with open("intro.txt", "r") as f:
        for line in f:
            print(line.strip())
    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")
    return name


def log_room(location):
    with open("log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")
    print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")
    print("You see a compass resting on a post.")
    take = input("Take the compass?").lower()
    if take == "yes":
        inventory.append("compass")
        print("You tuck the compass into your coat")
    else:
        print("You might want that compass! I recommend picking it up.")

    move = input("Type 'north' to move. > ").lower()

    # TODAY:
    # Allow players to type either:
    # "north" OR "go north"

    if move == "north":
        return 'trail'

    else:
        print("You can only type 'north' for now.")
        return 'dock'


def trail():
    log_room("trail")

    print("\nYou begin walking up the trail.")
    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.5)

    print(
        f"You are on a {random.choice(weather)} trail. Paths lead west into a forest, north to a cliff, or south back to the dock."
    )

    move = input("Where do you go? > ").lower()

    # TODAY:
    # Use OR so players can type:
    # west OR go west
    # south OR go south
    # north OR go north

    if move == "west":
        return "forest"

    if move == "south":
        return "dock"

    elif move == "north":
        return "cliff"

    # TODAY:
    # Add another elif that returns "cliff"

    else:
        print("Try 'west', 'north', or 'south'.")
        return "trail"


def forest():
    log_room("forest")

    print(f"\nYou step into a {random.choice(weather)} forest.")

    if "map" not in inventory:
        take = input("Take the map? > ").lower()

        if take == "yes":
            inventory.append("map")

    else:
        print("You've already taken the map.")

    # TODAY:
    # Accept "east" OR "go east"

    move = input("Type 'east' to return to the trail.> ").lower()

    if move == "east":
        return "trail"

    else:
        return "forest"

def cliff():
    global player_name
    log_room("cliff")
    print(f"\n{player_name}, you arrive at the edge of a steep cliff.")

    if "map" in inventory and "compass" in inventory:
        print("With both tools you descend safely.")
        #Congratulations message: YOU WON

    elif "map" in inventory or "compass" in inventory:
        print("You make it down, but it's risky.")
    else:
        print("You slip on loose rock. The story ends here.")
    return "end"


# TODAY:
# Create a new cliff() function.
#
# Things to add:
# - log the room
# - describe the cliff
# - check if the player has the map
#
# if the player HAS the map:
#     print a winning ending
#     return "end"
#
# else:
#     let them return to the trail


locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest,
    "cliff": cliff

    # TODAY:
    # Add cliff here.
}


player_name = intro()
current_location = "dock"

# TODAY:
# Change this loop so the game stops
# when current_location becomes "end".

while True:
    current_location = locations[current_location]()
    if current_location == "end":
         break