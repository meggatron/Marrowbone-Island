"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 5: Functions

Instructor: Meghan Thréinfhir
"""

import random
import time


# Create a list of possible weather conditions.
weather = ["foggy", "rainy", "sunny"]

# Create an empty inventory list.
inventory = []


# NEW: Delete the introduction code below and replace it with
# a function named intro().
#
# The function should:
# - print the introduction
# - ask the player for their name
# - print the welcome message
# - return the player's name
#
# After defining intro(), call the function and store its
# returned value in a variable named player_name.

print("You disembark from a ferry onto Marrowbone Island.")
name = input("What is your name, adventurer? > ")
print(f"Welcome, {name}. Your quest begins now...")


# Keep track of where the player currently is.
current_location = "dock"


# This loop repeats until we tell it to stop.
while True:

    # NEW: Delete the dock section below and replace it with
    # a function named dock().
    #
    # Move the dock code into the function.
    #
    # Instead of changing current_location inside the function,
    # return the name of the next location as a string.
    #
    # For example:
    # - moving north should return "trail"
    # - invalid input should return "dock"
    #
    # After defining dock(), call it from the main game loop
    # and store its returned value in current_location.

    if current_location == "dock":
        print(
            f"\nYou are on a {random.choice(weather)} dock. "
            "Paths lead north to a trail."
        )

        move = input("Type 'north' to move. > ").lower()

        if move == "north":
            current_location = "trail"
        else:
            print("You can only type 'north' for now.")


    # NEW: Repeat the same process for the trail.
    #
    # Delete the trail section below and replace it with
    # a function named trail().
    #
    # The function should return the name of the next location.

    if current_location == "trail":
        print("\nYou begin walking up the trail.")

        print("Step 1...")
        time.sleep(0.5)

        print("Step 2...")
        time.sleep(0.5)

        print("Step 3...")
        time.sleep(0.5)

        print(
            f"You are on a {random.choice(weather)} trail. "
            "You can go 'west' into a forest or "
            "'south' back to the dock."
        )

        move = input("Type 'west' or 'south'. > ").lower()

        if move == "west":
            current_location = "forest"
        elif move == "south":
            current_location = "dock"
        else:
            print("Type exactly 'west' or 'south'.")


    # NEW: Repeat the same process for the forest.
    #
    # Delete the forest section below and replace it with
    # a function named forest().
    #
    # The function can still use the inventory list.
    # It should return the name of the next location.

    if current_location == "forest":
        print(
            f"\nYou step into a {random.choice(weather)} forest. "
            "The trees are thick and quiet."
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
                "You've already taken the map. "
                "There's nothing else here."
            )

        print("\nYour inventory contains:")

        for item in inventory:
            print("-", item)

        move = input(
            "Type 'east' to return to the trail. > "
        ).lower()

        if move == "east":
            current_location = "trail"
        else:
            print("You can only type 'east' for now.")


# NEW: After creating the location functions, update the main game loop.
#
# Each part of the loop should call the function for the
# player's current location.
#
# Here is the dock example:
#
# if current_location == "dock":
#     current_location = dock()
#
# Use the same pattern to call the trail() and forest() functions.
#
# Add an else statement that prints an error message and
# uses break to end the game if the location is not recognized.