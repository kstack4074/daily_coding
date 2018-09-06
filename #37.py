'''
The power set of a set is the set of all its subsets.
Write a function that given a set, generates its power set.

e.g. {1, 2, 3} -> {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
'''

def find_power_set(mySet):
    power_set = []
    return helper(mySet, power_set)

def helper(mySet, power_set):
    if len(mySet) == 0:
        power_set.append(mySet)
        return
    else:
        power_set.append(mySet)

    for ele in mySet:
        tempSet = set(mySet)
        tempSet.remove(ele)
        if not tempSet in power_set:
            helper(tempSet, power_set)

    return power_set

if __name__ == '__main__':
    temp = set([1, 2, 3,4,5,6,7,8,9,10,11,12])
    print(find_power_set(temp))
