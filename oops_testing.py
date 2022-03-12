#Testing the  result of 2 students
#student is the class name
#check is the method created inside the class with sef as the deault attribute
#student1 and student2 are the object created from the class

class student:
    def check(self):
        if self.marks >= 80:
            return True
        else:
            return False

student1 = student()
student1.name = "Soumo"
student1.marks = 90

result = student1.check()
print("The result of Soumo is : ", result)

student2 = student()
student2.name = "Manna"
student2.marks = 60

result = student2.check()
print("The result of Manna is : ",result)

#calculating the complex numbers calculation
#complex is the name of the class
#add_calc is the name of the method
#num1 and num2 are the objects of the class complex
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add_calc(self, numbers):
        real = self.real + numbers.real
        imag = self.imag + numbers.imag
        result = complex(real,imag)
        return result

num1 = complex(5,6)
num2 = complex(-4,2)
result = num1.add_calc(num2)
print("Real data = ", result.real)
print("Imaginary data = ", result.imag)


#Getting a data of a particular student by using the Object Oriented way of writing code
class Student:
    def __init__(self, name , age, phone,subject):
        self.name = name
        self.age = age
        self.phone = phone
        self.subject = subject

    def get_data(self):
        self.name = input("Enter the name of the student : ")
        self.age = input("Enter the age of the student : ")
        self.phone = input("Enter the phone number of the student : ")
        self.subject = input("Enter the fav subject of the student :")

    def put_data(self):
        print(self.name)
        print(self.age)
        print(self.phone)
        print(self.subject)

student1 = Student("","","","")
student1.get_data()
student1.put_data()
