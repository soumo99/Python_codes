mylist = ["Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce"]

print(mylist)

mylist2 = ["apple" , 2 , 45 , "Mango" , True , False]
print(mylist2)

index = mylist2[2]
print(index)

index = mylist2[2:]
print(index)

index = mylist[-4]
print(index)

index = mylist2.pop() ##.remove function also works for removing the element from the list
print(index)
print(mylist2)
remove = mylist2.pop()
print(remove)
print(mylist2)

length = len(mylist)
print(length)

if "rolls" in mylist:
    print("yes")
else:
    print("no")

if "RollsRoyce" in mylist:
    print("yes")
else:
    print("no")

mylist2.append("Berries")
print(mylist2)

mylist.insert(2,"Strawberry")
print(mylist)

mylist2.clear()
print(mylist2)

mylist.reverse()
print(mylist)

mylist.sort() ##sorts the list in the alphabetical order and sorts the list in the ascending order in case of numbers
print(mylist)

sorted_list = sorted(mylist)
print(sorted_list)
print(mylist)

num_list = [0] * 5
print(num_list)

add_list = mylist + mylist2
print(add_list)
print(mylist)
print(mylist2)

slicing = mylist[2:6]
print(slicing)

slicing = mylist[::2]
print(slicing)
slicing = mylist[::-1]
print(mylist)

list_cpy = mylist.copy()
print(list_cpy)
list_cpy = list(mylist)
print(list_cpy)
list_cpy = mylist[:]
print(list_cpy)

n_list = [1,2,3,4,5,6,7,8,9]
result = [x*x for x in n_list]
print(n_list)
print(result)