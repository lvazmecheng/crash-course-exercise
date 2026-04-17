#!/usr/bin/env python3

guests = ['Connor', 'Jack', 'Amber', 'Zac']
print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")
print(f"Dear {guests[3]}, you are invited to dinner.")
not_cooming = "Amber"
guests.remove(not_cooming)
print(f"Unfortunately, {not_cooming} cannot make it to dinner.")
new_guest = "Steph"
guests.append(new_guest)
print(f"Dear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are still invited to dinner.")
print(f"Dear {guests[2]}, you are still invited to dinner.")
print(f"Dear {guests[3]}, you are invited to dinner.")