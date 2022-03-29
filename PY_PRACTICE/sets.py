num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(num)

print(6 in num) #checking whether the number in the set or not

num.add(12) #12 is being added to the end of the set
print(num)

num.remove(9) #Removes 9 from the set
print(num)

set_a = {1, 3, 5, 7, 9}

set_b = {2, 3, 4, 5, 9}

print(set_a | set_b) #Union of two sets using the | operator

print(set_a & set_b) #Intersection of two sets using & operator

print(set_a - set_b) #Subtracting set a from set b

print(set_b - set_a) #Subtracting set b from set a

