# Represents a cell in the Game of Life.
class Cell:

    def __init__(self, alive = False):
        self.alive = alive
        self.neighbors = 0
