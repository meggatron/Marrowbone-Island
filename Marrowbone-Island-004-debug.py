#algorithms
#debugging

import random
import time

print("You disembark from a ferry onto Marrowbone Island.")
name = input("What is your name, adventurer? > ")
print(f"Welcome, {name}. Your quest begins now...")

weather = ["foggy", "rainy", "sunny"]
inventory = []
current_location = 'dock'

while True:
    if current_location == 'dock':
        print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")
        move = input("Type 'north' to move. > ").lower()
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
        print(f"You are on a {random.choice(weather)} trail. You can go 'west' into a forest or 'south' back to the dock.")
        move = input("Type 'west' or 'south'. > ").lower()
        if move == "west":
            current_location = 'forest'
        elif move == "south":
            current_location = 'dock'
        else:
            print("Type exactly 'west' or 'south'.")

    if current_location == 'forest':
        print(f"\nYou step into a {random.choice(weather)} forest. The trees are thick and quiet.")
        if "map" not in inventory:
            take = input("You find a crumpled old map. Type 'yes' to take it. > ").lower()
            if take == "yes":
                inventory.append("map")
                print("You take the map and tuck it into your coat.")
            else:
                print("You leave the map in the tree hollow.")
        else:
            print("You've already taken the map. There's nothing else here.")

        print("\nYour inventory contains:")
        for item in inventory:
            print("-", item)

        move = input("Type 'east' to return to the trail. > ").lower()
        if move == "east":
            current_location = 'trail'
        else:
            print("You can only type 'east' for now.")
