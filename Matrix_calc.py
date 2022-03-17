#----------------------ADDITION-----------------------

x = [[1,2,3],
     [2,3,4],
     [4,5,6]]

y = [[7,8,9],
     [4,5,6],
     [4,8,2]]

results = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range(len(x)): #Iterating through rows
     for j in range(len(x[0])): #Iterating through columns
          results[i][j] = x[i][j] + y[i][j]

for r in results:
    print(r)


#------------------MATRIX ADDITION USING NESTED LIST COMPREHENSIONS-------------------


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)

#-----------------------SUBTRACTION----------------------

x = [[1, 2, 3],
     [2, 3, 4],
     [4, 5, 6]]

y = [[7, 8, 9],
     [4, 5, 6],
     [4, 8, 2]]

results = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for i in range(len(x)):  # Iterating through rows
    for j in range(len(x[0])):  # Iterating through columns
        results[i][j] = x[i][j] - y[i][j]

for r in results:
    print(r)


#-----------------------MULTIPLICATION--------------------------

x = [[1, 2, 3],
     [2, 3, 4],
     [4, 5, 6]]

y = [[7, 8, 9],
     [4, 5, 6],
     [4, 8, 2]]

results = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for i in range(len(x)):  # Iterating through rows
    for j in range(len(x[0])):  # Iterating through columns
        results[i][j] = x[i][j] * y[i][j]

for r in results:
    print(r)

#------------------------DIVISION------------------------------

x = [[1, 2, 3],
     [2, 3, 4],
     [4, 5, 6]]

y = [[7, 8, 9],
     [4, 5, 6],
     [4, 8, 2]]

results = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for i in range(len(x)):  # Iterating through rows
    for j in range(len(x[0])):  # Iterating through columns
        results[i][j] = x[i][j] / y[i][j]

for r in results:
    print(r)



#---------------------MATRIX TRANSPOSE UISNG NESTED LOOP--------------------------


X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


#--------------------MATRIX TRANSPOSE USING NESTED LIST COMPREHENSION---------------------

x = [[1,2,3],
     [4,5,6]]

result = [[x[i][j] for j in range(len(x[0]))] for i in range(len(x))]

for r in result:
    print(r)
