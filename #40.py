'''
Given an array of integers where every integer occurs three times except for 
one integer, which occurs only once. Find and return the non-duplicated integered.

e.g.
[6, 1, 3, 3, 3, 6, 6] return 1
[13, 19, 13, 13] return 19

Do this in O(n) time and O(1) space

If this was only two duplications, we could xor the values.
For three duplications, we can apply this same principle by mod 3.
We can't xor 3 times because we might have one bit go 1 > 0 > 1, and another go 0 > 0 > 1.
Let's assume that we get no numbers less than 32 bits.
'''

def find_unique(numbers):
    bits = [0] * 32

    for number in numbers:
        for i in range(32):
            bit = (number >> i) & 1
            bits[i] = (bits[i] + bit) % 3
    
    unique_number = 0

    for i in range(32):
        if bits[i] == 1:
            unique_number += (2 ** i)

    return unique_number

if __name__ == '__main__':
    array = [13, 19, 13, 13]
    number = find_unique(array)
    print(number)

