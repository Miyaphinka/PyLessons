mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
# mylist = [1,2,3]
# mylist[0] = 1 ...
print(mylist[0])
print(mylist[1])
print(mylist[2])

for my_items in mylist:
  print(my_items)
mylist2 = [11,12,13]
mylist.extend(mylist2)
print(mylist)

mylist.insert(3, 4)
print(f"the lenght of my list is {len(mylist)}")
print(mylist)
