from cell import Cell
from printer import Printer

# The Board represents the state of all the cells and can calculatethe next
# state based on the current, governed by the set of rules.
class Board:

    # The initializer for the Board creates a new 2D board that is size X size.
    def __init__(self, row_count, column_count):
        self.width = column_count
        self.height = row_count
        self.matrix = self.new_matrix(row_count, column_count)

    # Creates a new matrix via 2D arrays.
    def new_matrix(self, rows, cols):
        return [[Cell() for _ in range(cols)] for _ in range(rows)]

    # Given the current state of the cells, advances to the next state based
    # on the following rules:
    #   1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    #   2. Any live cell with two or three live neighbours lives on to the next generation.
    #   3. Any live cell with more than three live neighbours dies, as if by overcrowding.
    #   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    def advance(self):

        # Calculate the neighbors of each cell.
        for i in range(self.height):
            for j in range(self.width):
                cell = self.matrix[i][j]
                cell.neighbors = self.neighbor_count(i, j)

        # Kill, keep alive, or revive each cell based on neighbor count.
        for i in range(self.height):
            for j in range(self.width):
                cell = self.matrix[i][j]
                if cell.alive:
                    if cell.neighbors != 2 and cell.neighbors != 3:
                        cell.alive = False
                else:
                    if cell.neighbors == 3:
                        cell.alive = True

    # Returns the number of live neighbors of the cell at the given row and
    # column.
    def neighbor_count(self, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            if i > -1 and i < self.height:
                for j in range(col - 1, col + 2):
                    if j > -1 and j < self.width and not(i == row and j == col) and self.matrix[i][j].alive:
                        count += 1
        return count

    # Reprint the board
    def reprint(self):
        Printer.move_to_home()
        for i in range(self.height):
            row_string = ""
            for j in range(self.width):
                cell = self.matrix[i][j]
                if cell.alive:
                    row_string += "\033[32mX\033[0m"
                else:
                    row_string += "-"
            Printer.reprint(row_string)
