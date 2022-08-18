# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

from Stack import Stack


def validParentheses(stack, string):
    for s in string:

        if s in ['(', '[', '{']:
            stack.push(s)
        elif s == ')' and (not stack.IsEmpty()) and stack.peek() == '(':
            stack.pop()
        elif s == ']' and (not stack.IsEmpty()) and stack.peek() == '[':
            stack.pop()
        elif s == '}' and (not stack.IsEmpty()) and stack.peek() == '{':
            stack.pop()
        else:
            return False

    return stack.IsEmpty()


def main():
    stack = Stack()
    string = '{()({}[]()){}[((({}{})))]}'
    print(validParentheses(stack, string))


main()
