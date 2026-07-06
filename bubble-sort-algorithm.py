"""
Marrowbone Island
University of Washington Youth & Teen Programs

Day 5: algorithms

Instructor: Meghan Thréinfhir
"""
# BUBBLE SORT

import time

numbers = [5, 2, 9, 1, 3]

print("Starting list:", numbers)
time.sleep(1)

for i in range(len(numbers)):
    print(f"\nPass {i + 1}:")
    time.sleep(1)

    swapped = False

    for j in range(len(numbers) - 1):
        print(f" Comparing {numbers[j]} and {numbers[j + 1]}")
        time.sleep(0.5)

        if numbers[j] > numbers[j + 1]:
            print(f"  ---> Swapping {numbers[j]} and {numbers[j + 1]}")
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
        else:
            print("  No swap needed")

        print("  Current list:", numbers)
        time.sleep(0.5)

    if not swapped:
        print(" No swaps this pass - list is sorted!")
        break

print("\nSorted list:", numbers)
