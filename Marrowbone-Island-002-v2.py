# Marrowbone Island – teaching excerpt
# Written by Meghan Thréinfhir

print("You disembark from a ferry onto Marrowbone Island.")

name = input("What is your name, adventurer? ")

age = int(input("How old are you? "))

weight = float(input("How much does your backpack weigh (use a decimal point)? "))

ready = input("Are you ready to begin your quest? (yes/no) ").lower()
is_ready = ready == "yes"

print(f"\nWelcome, {name}. You are {age} years old, carrying {weight} pounds of gear.")

if is_ready: 
    print("You take your first step toward the unknown...")
else:
    print("You hesitate at the edge of the dock. Maybe next time.")
