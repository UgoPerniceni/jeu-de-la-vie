from models.Cell import Cell
from random import randint
import numpy as np


class Cells:
    cell_die = []
    cell_born = []

    def __init__(self, cellsX, cellsY, cellSize):
        self.cells_x_max = cellsX
        self.cells_y_max = cellsY

        self.cells2d = np.empty(shape=(cellsX, cellsY), dtype=object)

        for x in range(0, cellsX):
            for y in range(0, cellsY):
                self.cells2d[x, y] = Cell(x, y, False, cellSize)

    def gen_cells(self):
        self.cells2d[40][30].alive = True
        self.cells2d[40][31].alive = True
        self.cells2d[40][32].alive = True

    def generate_random_cells_alive(self, numberCell=400):
        count = 0

        while count < numberCell:
            randX = randint(0, 79)
            randY = randint(0, 59)

            if not self.cells2d[randX][randY].alive:
                self.cells2d[randX][randY].alive = True
                count = count + 1

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

    def get_neighbours(self, x, y):
        X = self.cells_x_max - 1
        Y = self.cells_y_max - 1

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
        self.cell_die.clear()
        self.cell_born.clear()

        for x in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                self.rule_cell(x, y)

        for tup in self.cell_die:
            self.cells2d[tup[0]][tup[1]].alive = False
        for tup in self.cell_born:
            self.cells2d[tup[0]][tup[1]].alive = True

    def rule_cell(self, x, y):
        neighbours_alive = self.get_neighbours_alive(x, y)
        # Rule 1 -> Si une cellule a exactement trois voisines vivantes, elle est vivante à l’étape suivante.
        if neighbours_alive == 3:
            # self.cells2d[x][y].alive = True
            self.cell_born.append((x, y))
        # Rule 2 -> Si une cellule a exactement deux voisines vivantes, elle reste dans son état actuel à l’étape suivante.
        # elif self.get_neighbours_alive(x, y) == 2:
        #     self.cells2d[x][y].alive = self.cells2d[x][y].alive
        # Rule 3 -> Si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle est morte à l’étape suivante.
        elif neighbours_alive < 2 or neighbours_alive > 3:
            # self.cells2d[x][y].alive = False
            self.cell_die.append((x, y))

    def draw_spaceship_Glider(self):
        self.cells2d[20][20].setAlive()
        self.cells2d[21][20].setAlive()
        self.cells2d[22][20].setAlive()

        self.cells2d[21][18].setAlive()
        self.cells2d[22][19].setAlive()

    def draw_spaceship_Light_weight(self):
        self.cells2d[21][20].setAlive()
        self.cells2d[22][20].setAlive()

        self.cells2d[20][21].setAlive()
        self.cells2d[21][21].setAlive()
        self.cells2d[22][21].setAlive()
        self.cells2d[23][21].setAlive()

        self.cells2d[20][22].setAlive()
        self.cells2d[21][22].setAlive()
        self.cells2d[23][22].setAlive()
        self.cells2d[24][22].setAlive()

        self.cells2d[22][23].setAlive()
        self.cells2d[23][23].setAlive()

    def draw_oscillator_toad(self):
        self.cells2d[38][30].setAlive()
        self.cells2d[39][30].setAlive()
        self.cells2d[39][31].setAlive()
        self.cells2d[38][31].setAlive()
        self.cells2d[37][30].setAlive()
        self.cells2d[40][31].setAlive()

    def draw_Gosper_glider_gun(self):
        self.cells2d[20][25].setAlive()
        self.cells2d[20][26].setAlive()
        self.cells2d[21][25].setAlive()
        self.cells2d[21][26].setAlive()
        self.cells2d[30][25].setAlive()
        self.cells2d[30][26].setAlive()
        self.cells2d[30][27].setAlive()
        self.cells2d[31][24].setAlive()
        self.cells2d[31][28].setAlive()
        self.cells2d[32][23].setAlive()
        self.cells2d[32][29].setAlive()
        self.cells2d[33][23].setAlive()
        self.cells2d[33][29].setAlive()
        self.cells2d[34][26].setAlive()
        self.cells2d[35][24].setAlive()
        self.cells2d[35][28].setAlive()
        self.cells2d[36][25].setAlive()
        self.cells2d[36][26].setAlive()
        self.cells2d[36][27].setAlive()
        self.cells2d[37][26].setAlive()
        self.cells2d[40][23].setAlive()
        self.cells2d[40][24].setAlive()
        self.cells2d[40][25].setAlive()
        self.cells2d[41][23].setAlive()
        self.cells2d[41][24].setAlive()
        self.cells2d[41][25].setAlive()
        self.cells2d[42][22].setAlive()
        self.cells2d[42][26].setAlive()
        self.cells2d[44][21].setAlive()
        self.cells2d[44][22].setAlive()
        self.cells2d[44][26].setAlive()
        self.cells2d[44][27].setAlive()
        self.cells2d[54][23].setAlive()
        self.cells2d[54][24].setAlive()
        self.cells2d[55][23].setAlive()
        self.cells2d[55][24].setAlive()

    def print_cells(self):
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                print(self.cells2d[i][y].toString())
