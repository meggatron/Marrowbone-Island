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
        time.sleep(0.5)  # pause for half a second
        print("Step 2...")
        time.sleep(0.5)
        print("Step 3...")
        time.sleep(0.5)

        # choose random weather each time the trail is displayed
        print(f"You are on a {random.choice(weather)} trail. You can return south to the dock.")

        # ask where the player wants to go next
        move = input("Type 'south' to return. > ").lower()

        # if the player typed "south", move back to the dock
        if move == "south":
            current_location = 'dock'

        # otherwise, remind them of the valid choice
        else:
            print("You can only type 'south' for now.")