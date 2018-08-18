def number_sum(array, sum):
    array.sort()
    l = len(array) - 1
    s = 0

    for _ in array:
        if array[l] + array[s] == sum:
            return True
        elif array[l] + array[s] > sum:
            l -= 1
        else:
            s += 1
    return False

numberArr = [10, 15, 3, 7]



retVal = number_sum(numberArr, 10)
print(retVal)
