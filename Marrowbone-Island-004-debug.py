"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 4: Algorithms & Debugging

Instructor: Meghan Thréinfhir
"""

# import libraries so we can use their built-in functions
import random
import time

# introduction
print("You disembark from a ferry onto Marrowbone Island.")

# ask the player for their name and store it in a variable
name = input("What is your name, adventurer? > ")

# use an f-string to personalize the welcome message
print(f"Welcome, {name}. Your quest begins now...")

# create a list of possible weather conditions
weather = ["foggy", "rainy", "sunny"]

# NEW: create an empty inventory list

# keep track of where the player currently is
current_location = 'dock'

# this loop repeats forever until we tell it to stop
while True:

    # check whether the player is currently at the dock
    if current_location == 'dock':

        # random.choice() picks one weather condition from the list
        print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")

        # get the player's choice and convert it to lowercase
        move = input("Type 'north' to move forward. > ").lower()

        # if the player typed "north", update their location
        if move == "north":
            current_location = 'trail'

        # otherwise, display an error message
        else:
            print("You can only type 'north' for now.")

    # check whether the player is now on the trail
    if current_location == 'trail':

        # display a short walking animation
        print("\nYou begin walking up the trail.")
        print("Step 1...")
        time.sleep(0.5)
        print("Step 2...")
        time.sleep(0.5)
        print("Step 3...")
        time.sleep(0.5)

        # choose random weather each time the trail is displayed
        print(f"You are on a {random.choice(weather)} trail. You can return south to the dock.")

        # ask where the player wants to go next
        move = input("Type 'south' to return. > ").lower()

        # NEW: allow the player to travel west into a forest

        # if the player typed "south", move back to the dock
        if move == "south":
            current_location = 'dock'

        # otherwise, remind them of the valid choice
        else:
            print("You can only type 'south' for now.")

    # NEW: create a forest location

        # NEW: check whether the player already has the map

            # NEW: ask whether the player wants to take the map

                # NEW: add the map to the inventory

        # NEW: display every item in the inventory using a for loop

        # NEW: allow the player to return to the trail