import time

from random import randint
from board import Board

# This Game class is responsible for running the game over time.
class Game:

    # The Game initializer.
    def __init__(self, width, height):
        self.board = Board(width, height)

    # Seeds the cell at the given position.
    # Input should be an array, i.e. [0,0]
    def seed(self, x, y):
        self.board.matrix[x][y].alive = True

    # Run a game with the given number of iterations.
    def run(self, num):
        for _ in range(num):
            time.sleep(0.1)
            self.board.advance()
            self.board.reprint()

    # Setups a "toad" which is a specific pattern of cells.
    def setup_toad(self):
        self.seed(10, 10)
        self.seed(10, 11)
        self.seed(10, 12)
        self.seed(11, 9)
        self.seed(11, 10)
        self.seed(11, 11)

    # Setups a given number of cells in random locations across the board. this line is so effing long
    def setup_random(self, number):
        for _ in range(number):
            seed(randint(self.board.height), randint(self.board.width))
