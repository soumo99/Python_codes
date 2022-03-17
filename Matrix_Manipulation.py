import numpy

x = numpy.array([[1,2],[4,6]])
y = numpy.array([[2,4],[6,8]])

print("Addition of 2 matrices : ")
print(numpy.add(x,y))

print("Subtraction of 2 matrices : ")
print(numpy.subtract(x,y))

print("Multiplication of 2 matrices : ")
print(numpy.multiply(x,y))

print("Division of 2 matrices : ")
print(numpy.divide(x,y))

print("Product of  of 2 matrices : ")
print(numpy.dot(x,y))

print("Addition of 2 matrices : ")
print(numpy.sqrt(x))

print("Summation of elements : ")
print(numpy.sum(y))

print("Row wise Summation : ")
print(numpy.sum(y,axis=1))

print("Column wise summation : ")
print(numpy.sum(y,axis=0))

print("Matrix Transpose : ")
print(x.T)

