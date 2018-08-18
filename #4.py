'''
Daily coding problem #4 04-08-2018
Asked by stripe

Given an array of integers, find the first missing positive integer in linear time
and constant space. In other words, find the lowest positive integer that does not
exist in the array. The array can contain duplicates and negative numbersself.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place

Cases:
1. Empty array [] -> 1
2. All negatives [-1, -2] -> 1
3. All positives [1, 2] -> 3
4. Mixture [-1, 2] -> 1

Can solve by storing in dictionary than iterating over.
Linear time but not constant space.

Need to modify the array in-place.
Sort it?
Do linear sorters exist? No

Find lowest and highest value.
Assign elements to place in array via index?

'''

def missing_int(array):
    if len(array) == 0:
        return 1

    #Sorting
    for i in range(len(array)):
        if(array[i] > len(array) or array[i] <= 0):
            array[i] = -1
        else:
            while((array[i] != i + 1) and (0 < array[i] <= len(array))):
                value = array[i] - 1
                if(array[i] == array[value]):
                    break
                else:
                    array[i], array[value] = array[value], array[i]

    #Find missing int
    for i in range(len(array)):
        if(array[i] != i + 1):
            return i + 1

    print(array)

array = [3,4,3,1]
retVal = missing_int(array)
print(retVal)
