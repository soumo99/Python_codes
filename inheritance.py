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


#-----------------------------------------------------INHERITANCE----------------------------------------------------------------------

#-----------SINGLE INHERITANCE-------------

#student is the base class from where Science_student is being inherited
#Science_student is the derived class or the sub class

class Science_student(Student):
    def science(self):
        print("This is a science method ")

x = Science_student("","","","")
x.get_data()
x.put_data()


#----------MULTIPLE INHERITANCE------------

#Class A and B is being inherited by Class C and therefore it has access to both the Classes

class A:
    def a_method(self):
        print("This is a method from class A")


class B:
    def b_method(self):
        print("This is a method from class B")


class C(A,B):
    def c_method(self):
        print("This is a method from class C")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()


#---------------MULTI-LEVEL INHERITANCE----------------

#Class B is being inherited by Class A
#Class C is being inherited by Class B and therefore it has access to both the Class A and Class B

class A:
    def a_method(self):
        print("This is a method from class A")


class B(A):
    def b_method(self):
        print("This is a method from class B")


class C(B):
    def c_method(self):
        print("This is a method from class C")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()

