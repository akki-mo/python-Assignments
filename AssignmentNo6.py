class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def is_balanced_parentheses(input_string):
    stack = Stack()
    for char in input_string:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if (char == ')' and top_char != '(') or \
               (char == ']' and top_char != '[') or \
               (char == '}' and top_char != '{'):
                return False
    return stack.is_empty()


input_string = "((({}))"
if is_balanced_parentheses(input_string):
    print("The given string of parentheses is balanced.")
else:
    print("The given string of parentheses is not balanced.")
