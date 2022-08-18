class Stack:

    # Creating a stack
    def __init__(self):
        self.stack = []

    # Creating an empty stack
    def IsEmpty(self):
        return len(self.stack) == 0

    # Adding items into the stack
    def push(self, item):
        self.stack.append(item)

    # Removing an element from the stack
    def pop(self):
        if self.IsEmpty():
            return "Stack is empty"
        return self.stack.pop()

    # Get the value of the top element without removing it
    def peek(self):
        if self.IsEmpty():
            return "Stack is empty"
        return self.stack[-1]

    # Get all stack
    def getStack(self):
        return self.stack
