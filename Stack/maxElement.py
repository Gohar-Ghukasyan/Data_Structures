# find max element

from Stack import Stack


def findMaxElement(stack):
    max = stack.peek()
    stack.pop()
    for i in range(len(stack.getStack())):
        if max < stack.peek():
            max = stack.peek()
        stack.pop()
    return max


def main():
    stack = Stack()
    stack.push(0)
    stack.push(9)
    stack.push(5)
    stack.push(6)
    stack.push(1)
    print(findMaxElement(stack))


main()
