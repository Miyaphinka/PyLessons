# ctrl z = undo changes
# ctrl + shift + z = redo changes

for x in range(1, 3):
  print(f"We're on time {x}")

# years_together = 0
# for x in range(1, 100):
#   print(f'mia and jahan have been together for {x} years')

# x = 1
# while True:
#   print(f"To infinity and beyond! We're getting close {x}")
#   x += 1

for x in range(1, 3):
  for y in range(1, 5):
    print(f'{x} * {y} = { x * y}')

for x in range(3):
  if x == 1:
    break
  print('loop is running')

for x in list(range(1, 3)) + list(range(5, 7)):
  print(f'meow {x}')

# for years_me_and_mia_together in range(100):
#   if years_me_and_mia_together == 50:
#     print('meow')
#   else:
#     print(years_me_and_mia_together)

string = "Hello World"
for x in string:
  print(x)

collection = ['hey', 5, 'd']
for x in collection:
  print(x)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
  for x in list:
    print(x)

for x in range(1, 20):
  if x % 2 == 0:
    print(f'{x} is even')
    continue
  print(f'current number is {x}')