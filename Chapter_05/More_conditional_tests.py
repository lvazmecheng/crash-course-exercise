#!/usr/bin/env python3

dessert = "Tiramisu"
print("Is dessert == 'Tiramisu'? I predict True.")
print(dessert == "Tiramisu")
print("\nIs dessert == 'Cheesecake'? I predict False.")
print(dessert == "Cheesecake")

favorite_fruit = "Pineapple"
print("\nIs favorite_fruit == 'pineapple'? I predict True.")
print(favorite_fruit.lower() == "pineapple")
print("\nIs favorite_fruit == 'Apple'? I predict False.")
print(favorite_fruit == "Apple")

favorite_num = 7
print("\nIs favorite_num is between 3 and 8? I predict True.")
print(3 <= favorite_num <= 8)
print("\nIs favorite_num is between 9 and 15? I predict False.")
print(9 <= favorite_num <= 15)

Passcode = 9876
print("\nIs Passcode == 9876? I predict True.")
print(Passcode == 9876)
print("\nIs Passcode == 1234? I predict False.")
print(Passcode == 1234)

attendance = 4
print("\nIs attendance is less than 6 and an even number? I predict True.")
print(attendance < 6 and attendance % 2 == 0)
print("\nIs attendance is greater than 6 and an even number? I predict False.")
print(attendance > 6 and attendance % 2 == 0)

car_brands = ["Toyota", "Honda", "Ford", "BMW", "Tesla"]
print("\nIs 'Honda' in car_brands? I predict True.")
print("Honda" in car_brands)
print("\nIs 'Mercedes' in car_brands? I predict False.")
print("Mercedes" in car_brands)

lotto_numbers = [1, 8, 17, 18, 38]
print("\nIs 15 not in lotto_numbers? I predict True.")
print(15 not in lotto_numbers)
print("\nIs 8 not in lotto_numbers? I predict False.")