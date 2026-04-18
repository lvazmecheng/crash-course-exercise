#!/usr/bin/env python3

users = ['amber', 'jack', 'admin', 'connor', 'zac']
for user in users:
    if user == 'admin':
        print(f"Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")