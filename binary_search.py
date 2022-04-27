def binary(array , key , low , high):
    if high > low:
        mid = high - (low + high)//2

        if array[mid] == key:
            return mid

        elif array[mid] >= key:
            return binary(array,key,low,high-1)

        else:
            return binary(array,key,low+1,high)


    else:
        return -1

array = [3,4,5,6,7,8,9]
key = 6

result = binary(array,key,0,len(array)-1)

if result != -1:
    print("The element is found  and the index number is : ", result)
else:
    print("Sorry , The element is not found ")
