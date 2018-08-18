'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

We return pair with the input a, b
This returned value expects a function to be passed as well
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def inner(a, b):
        return a
    return pair(inner)

def cdr(pair):
    def inner(a, b):
        return b
    return pair(inner)

print(car(cons(1, 4)), cdr(cons(1,7)))
