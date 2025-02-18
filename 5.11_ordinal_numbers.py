# Mark Tenchavez
# 02-18-25

"""
    Create a list that will indicae the position.
"""

numbers = [number for number in range(1, 10)]
ordinal_numbers = []
for number in numbers:
    if number == 1:
        ordinal_number = '1st'
        ordinal_numbers.append(ordinal_number)
    if number == 2:
        ordinal_number = '2nd'
        ordinal_numbers.append(ordinal_number)
    if number == 3:
        ordinal_number = '3rd'
        ordinal_numbers.append(ordinal_number)
    if 4 < number <= 9:
        ordinal_number = f'{number}th'
        ordinal_numbers.append(ordinal_number)

print('\n'.join(ordinal_numbers))