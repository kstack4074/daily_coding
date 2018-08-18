def array_sum(array):
        s = 1
        for val in array:
                s = s * val
        for idx, val in enumerate(array):
                array[idx] = int(s/val)
	
        return array


def array_sum_no_div(array):
        arrayLen = len(array)
        leftArray = [0] * (arrayLen)
        leftArray[0] = 1
        rightArray = [0] * (arrayLen)
        rightArray[len(array) - 1] = 1

        for i in range(1, arrayLen, 1):
                leftArray[i] = leftArray[i - 1] * array[i - 1]

        for i in range(arrayLen - 2, -1, -1):
                rightArray[i] = rightArray[i + 1] * array[i + 1]

        for i in range(arrayLen):
                array[i] = leftArray[i] * rightArray[i]

        print(leftArray)
        print(rightArray)
        return array
        
array = [1,2,3,4,5]
print(array)
array = array_sum_no_div(array)
print(array)
		
