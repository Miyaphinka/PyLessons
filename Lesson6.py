alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

word_dictionary = {
    'clouds': 'water particles in the sky',
    'dirt': 'the stuff on the ground',
    'league': 'a stupid game',
    'numbers': [1, 2, 3, 4, 5],
    'verbs': {
        'and': 'the conjunction and',
        'or': '...',
    }
}

print(word_dictionary['league'])
print(word_dictionary['numbers'])
print(word_dictionary['verbs']['and'])

new_points = alien_0['points']
print(f'You earned {new_points} points')

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

relentless_hunter_killed_champs = {}
relentless_hunter_killed_champs['lux'] = True  # true means "killed"
relentless_hunter_killed_champs['syndra'] = True
relentless_hunter_killed_champs['qiyana'] = True

print(relentless_hunter_killed_champs.get('seraphine', 'didnt kill yet'))

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'

alien_1 = {'color': 'green', 'points': [5, 6]}
print(alien_1)
del alien_1['points'][1]
print(alien_1)

alien_2 = {'color': 'green', 'speed': 'slow'}

# always check if input exists in dictionary before accessing
input = 493224328
if input in alien_2:
  pass  # checking if input is inside

point_value = alien_2.get('points', 'no points assigned.')
print(point_value)

if 'color' in alien_2:
  print('we have a color')

# user_0 is a dictionary class
user_0 = {'username': 'miya', 'first': 'mia', 'last': 'addison'}

# items method: https://docs.python.org/3/library/stdtypes.html#typesmapping

# (username, miya)

for k, v in user_0.items():
  print(f"\nKey: {k}")
  print(f"Value: {v}")