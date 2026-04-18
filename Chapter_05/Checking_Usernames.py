#!/usr/bin/env python3

current_users = ['admin', 'Jack', 'Zac', 'Connor', 'Erin']
new_users = ['erin', 'Connor', 'Alice', 'Bob', 'Charlie']
lower_current_users = [user.lower() for user in current_users]
for new_user in new_users:
    status = 'Enter a new username' if new_user.lower() in lower_current_users else 'username is available'
    print(status)