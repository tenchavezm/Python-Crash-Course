# Mark Tenchavez
# 02-19-25

alien_0 = {
    'colors': 'green',
    'speed': 'slow'
}

# Brings an error
# print(alien_0['points']) 

# get() takes the first argument as a key
# The second argument is optional and will return the string
# If there is no second argument and key is not found, it will return None
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)