#creating stack

def create():
    stack = []
    return stack

#checking if the stack is empty

def check_empty(stack):
    return len(stack) == 0

#adding items to the stack

def push(stack,item):
    stack.append(item)
    print("Pushed item : ", item)

#removing an element from a stack

def pop(stack):
    if check_empty((stack)):
        return "The stack is empty"

    return stack.pop()

stack = create()

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
push(stack, str(6))

print("Popped Item : ", pop(stack))
print("Stack after popping an element : ", str(stack))






