def additon(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def exponent(x):
    return x ** 2

def modulus(x,y):
    return x % y

print("Select the operation : ")
print("1 : ADDITION")
print("2 : SUBTRACTION")
print("3 : MULTIPLICATION")
print("4 : DIVISION")
print("5 : EXPONENT")
print("6 : MODULUS")

while True:
    choice = input("Enter the choice of operation : 1 // 2 // 3 // 4 // 5 // 6: ")

    if choice in ('1','2','3','4','5','6'):
        num_1 = eval(input("Enter the first number : "))
        num_2 = eval(input("Enter the second number : "))

        if choice == '1':
            print(num_1,"+",num_2,"=",additon(num_1,num_2))

        elif choice == '2':
            print(num_1,"-",num_2,"=",subtraction(num_1,num_2))

        elif choice == '3':
            print(num_1,"*",num_2,"=",multiplication(num_1,num_2))

        elif choice == '4':
            print(num_1,"/",num_2,"=",division(num_1,num_2))

        elif choice == '5':
            print(num_1,"^ 2 = ",exponent(num_1))

        elif choice == '6':
            print(num_1,"%",num_2,"=",modulus(num_1,num_2))

        next_calc = input("Do you need another calculation to perform : (yes/no): ")
        if next_calc == 'no':
            break
    else:
        print("Please check and insert again !")
