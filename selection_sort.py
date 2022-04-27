def selection(array,size):
    for step in range(size):
        min_index = step

        for i in range(step+1,size):
            if array[i] < array[min_index]:
                min_index = i
        (array[step] , array[min_index]) = (array[min_index], array[step])


data = [-2,45,0,11,-9]
size = len(data)
selection(data,size)
print("Sorted array in ascending order by using Selection sort ")
print(data)