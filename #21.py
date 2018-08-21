'''
Given an array of time intervals (start, end) for lectures (possibly overalapping),
find the minimum number of rooms required.

e.g. [(30, 75), (0, 50), (60, 150)] should return 2.

Greedy algorithm. Keep track of max class number and current classes.

Split the start times into one array, and the end times into another, both sorted.
This would be O(nlog(n)) time and O(n) space complexity.

Can we do it in constant space?
'''

def classroom_numbers(class_times):
    class_start_times = [-1] * len(class_times)
    class_end_times = [-1] * len(class_times)

    for idx, class_time in enumerate(class_times):
        class_start_times[idx] = class_times[idx][0]
        class_end_times[idx] = class_times[idx][1]
    class_start_times.sort()
    class_end_times.sort()

    maxClasses = 0
    currentClasses = 0
    i, j = 0, 0
    while(i < len(class_start_times) and j < len(class_end_times)):
        if class_start_times[i] < class_end_times[j]:
            currentClasses += 1
            if currentClasses > maxClasses:
                maxClasses = currentClasses
            i += 1
        else:
            currentClasses -= 1
            j += 1
    return maxClasses

if __name__ == '__main__':
    class_times = [(30, 75), (0, 30), (30, 150)]
    class_numbers = classroom_numbers(class_times)
    print(class_numbers)
