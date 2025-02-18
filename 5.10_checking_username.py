# Mark Tenchavez
# 02-18-25

"""
    Create a program that simulates checking unique username.
"""

current_users = ['admin', 'mArK', 'ella', 'jenny', 'brian']
current_users = [current_user.lower() for current_user in current_users]
new_users = ['maRk', 'ella', 'jeg', 'karl', 'carl']

if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print(
                f'The username {user.title()} is currently in use.',
                f'Please print a new username.'
                )
        else:
            print(f'The user, {user.title()} is available.')
else:
    print(f'There are no new users.')