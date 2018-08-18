'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

[1, 2, 3, 4] OR [1, 2, 3, 4]
 ^     ^            ^     ^

For odd lengths:
[1, 2, 3, 4, 5] OR [1, 2, 3, 4, 5]
 ^     ^     ^         ^     ^

You'll always want to grab the maxium number of elements,
it just depends where you start to hit the max val.

Define two values, the sum starting from 0,
and the sum starting from 1.

Wrong, in [5, 1, 1, 5] example we take the two bound values.
incl = 5, excl = 0
incl = 1, excl = 5
incl = 6, excl = 5
incl = 10, excl = 6
'''

def largest_sum(array):
    incl = 0
    excl = 0
    new_excl = 0

    for value in array:
        print(incl, excl)
        if excl > incl:
            new_excl = excl
        else:
            new_excl = incl

        incl = excl + value
        excl = new_excl

    return (excl if excl > incl else incl)


test1 = [2, 4, 6, 2, 5] #13
test2 = [5, 1, 1, 5] #10
test3 = [5, 5, 10, 100, 10, 5] #110

largest_sum(test2)
