x = {
    1:'rob',
    2:'john',
    3:'janet',
    4:'julie',
    5:'ronny',
    6:'james'

}
print(x) #Prints the whole dictionary
print(type(x))#Prints the type of class

print(x[1]) #Prints the index 1 value

x[2] = 'Soumo' #Adds value
print(x[2]) #Prints only the mentioned value

x[7]='subrata' #Adds the value at the mentioned index i.e 7
print(x) #Prints the whole dictionary

print(len(x))

x.clear() #clears the whole dictionary

print(x)

y = {
    1:'rob',
    2:'john',
    3:'janet',
    4:'julie',
    5:'ronny',
    6:'james'

}

#-----------------LOOPS--------------
for a in y:
    print(a)

for a in y:
    print(y[a])

for a in y.values():
    print(a)

for a in y.keys():
    print(a)

for m , n in y.items():
    print(m,n)




print(y)
b = y.copy() #Makes a copy of dixtionary y and stores in b
print(b)

print(b.values()) #Shows all the values present in the dixtionary

print(b.get(2)) #Shows value at index position 2

print(y.items()) #Shows the iyems in the key value pair

print(y.keys()) #shows all the keys present in the dictionary

print(y.pop(3)) #Deletes the mentioned index from the dictionary

print(y.popitem()) #Deletes the last item from the dictionary

print(y.setdefault(2)) #shows the value of the specified key that is mentioned





#------------The values of dictionary canbe of any datatypes-----------------
new_dict = {
    "sub1":"Maths",
    "marks":90,
    "results":"Pass and got highest in class",
    "other_subs":["chemistry","english","computer","physics"]

}
print(new_dict)

new_dict["marks"] = 100
print(new_dict)#changes the value of a particular key


#----------------NESTED DICTIONARY--------------------

Exam = {
    "first_term":{
        "subject_a":"Mathematics",
        "makrs":90,
        "status_pass/fail":True

    },
    "second_term":{
        "subject_b":"Computer",
        "makrs":80,
        "status_pass/fail":True
    },
    "final_exam":{
        "subject_c":"Physics",
        "marks":45,
        "status_pass/fail":False
    }

}

print(Exam)#Prints the whole nested dictionary

print(Exam["final_exam"])#Prints the mentioned key from the dictionary along with the key and values
