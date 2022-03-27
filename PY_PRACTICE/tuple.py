demo_tuple = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce")
#Prints the tuple

print(demo_tuple)

#Checks the length of the tuple using length function

print(len(demo_tuple))

#Prints the type of tuple

print(type(demo_tuple))

#Tuples can be of an datatype just like lists

tuple_data = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , 1, 2,45, 56.0, True, False )
print(tuple_data)


demo_tuple = tuple(("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce"))
print(demo_tuple)

#Returns the element of index value 4

print(demo_tuple[4])

#Returns the index value of negative index from the end

print(demo_tuple[-1])

#Tuples slicing from index 3 to 5

print(demo_tuple[3:6])

#Tuples slicing from index 0 to 4

print(demo_tuple[:5])

#Since tuples is homogeneous or immutable so the elements in a tuple is unchangeable
#so it is first changed to a list format then the values were changed and printed

x_tuple = ("name", "class" , "section", "age" , "email")
y_tuple = list(x_tuple)
y_tuple[3] = "subject"
x_tuple = tuple(y_tuple)

print(x_tuple)

#append function doesn't work since tuple are immutable so it is again converted to a list

demo_tuple = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce")
sample_tuple = list(demo_tuple)
sample_tuple.append("Porsche")
demo_tuple = tuple(sample_tuple)
print(demo_tuple)

#Adding tuple to a tuple is possible

demo_tuple = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce")
sample_tuple = ("Porsche",)
demo_tuple += sample_tuple
print(demo_tuple)

#Removing an element from a tuple after converting it to a list

demo_tuple = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce")
sample_tuple = list(demo_tuple)
sample_tuple.remove("RollsRoyce")

print(sample_tuple)

#Del keyword can delete the tuple completely

x_tuple = ("name", "class" , "section", "age" , "email")
del x_tuple
#print(x_tuple) #It is commented ot since , this tuple will raise an error since the elements in the tuple no longer exists

student = ("name","class","age", "subject")
(soumobrata,two,twelve,maths) = student
print(soumobrata)
print(12)
print(22)
print(maths)

#for Loop through a tuple
demo_tuple = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce")
for x in demo_tuple:
    print("The values are ", x)

#While loop through a tuple
demo_tuple = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce")
x=0
while x <len(demo_tuple):
    print(demo_tuple[x])
    x = x + 1

#Tuple joining
demo_tuple = ("Mercedes", "Bmw" , "Audi" , "Ferrari" , "Maruti" , "Jeep" , "Hyundai" , "RollsRoyce")
student = ("name","class","age", "subject")
total_tuple = demo_tuple + student
print(total_tuple)

#Multiplying tuple
student = ("name","class","age", "subject")
double_tuple = student * 2
print(double_tuple)