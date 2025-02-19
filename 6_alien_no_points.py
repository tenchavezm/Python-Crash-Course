# Mark Tenchavez
# 02-19-25

alien_0 = {
    'colors': 'green',
    'speed': 'slow'
}

# Brings an error
# print(alien_0['points']) 

point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)