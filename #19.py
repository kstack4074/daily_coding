'''
A builder is looking to build a row of N houses that can be K different colours.
He has a goal of minimizing cost while ensuring that no two neighbouring houses
are of the same colour.

Given an N by K matrix where the nth and the kth column represents the cost to
build the nth house with the kth colour, return the minimum cost which achieves
this goal.

Dynamic programming.
And then add memorization
'''
from timeit import default_timer as timer

def building_cost(costMatrix):
    min_cost = -1
    memo = [-1] * (len(costMatrix)*len(costMatrix[0]) + 1)
    for i in range(1, len(costMatrix[0]) + 1):
        cost = helper(costMatrix, 1, i, memo)
        if cost < min_cost or min_cost == -1:
            min_cost = cost

    return min_cost

def helper(costMatrix, curHouse, curColour, memo):
    cost = -1
    maxHouses = len(costMatrix)
    maxColours = len(costMatrix[0])
    memIdx = (curHouse - 1)*maxColours + (curColour - 1)

    if curHouse > maxHouses:
        return 0
    if curHouse == maxHouses:
        return costMatrix[curHouse - 1][curColour - 1]

    if memo[memIdx] != -1:
        return memo[memIdx]

    for i in range(1, maxColours + 1):
        if i != curColour:
            new_cost = helper(costMatrix, curHouse + 1, i, memo)
            if new_cost < cost or cost == -1:
                cost = new_cost
    cost += costMatrix[curHouse - 1][curColour - 1]
    memo[memIdx] = cost
    return cost


if __name__ == '__main__':
    costMatrix = [[1, 2, 3], [1, 4, 5], [1,2,2]]
    start = timer()
    print(building_cost(costMatrix))
    end = timer()
    print('Elapsed time ' + str(end - start))
