'''
Conway's Game of Life!

The game takes place on an infinite 2D board of square cells.
Each cell is either dead or alive, and the following rules are applied at each tick:

    - Any live cell with less than two live neighbours dies
    - Any live cell with two or three live neighbours remains living
    - Any live cell with more than three live neighbours dies
    - Any dead cell with exactly three live neighbours becomes a live cell

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
The game should be initialized with a start list of live cell coordinates and the number
of ticks the game should run for.
The board is infinite, so only the cells relevant to the game (with cells) should be shown.

Represent a live cell with * and a dead cell with .
'''
class GameOfLife:
    def __init__(self, n, cells = set()):
        self.cells = cells
        self.iterations = n

    def play(self):
        for _ in range(self.iterations):
            try:
                self.print_board()
            except:
                break
            
            self.next()

    def get_number_of_live_neighbours(self, row, col):
        count = 0
        for cell_row, cell_col in self.cells:
            if abs(cell_row - row) > 1:
                continue
            if abs(cell_col - col) > 1:
                continue
            if cell_row == row and cell_col == col:
                continue
            count += 1

        return count

    def get_neighbouring_cells(self, row, col):
        return set([
            (row - 1, col - 1),
            (row, col - 1),
            (row + 1, col - 1),
            (row - 1, col),
            (row + 1, col),
            (row - 1, col + 1),
            (row, col + 1),
            (row + 1, col + 1),
        ])

    def get_boundaries(self):
        top = min(self.cells, key = lambda cell:cell[0])[0]
        left = min(self.cells, key = lambda cell:cell[1])[1]
        bottom = max(self.cells, key = lambda cell:cell[0])[0]
        right = max(self.cells, key = lambda cell:cell[1])[1]

        return top, left, bottom, right

    def print_board(self):
        top, left, bottom, right = self.get_boundaries()
        print('------------------------------------------')
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if (i, j) in self.cells:
                    print('*', end = '')
                else:
                    print('.', end = '')
            print('')
        print('------------------------------------------')

    def next(self):
        new_generation = set()

        #Find the cells in the current generation that do not die
        for row, col in self.cells:
            num_of_neighbours = self.get_number_of_live_neighbours(row, col)
            if 2 <= num_of_neighbours <= 3:
                new_generation.add((row, col))

        potential_new_cells = set()

        #Find the dead cells that may come to life
        for row, col in self.cells:
            #Find a unique set of cells that have live neighbours
            potential_new_cells = potential_new_cells.union(self.get_neighbouring_cells(row, col))
            #Remove already existing cells from the set
            potential_new_cells = potential_new_cells - self.cells
        
        #Find the potential cells that should come to life
        for row, col in potential_new_cells:
            num_of_neighbours = self.get_number_of_live_neighbours(row, col)
            if num_of_neighbours == 3:
                new_generation.add((row, col))

        self.cells = new_generation

if __name__ == '__main__':
    game = GameOfLife(5, set([(1,2), (2, 1), (1, 1), (2, 2), (3,3)]))
    game.play()
