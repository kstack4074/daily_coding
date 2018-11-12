'''
N queens problem.
Given an N by N board, write a function that given N, returns the number
of possible arrangements of the board where N queens can be placed such that they are on:

    - distinct rows
    - distinct columns
    - distinct diagonals
'''

'''
Squish the board to a 1D array where index represents row and value
represents column.
Backtracking, add queen to board, if it's valid try the next row,
if it's not pop it from the board and try the next column.
'''
def n_queens(n, board = []):
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            count += n_queens(n, board)
        board.pop()

    return count

def is_valid(board):
    current_row = len(board) - 1
    current_col = board[-1]
    
    for row, col in enumerate(board[:-1]):
        diff = abs(current_col - col)
        if diff == 0 or diff == current_row - row:
            return False

    return True

if __name__ == '__main__':
    board_size = 4
    arrange = n_queens(board_size)
    print(arrange)