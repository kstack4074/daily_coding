def decoder(array):
    memo = [-1] * (len(array) + 1)
    return number_of_ways(array, len(array), memo)


def number_of_ways(array, k, memo):
    result = 0
    if k == 0:
        return 1

    sIdx = len(array) - k
    if array[sIdx] == '0':
        return 0

    if memo[k] != -1:
        return memo[k]

    if(k >= 2 and int(array[sIdx] + array[sIdx + 1]) < 26):
        result += number_of_ways(array, k - 1, memo) + \
            number_of_ways(array, k - 2, memo)
    else:
        result += number_of_ways(array, k - 1, memo)

    memo[k] = result
    return result


string = '113'
decoder(string)
