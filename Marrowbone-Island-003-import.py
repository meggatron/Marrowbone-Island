#if statements
#logical operators
#for loop
#while loop
#lists
#solve a logic problem
#import external library

import random
import time

print("You disembark from a ferry onto Marrowbone Island.")
name = input("What is your name, adventurer? > ")
print(f"Welcome, {name}. Your quest begins now...")

weather = ["foggy", "rainy", "sunny"]

current_location = 'dock'

while True:
    if current_location == 'dock':
        print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")
        move = input("Type 'north' to move forward. > ").lower()
        if move == "north":
            current_location = 'trail'
        else:
            print("You can only type 'north' for now.")

    if current_location == 'trail':
        print("\nYou begin walking up the trail.")
        print("Step 1...")
        time.sleep(0.5)
        print("Step 2...")
        time.sleep(0.5)
        print("Step 3...")
        time.sleep(0.5)
        print(f"You are on a {random.choice(weather)} trail. You can return south to the dock.")
        move = input("Type 'south' to return. > ").lower()
        if move == "south":
            current_location = 'dock'
        else:
            print("You can only type 'south' for now.")
