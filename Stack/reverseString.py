# reverse string

from Stack import Stack


def reverseString(stack, string):
    for s in string:
        stack.push(s)

    str = ""
    for i in range(len(stack.getStack())):
        str += stack.peek()
        stack.pop()

    return str


def main():
    stack = Stack()
    string = "Hello world!"
    print(reverseString(stack, string))


main()
