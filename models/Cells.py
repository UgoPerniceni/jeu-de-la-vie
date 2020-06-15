from models.Cell import Cell
import random
import numpy as np


class Cells:

    def __init__(self, cellsX, cellsY, cellSize):
        self.cells_x_max = cellsX - 1
        self.cells_y_max = cellsY - 1

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

    def get_neighbours_alive(self, x, y):
        alive = 0
        neighbors = self.get_neighbours(x, y)
        for tup in neighbors:
            if self.cells2d[tup[0]][tup[1]].alive:
                alive = alive + 1

        return alive

    def update_cell_state(self):
        for x in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                self.rule_cell(x, y)

    def rule_cell(self, x, y):
        # Rule 1 -> Si une cellule a exactement trois voisines vivantes, elle est vivante à l’étape suivante.
        if self.get_neighbours_alive(x, y) == 3:
            self.cells2d[x][y].alive = True
        # Rule 2 -> Si une cellule a exactement deux voisines vivantes, elle reste dans son état actuel à l’étape suivante.
        # elif self.get_neighbours_alive(x, y) == 2:
        #     self.cells2d[x][y].alive = self.cells2d[x][y].alive
        # Rule 3 -> Si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle est morte à l’étape suivante.
        elif self.get_neighbours_alive(x, y) < 2 or self.get_neighbours_alive(x, y) > 3:
            self.cells2d[x][y].alive = False

    def print_cells(self):
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                print(self.cells2d[i][y].toString())
