mylist = ["Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce"]

print(mylist) #Prints the whole lists

mylist2 = ["apple" , 2 , 45 , "Mango" , True , False]
print(mylist2) #Prints the whole lists with diff datatypes

index = mylist2[2]
print(index) #Returns the value at index 2

index = mylist2[2:]
print(index) #Lists slicing from index 2

index = mylist[-4]
print(index) #Returns the values of index pos -4

index = mylist2.pop() ##.remove function also works for removing the element from the list
print(index)
print(mylist2)
remove = mylist2.pop()
print(remove)
print(mylist2)

length = len(mylist)
print(length) #Prints the length of the list

if "rolls" in mylist:
    print("yes")
else:
    print("no")

if "RollsRoyce" in mylist:
    print("yes")
else:
    print("no")

mylist2.append("Berries")
print(mylist2) #Append function adds a new element to the end of the list

mylist.insert(2,"Strawberry")
print(mylist) #Insert function adds a new element at the specific mentioned index

mylist2.clear()
print(mylist2) #Clear function clears the whole list

mylist.reverse()
print(mylist) #Reverse function reverse the whole list from the end to start

mylist.sort() ##sorts the list in the alphabetical order and sorts the list in the ascending order in case of numbers
print(mylist)

sorted_list = sorted(mylist)
print(sorted_list)
print(mylist)

num_list = [0] * 5
print(num_list)

#Adding 2 lists
add_list = mylist + mylist2
print(add_list)
print(mylist)
print(mylist2)

slicing = mylist[2:6]
print(slicing) #Slicinf from index 2 to 5

#Slicing function
slicing = mylist[::2]
print(slicing)
slicing = mylist[::-1]
print(mylist)

#Different methods of copying a  list items from another list
list_cpy = mylist.copy()
print(list_cpy)
list_cpy = list(mylist)
print(list_cpy)
list_cpy = mylist[:]
print(list_cpy)

#Squaring all the list items
n_list = [1,2,3,4,5,6,7,8,9]
result = [x*x for x in n_list]
print(n_list)
print(result)

