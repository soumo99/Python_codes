def bubble(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

data = [-2,4,6,1,0,7,9]
bubble(data)
print("Sorted array in ascending order ")
print(data)