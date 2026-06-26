# easter egg

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
    print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail and west to a boathouse.")
    move = input("Where do you go? > ").lower()
    if move == "go north" or move == "north":
        return 'trail'
    elif move == "go west" or move == "west":
        return 'boathouse'
    else:
        print("Try typing 'go north' or 'go west'.")
        return 'dock'


def trail():
    log_room("trail")
    print("\nYou begin walking up the trail.")
    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.1)
    print(
        f"You are on a {random.choice(weather)} trail. Paths lead west into a forest, north to a cliff, or south back to the dock.")
    move = input("Where do you go? > ").lower()
    if move == "go west" or move == "west":
        return 'forest'
    elif move == "go north" or move == "north":
        return 'cliff'
    elif move == "go south" or move == "south":
        return 'dock'
    else:
        print("Try 'west', 'north', or 'south'.")
        return 'trail'


def forest():
    log_room("forest")
    print(f"\nYou step into a {random.choice(weather)} forest. The trees are thick and mossy.")
    if "map" not in inventory:
        take = input("You find a crumpled old map. Take it? (yes/no) > ").lower()
        if take == "yes":
            inventory.append("map")
            print("You take the map and tuck it into your coat.")
        else:
            print("You leave the map in the tree hollow.")
    else:
        print("The forest is quiet. You've already taken the map.")

    print("You can go east to return to the trail.")
    move = input("Where do you go? > ").lower()
    if move == "go east" or move == "east":
        return 'trail'
    else:
        print("Try typing 'east'.")
        return 'forest'


def cliff():
    log_room("cliff")
    print(
        f"\nYou reach the edge of a {random.choice(weather)} cliff. A strange chest is buried here, half-covered in moss and time.")

    if "map" in inventory:
        time.sleep(1)
        print("You study the map one last time. The X marks a hollow beneath the old cedar.")
        time.sleep(1)
        print("Digging carefully, your fingers strike metal.")
        time.sleep(1)
        print(
            "You pull free a rusted chest. Inside: silver coins, carved stones, and a locket still warm to the touch.")
        time.sleep(1)
        print("No one will believe what you’ve found here.")
        time.sleep(1)
        print("But the island remembers.")
        time.sleep(1)
        print(f"Congratulations {player_name}, you win Marrowbone Island! ")
        return 'end'
    else:
        print("The chest is here... but without the map, its meaning is lost.")
        print("You can go south to return to the trail.")
        move = input("Where do you go? > ").lower()
        if move == "go south" or move == "south":
            return 'trail'
        else:
            print("Try typing 'south'.")
            return 'cliff'


def boathouse():
    log_room("boathouse")
    print(f"\nYou enter a {random.choice(weather)} boathouse. The air smells like mildew and salt.")
    print("A broken canoe leans against the wall. In the corner, a warped door leads to a small room.")
    move = input("Do you go into the laundry room? (yes/no) > ").lower()
    if move == "yes":
        return 'laundry_room'
    else:
        print("You return to the dock.")
        return 'dock'


def laundry_room():
    log_room("laundry_room")
    print("\nYou open the warped door. Water seeps across the floor.")
    time.sleep(1)
    print("A giant shrimp—at least eight feet long—stands beside a washing machine, folding towels.")
    time.sleep(2)
    print("He turns to you, antennae twitching. 'Would you like a poem?' he asks.")
    time.sleep(1)

    choice = input("Do you give the shrimp three words? (yes/no) > ").lower()
    if choice == "yes":
        noun = input("Give the shrimp a noun > ")
        emotion = input("How do you feel today? > ")
        adjective = input("Describe the sea in one word > ")
        print("\nThe shrimp bows and recites:\n")
        time.sleep(1)
        print(f"{noun} in moonlight")
        time.sleep(1.5)
        print(f"{emotion} flows through the tidepool")
        time.sleep(1.5)
        print(f"The sea is {adjective}.")
        time.sleep(2)
    else:
        print("The shrimp nods solemnly and returns to his towels.")
        time.sleep(1)
    # lore
    print("\nAs you turn to leave, the shrimp whispers:")
    time.sleep(2)
    print('"The troll fears mirrors. The orca watches from below. The giant footprints in the grove are fresh."')
    time.sleep(3)

    print("You leave the laundry room.")
    return 'boathouse'


locations = {
    'dock': dock,
    'trail': trail,
    'forest': forest,
    'cliff': cliff,
    'boathouse': boathouse,
    'laundry_room': laundry_room
}

player_name = intro()
current_location = 'dock'

while current_location != 'end':
    current_location = locations[current_location]()
