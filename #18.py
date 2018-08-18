'''
Given an array of integers and a number k, where 1 <= k <= len(arary) compute
the maximum values of each subarray of length kself.

e.g.
array = [10, 5, 2, 7, 8, 7], k = 3
-> [10, 7, 8,8]

Do this in O(n) time and O(k) space. Don't need to store results, you can just
print it as you compute it.
'''
from collections import deque

def max_subarray(array, k):
    Qi = deque()

    for i in range(k):
        while Qi and array[i] >= array[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    for i in range(k, len(array)):
        #Print the current window max
        print(array[Qi[0]])

        #Remove elements not in current window
        while Qi and Qi[0] <= i - k:
            Qi.popleft()

        #Add new maximums to window
        while Qi and array[Qi[-1]] <= array[i]:
            Qi.pop()

        #Print the last windows maximum
        Qi.append(i)

    print(array[Qi[0]])


if __name__ == '__main__':
    max_subarray([10,2,5,7,8,7], 3)
