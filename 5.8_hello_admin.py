# Mark Tenchavez
# 02-18-25

"""
    Make a list if 5 users, including admin.
    If user == admin, create a special greeting.
    Elif user != admin, create a simple greeting
"""

users = ['admin', 'mark', 'ella', 'jenny', 'brian']

for user in users:
    if user == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in agian.')
