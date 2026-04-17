#!/usr/bin/env python3

numbers = list(range(1, 11))
for number in numbers:
    cube = number ** 3
    print(cube)
print(f"\nThe first three items in the list are: {numbers[:3]}")
print(f"The middle three items in the list are: {numbers[4:7]}")
print(f"The last three items in the list are: {numbers[-3:]}")