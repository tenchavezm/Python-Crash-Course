# Mark Tenchavez
# 02-19-2025

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

# Adding a new key-value pair
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying the values of a key
alien_0 = {'color': 'green'}
print(f'The alien is {alien_0["color"]}.')

alien_0['color'] = 'yellow'
print(f'The alien is {alien_0["color"]}.')

# Tracking the position
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position: {alien_0["x_position"]}')

# Move th ealien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Fast alien
    x_increment = 3

alien_0['x_position'] += x_increment

print(f'New position: {alien_0["x_position"]}')

# Change speed value
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position: {alien_0["x_position"]}')
alien_0['speed'] = 'fast'

# Move th ealien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Fast alien
    x_increment = 3

alien_0['x_position'] += x_increment

print(f'New position: {alien_0["x_position"]}')

# Delete values
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']

print(alien_0)