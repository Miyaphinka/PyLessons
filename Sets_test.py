daddys_fav_champs = ['Diana', 'MF', 'Seraphine', 'Lux', 'Soraka']
my_fav_champs = ['Soraka', 'Lulu', 'Nami', 'Millio', 'Sona']

daddy = set(daddys_fav_champs)
me = set(my_fav_champs)

our_champs = me - daddy
result = daddys_fav_champs + list(our_champs)
print(result)