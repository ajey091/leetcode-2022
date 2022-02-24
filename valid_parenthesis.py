# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# s - '(([[]]))' valid
# s - '(([]][))' not valid

# (([[]]))
# True

# (([]][))
# (, (,
# False

# []()
# (]

def valid(string):
    stack = []
    for char in string:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif len(stack) > 0:
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0
