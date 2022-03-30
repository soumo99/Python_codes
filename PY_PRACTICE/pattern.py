#Pattern 1
n = int(input("Enter the value of n "))

for i in range(n):
    for j in range(i+1):
        print(" $ ",end=" ")

    print()

#Pattern_2
Num = int(input("Enter the value of Num : "))
for x in range(Num,0,-1):
    for y in range(Num,x,-1):
        print(end=" ")
    for m in range(0,x):
        print("* ",end=" ")
    print()

#Pattern_3
Num = int(input("Enter the value of Num : "))
for x in range(Num,0,-1):
    for y in range(Num,x,-1):
        print(end=" ")
    for m in range(0,x):
        print("* ",end=" ")
    print()
for x in range(1,Num):
    for y in range(0,Num-x-1):
        print(end=" ")
    for m in range(0, x+1):
        print("* ", end=" ")
    print()

#Pattern_4

rows = int(input("Enter the value of Num : "))
for x in range(rows+1):
    for y in range(rows):
        print(x,end=" ")
    print()

#Pattern_5
rows = int(input("Enter the value of Num : "))
for x in range(rows+1):
    for y in range(x):
        print(x,end=" ")
    print()

#Pattern_6
rows = int(input("Enter the value of Num : "))
for x in range(0,rows+1):
    for y in range(rows-x,0,-1):
        print(y,end=" ")
    print()