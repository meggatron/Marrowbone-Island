"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 5: algorithms

Instructor: Meghan Thréinfhir
"""
# SELECTION SORT

numbers = [5, 2, 9, 1, 3]

print("Starting list:", numbers)

# Pass 1
print("\nPass 1")
print("Looking for the smallest number.")
smallest = 0

if numbers[1] < numbers[smallest]:
    print(f"{numbers[1]} is smaller than {numbers[smallest]}.")
    smallest = 1

if numbers[2] < numbers[smallest]:
    print(f"{numbers[2]} is smaller than {numbers[smallest]}.")
    smallest = 2

if numbers[3] < numbers[smallest]:
    print(f"{numbers[3]} is smaller than {numbers[smallest]}.")
    smallest = 3

if numbers[4] < numbers[smallest]:
    print(f"{numbers[4]} is smaller than {numbers[smallest]}.")
    smallest = 4

print(f"Swapping {numbers[0]} and {numbers[smallest]}.")
numbers[0], numbers[smallest] = numbers[smallest], numbers[0]
print(numbers)

# Pass 2
print("\nPass 2")
print("Looking for the smallest remaining number.")
smallest = 1

if numbers[2] < numbers[smallest]:
    print(f"{numbers[2]} is smaller than {numbers[smallest]}.")
    smallest = 2

if numbers[3] < numbers[smallest]:
    print(f"{numbers[3]} is smaller than {numbers[smallest]}.")
    smallest = 3

if numbers[4] < numbers[smallest]:
    print(f"{numbers[4]} is smaller than {numbers[smallest]}.")
    smallest = 4

print(f"Swapping {numbers[1]} and {numbers[smallest]}.")
numbers[1], numbers[smallest] = numbers[smallest], numbers[1]
print(numbers)

# Pass 3
print("\nPass 3")
print("Looking for the smallest remaining number.")
smallest = 2

if numbers[3] < numbers[smallest]:
    print(f"{numbers[3]} is smaller than {numbers[smallest]}.")
    smallest = 3

if numbers[4] < numbers[smallest]:
    print(f"{numbers[4]} is smaller than {numbers[smallest]}.")
    smallest = 4

print(f"Swapping {numbers[2]} and {numbers[smallest]}.")
numbers[2], numbers[smallest] = numbers[smallest], numbers[2]
print(numbers)

# Pass 4
print("\nPass 4")
print("Looking for the smallest remaining number.")
smallest = 3

if numbers[4] < numbers[smallest]:
    print(f"{numbers[4]} is smaller than {numbers[smallest]}.")
    smallest = 4

print(f"Swapping {numbers[3]} and {numbers[smallest]}.")
numbers[3], numbers[smallest] = numbers[smallest], numbers[3]
print(numbers)

print("\nSorted list:", numbers)