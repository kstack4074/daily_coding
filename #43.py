'''
Implement a stack that has the following methods:
    - push(val), which pushes an element to the stack
    - pop(), which pops the last element, if no values, return null
    - max(), which returns the maximum value currently in the stack

Each method should run in constant time

Pushing and popping is easy to do in constant time.
Max is the main thing we need to consider.

How about we keep our normal stack, and a separate variable keeping track of the maximum.
We are only pushing one value at a time, so we can compare this value to the current max and change if needed.
When we pop, if the top value is the maximum, we need someway to remember what the previous maximum was.
How about we have two stacks??
'''

class Stack():
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):
        self.stack.append(val)
        if self.maxes:
            self.maxes.append(max(val, self.maxes[-1]))
        else:
            self.maxes.append(val)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]

if __name__ == '__main__':
    stack = Stack()