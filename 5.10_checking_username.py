# Mark Tenchavez
# 02-18-25

"""
    Create a program that simulates checking unique username.
"""

current_users = ['admin', 'mark', 'ella', 'jenny', 'brian']
new_users = ['mark', 'ella', 'jeg', 'karl', 'carl']

if new_users:
    for user in new_users:
        if user in current_users:
            print(
                f'The username {user.title} is currently in use.'
                f'Please print a new username.'
                )
else:
    print(f'There are no new users.')