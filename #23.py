'''
You are given an M by N matrix consisting of booleans that represent a board.
True represents a wall, False represents traversable tiles.

Given this matrix, a start coord, and an end coord, return the minimum number
of steps to go from start to end. If there's no possible path, return null.
'''
from queue import Queue

def walkable(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    return not board[row][col]

def get_walkable_neighbours(board, row, col):
    return [(r, c) for r, c in [
        (row, col - 1),
        (row, col + 1),
        (row - 1, col),
        (row + 1, col)]
        if walkable(board, r, c)
    ]

def path_builder(nodePath, node):
    path = []
    while nodePath[node] != None:
        path.append(node)
        node = nodePath[node]

    path.append(node)
    return path

def board_walk(board, start, end):
    nodePath = {}
    nodesToVisit = Queue()

    nodesToVisit.put((start, 0))
    nodePath[start] = None

    while nodesToVisit:
        node, count = nodesToVisit.get()
        print(nodesToVisit)
        if node == end:
            return path_builder(nodePath, node)

        #Adjacency List
        for neighbour in get_walkable_neighbours(board, node[0], node[1]):
            if neighbour not in nodePath:
                nodesToVisit.put((neighbour, count + 1))
                nodePath[neighbour] = node

    return 'b'

if __name__ == '__main__':
    board = [[False, False, False, False],
             [True, True, False, True],
             [False, False, False, False],
             [False, False, False, False]]

    start = (2, 0)
    end = (0, 0)
    a = []
    minSteps = board_walk(board, start, end)
    print(minSteps)
