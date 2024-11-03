hellos = "hello " * 10
print(hellos)
print([1, 2, 3] * 3)
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
all_numbers.sort()

jahan_fav_support_champs = ['Lux', 'Seraphine', 'Sona', 'Soraka']
mia_fav_support_champs = ['Milio', 'Lulu', 'Sona', 'Soraka']

me_and_mia_favorite_champs = jahan_fav_support_champs + mia_fav_support_champs
me_and_mia_favorite_champs.sort()
print(me_and_mia_favorite_champs)

# The target of this exercise is to create two lists called x_list and y_list, which
# contain 10 instances of the  variables x and y, respectively. You are also required
# to create a list called big_list, which contains the variables x and y, 10 times each,
# by concatenating the two lists you have created.

x = 'item 1'
y = 'item 2'

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print(f"x_list contains objects {len(x_list)}")
print(f"y_list contains objects {len(y_list)}")
print(f"big_list contains objects {len(big_list)}")


x = [1, 2, 3]
y = x

print(x == y) # Prints out True
print(x is x) # Prints out False