jahan_fav_support_champs = ['Lux', 'Seraphine', 'Sona', 'Soraka']
mia_fav_support_champs = ['Milio', 'Lulu', 'Sona', 'Soraka']

fake_list = [1, 2, 3, 4, 5]
print(2 in fake_list)
print(jahan_fav_support_champs[1])


def find_same_fav_champ():
  for fav_champs in jahan_fav_support_champs:
    if fav_champs in mia_fav_support_champs:
      print(f'Jahan and Mia both like {fav_champs}')


find_same_fav_champ()
 