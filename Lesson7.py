favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language_names = favorite_languages.keys()

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favourite language is {language.title()}.")

for name in favorite_languages:
  print(name.title())

# \t = insert tab
# \n = insert newline

friends = ['jen', 'sarah']
for name in favorite_languages:
  print(f'Hi {name.title()}.')
  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
  print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
  print(language.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
  print(alien)

# data structure = "structure of data"
# such as list, dictionaries, sets, and mixes

champ_1 = {
    'name': 'lux',
    'level': 15,
    'stats': {
        'ap': 435,
        'as': 0.221,
    },
    'items': ['doran ring', 'luden', 'shadowflame', 'rod of ages'],
    # rune stats, item stats, ad, }
}

champ_2 = {'name': 'sera', 'level': 10, 'items': []}
champ_3 = {'name': 'mf', 'level': 9, 'items': []}

champions = [champ_1, champ_2, champ_3]

# champions['lux']['runes']['stats']['dark_harvest']

print(f"Lux's ap at minute 15 is {champions[0]['stats']['ap']}")

print(f"Lux's first item is {champions[0]['items'][0]}")

aliens = []
for alien_number in range(10):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)
  # slicing https://www.shecodes.io/athena/40619-how-to-get-the-last-two-indices-in-a-python-list 
for alien in aliens[-3:]:
  print(alien)

print(f"\nTotal number of aliens: {len(aliens)}")

my_str = "Hello I love you mia"
print(my_str[-3:]) # "mia"

for champ in champions:
  if 'shadowflame' in champ['items']:
    champ['stats']['ap'] += 300
  if 'rod of ages' in champ['items']:
    # same as doing += like above
    champ['level'] = champ['level'] + 1

print(champions)
    