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
print("Everyone! We found a bigger dinner table, so more guests can come!")
more_guests = ['Em', 'Erin', 'Alison']
guests.insert(0, more_guests[0])
guests.insert(3, more_guests[1])
guests.append(more_guests[2])
print(f"Dear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are still invited to dinner.")
print(f"Dear {guests[2]}, you are still invited to dinner.")
print(f"Dear {guests[3]}, you are still invited to dinner.")
print(f"Dear {guests[4]}, you are still invited to dinner.")
print(f"Dear {guests[5]}, you are still invited to dinner.")
print(f"Dear {guests[6]}, you are still invited to dinner.")

print(f"Sorry{guests.pop(0)}, we can only invite two people for dinner.")
print(f"Sorry{guests.pop(0)}, we can only invite two people for dinner.")
print(f"Sorry{guests.pop(0)}, we can only invite two people for dinner.")
print(f"Sorry{guests.pop(1)}, we can only invite two people for dinner.")
print(f"Sorry{guests.pop(1)}, we can only invite two people for dinner.")
print(f"Dear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are still invited to dinner.")
del guests[0]
del guests[0]
print(guests)