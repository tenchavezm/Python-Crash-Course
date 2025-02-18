# Mark Tenchavez
# 02-18-25

"""
    Add a conditional test to see if there's a name on the list.
    If list is empty, print a message.
"""
# This will trigger the if block
users = ['admin', 'mark', 'ella', 'jenny', 'brian']

if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user.title()}, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in agian.')
else:
    print(f'We need to find some users!')

# This will trigger the else block
users = []

if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user.title()}, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in agian.')
else:
    print(f'We need to find some users!')