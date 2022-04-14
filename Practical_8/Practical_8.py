# 20CS010 - Meet Butani
# Write a Program in Python to implement a Stack Data Structure using
# Class and Objects, with push, pop, and traversal method.
# -------------------------------------------------------------------


# creating a class named 'Stack'
class Stack:
    # Creating an empty stack
    def create_stack():
        stack = []
        return stack

    # Adding/pushing the items into the stack
    def push(stack, item):
        stack.append(item)
        print("Pushed item: " + item)

    # Removing/popping an element from the stack
    def pop(stack):
        if (len(stack) == 0):
            return "Stack is empty"

        return stack.pop()


    # creating a stack and pushing the elements into it
    stack = create_stack()
    push(stack, str(2))
    push(stack, str(4))
    push(stack, str(6))
    push(stack, str(8))

    # printing the contents of the stack
    print("Contents of stack: " + str(stack))

    # popping an element from the stack
    print("Popped item: " + pop(stack))

    # printing the updated stack
    print("Stack after popping an element: " + str(stack))

