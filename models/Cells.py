from models.Cell import Cell
import random
import numpy as np


class Cells:

    def __init__(self, cellsX, cellsY, cellSize):
        self.cells_x_max = cellsX
        self.cells_y_max = cellsY

        self.cells2d = np.empty(shape=(cellsX, cellsY), dtype=object)

        for x in range(0, cellsX):
            for y in range(0, cellsY):
                self.cells2d[x, y] = Cell(x, y, False, cellSize)

    def generate_random_cells_alive(self, percentage=10):
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                chance = random.random()
                # 10% chance
                if chance * 100 < percentage:
                    self.cells2d[i][y].alive = True

    def kill_cells(self):
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                self.cells2d[i][y].alive = False

    def count_cells_alive(self):
        alive = 0
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                if self.cells2d[i][y].alive:
                    alive = alive + 1
        return alive

    # def get_cell_by_id(self, id):
    #     print(self.rows[id].toString())

    def get_neighbours(self, x, y):
        X = self.cells_x_max
        Y = self.cells_y_max

        neighbors = [
            (x2, y2)
            for x2 in range(x - 1, x + 2)
            for y2 in range(y - 1, y + 2)
            if (-1 < x <= X and -1 < y <= Y and
                (x != x2 or y != y2) and
                (0 <= x2 <= X) and
                (0 <= y2 <= Y))
        ]

        return neighbors

    def print_cells(self):
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                print(self.cells2d[i][y].toString())
