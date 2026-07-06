# import libraries

import time
import random

# introduction

print("You disembark from a ferry onto Marrowbone Island.")

# ask the player for their name and store it in a variable

name = input("What is your name, adventurer? > ")

# use an f-string to personalize the welcome message

print(f"Welcome, {name}. Your quest begins now...")

# create a list of possible weather conditions

possible_weather_conditions = ["sunny", "rainy", "snowy"]

# keep track of the player's current location

current_location = "dock"

# repeat the game forever

while True:

    # check if the player is at the dock

    if current_location == "dock":

        # choose random weather from the list
        print(f"You are on a {random.choice(possible_weather_conditions)} dock. Paths lead north to a trail")

        # ask the player where they want to go
        move = input("Type NORTH to move forward").lower()

        # if they typed north, update their location
        if move == "north":
            current_location = "trail"

        # otherwise, display an error message
        else:
            print("You can only print 'north' for now")

    # check if the player is on the trail
    if current_location == "trail":

        # display a short walking animation
        print("You begin walking up the trail")
        print("step 1....")
        # pause for half a second
        time.sleep(.5)  # pause for half a second
        print("step 2...")
        time.sleep(2)

        # display the trail with random weather
        print(f"You are on a {random.choice(possible_weather_conditions)} trail. You can return south to the dock")

        # ask the player where they want to go
        move = input("Type SOUTH to return").lower()

        # if they typed south, update their location
        if move == "south":
            current_location = 'dock'

        # otherwise, display an error message
        else:
            print("You can only print 'south' for now")