"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 8: Logic

Instructor: Meghan Thréinfhir
"""
# Marrowbone Island game updated with logic &  more

import random
import time

weather = ["foggy", "rainy", "sunny"]
inventory = []


# Read intro text from file
def intro():
    with open("intro.txt", "r") as f:
        for line in f:
            print(line.strip())
    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")
    return name


# Append each room visit to a log file
def log_room(location):
    with open("log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")
    print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")

    move = input("Where do you go? > ").lower()

    # NEW TODAY:
    # Use OR so the player can type either "north" or "go north".
    if move == "north" or move == "go north":
        return 'trail'
    else:
        print("Try typing 'north' or 'go north'.")
        return 'dock'


def trail():
    log_room("trail")
    print("\nYou begin walking up the trail.")

    # OPTIONAL TODAY:
    # Replace repeated print statements with a for loop.
    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.5)

    print(
        f"You are on a {random.choice(weather)} trail. Paths lead west into a forest, north to a cliff, or south back to the dock."
    )

    move = input("Where do you go? > ").lower()

    # NEW TODAY:
    # Use OR so players can type either:
    # "west" or "go west"
    # "north" or "go north"
    # "south" or "go south"
    if move == "west" or move == "go west":
        return 'forest'
    elif move == "north" or move == "go north":
        return 'cliff'
    elif move == "south" or move == "go south":
        return 'dock'
    else:
        print("Try 'west', 'north', or 'south'.")
        return 'trail'


def forest():
    log_room("forest")
    print(f"\nYou step into a {random.choice(weather)} forest. The trees are thick and mossy.")

    if "map" not in inventory:
        take = input("You find a crumpled old map. Type 'yes' to take it. > ").lower()

        if take == "yes":
            inventory.append("map")
            print("You take the map and tuck it into your coat.")
        else:
            print("You leave the map in the tree hollow.")
    else:
        print("The forest is quiet. You've already taken the map.")

    print("You can go east to return to the trail.")
    move = input("Where do you go? > ").lower()

    # NEW TODAY:
    # Use OR so the player can type either "east" or "go east".
    if move == "east" or move == "go east":
        return 'trail'
    else:
        print("Try typing 'east' or 'go east'.")
        return 'forest'


# NEW TODAY:
# Add a new location function: cliff()
# This is where the game can end.
def cliff():
    log_room("cliff")
    print(
        f"\nYou reach the edge of a {random.choice(weather)} cliff. "
        "A strange chest is buried here, half-covered in moss and time."
    )

    # NEW TODAY:
    # Use inventory logic to check whether the player has the map.
    if "map" in inventory:
        time.sleep(1)
        print("You study the map one last time. The X marks a hollow beneath the old cedar.")
        time.sleep(1)
        print("Digging carefully, your fingers strike metal.")
        time.sleep(1)
        print("You pull free a rusted chest. Inside: silver coins, carved stones, and a locket still warm to the touch.")
        time.sleep(1)
        print("No one will believe what you’ve found here.")
        time.sleep(1)
        print("But the island remembers.")
        time.sleep(1)
        print("Congratulations, you win Marrowbone Island!")

        # NEW TODAY:
        # Return "end" to tell the main game loop to stop.
        return 'end'

    else:
        print("The chest is here... but without the map, its meaning is lost.")
        print("You can go south to return to the trail.")

        move = input("Where do you go? > ").lower()

        if move == "south" or move == "go south":
            return 'trail'
        else:
            print("Try typing 'south' or 'go south'.")
            return 'cliff'


# Dictionary of location names mapped to functions
locations = {
    'dock': dock,
    'trail': trail,
    'forest': forest,

    # NEW TODAY:
    # Add the new cliff location here.
    'cliff': cliff
}


# Start the game
player_name = intro()
current_location = 'dock'

# NEW TODAY:
# Change the game loop so it stops when current_location is "end".
while current_location != 'end':
    current_location = locations[current_location]()