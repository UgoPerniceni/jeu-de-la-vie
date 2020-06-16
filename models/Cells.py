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

    def draw_spaceship_glider(self):
        self.cells2d[20][20].setAlive()
        self.cells2d[21][20].setAlive()
        self.cells2d[22][20].setAlive()

        self.cells2d[21][18].setAlive()
        self.cells2d[22][19].setAlive()

    def draw_spaceship_light_weight(self):
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

    def draw_still_life_block(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[40][31].setAlive()
        self.cells2d[41][30].setAlive()
        self.cells2d[41][31].setAlive()

    def draw_still_life_bee_hive(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[41][30].setAlive()
        self.cells2d[39][29].setAlive()
        self.cells2d[42][29].setAlive()
        self.cells2d[40][28].setAlive()
        self.cells2d[41][28].setAlive()

    def draw_still_life_boat(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[41][30].setAlive()
        self.cells2d[40][29].setAlive()
        self.cells2d[42][29].setAlive()
        self.cells2d[41][28].setAlive()

    def draw_still_life_loaf(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[41][30].setAlive()
        self.cells2d[39][29].setAlive()
        self.cells2d[42][29].setAlive()
        self.cells2d[40][28].setAlive()
        self.cells2d[42][28].setAlive()
        self.cells2d[41][27].setAlive()

    def draw_still_life_tube(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[39][29].setAlive()
        self.cells2d[41][29].setAlive()
        self.cells2d[40][28].setAlive()

    def draw_blinker(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[41][30].setAlive()
        self.cells2d[42][30].setAlive()

    def draw_oscillator_beacon(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[40][31].setAlive()
        self.cells2d[41][30].setAlive()
        self.cells2d[41][31].setAlive()
        self.cells2d[42][32].setAlive()
        self.cells2d[42][33].setAlive()
        self.cells2d[43][32].setAlive()
        self.cells2d[43][33].setAlive()

    def draw_oscillator_penta_decathlon(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[40][31].setAlive()
        self.cells2d[39][32].setAlive()
        self.cells2d[41][32].setAlive()
        self.cells2d[40][33].setAlive()
        self.cells2d[40][34].setAlive()
        self.cells2d[40][35].setAlive()
        self.cells2d[40][36].setAlive()
        self.cells2d[39][37].setAlive()
        self.cells2d[41][37].setAlive()
        self.cells2d[40][38].setAlive()
        self.cells2d[40][39].setAlive()

    def draw_oscillator_toad(self):
        self.cells2d[38][30].setAlive()
        self.cells2d[39][30].setAlive()
        self.cells2d[39][31].setAlive()
        self.cells2d[38][31].setAlive()
        self.cells2d[37][30].setAlive()
        self.cells2d[40][31].setAlive()

    def draw_oscillator_pulsar(self):
        self.cells2d[40][30].setAlive()
        self.cells2d[41][30].setAlive()
        self.cells2d[42][30].setAlive()
        self.cells2d[46][30].setAlive()
        self.cells2d[47][30].setAlive()
        self.cells2d[48][30].setAlive()
        self.cells2d[40][35].setAlive()
        self.cells2d[41][35].setAlive()
        self.cells2d[42][35].setAlive()
        self.cells2d[46][35].setAlive()
        self.cells2d[47][35].setAlive()
        self.cells2d[48][35].setAlive()
        self.cells2d[40][37].setAlive()
        self.cells2d[41][37].setAlive()
        self.cells2d[42][37].setAlive()
        self.cells2d[46][37].setAlive()
        self.cells2d[47][37].setAlive()
        self.cells2d[48][37].setAlive()
        self.cells2d[40][42].setAlive()
        self.cells2d[41][42].setAlive()
        self.cells2d[42][42].setAlive()
        self.cells2d[46][42].setAlive()
        self.cells2d[47][42].setAlive()
        self.cells2d[48][42].setAlive()
        self.cells2d[38][32].setAlive()
        self.cells2d[38][33].setAlive()
        self.cells2d[38][34].setAlive()
        self.cells2d[43][32].setAlive()
        self.cells2d[43][33].setAlive()
        self.cells2d[43][34].setAlive()
        self.cells2d[45][32].setAlive()
        self.cells2d[45][33].setAlive()
        self.cells2d[45][34].setAlive()
        self.cells2d[50][32].setAlive()
        self.cells2d[50][33].setAlive()
        self.cells2d[50][34].setAlive()
        self.cells2d[38][38].setAlive()
        self.cells2d[38][39].setAlive()
        self.cells2d[38][40].setAlive()
        self.cells2d[43][38].setAlive()
        self.cells2d[43][39].setAlive()
        self.cells2d[43][40].setAlive()
        self.cells2d[45][38].setAlive()
        self.cells2d[45][39].setAlive()
        self.cells2d[45][40].setAlive()
        self.cells2d[50][38].setAlive()
        self.cells2d[50][39].setAlive()
        self.cells2d[50][40].setAlive()

    def draw_special_benjamin(self):
        for i in range(10, 20):
            for j in range(10, 20):
                self.cells2d[i][j].setAlive()
        for i in range(35, 45):
            for j in range(10, 20):
                self.cells2d[i][j].setAlive()
        for i in range(20, 35):
            for j in range(20, 37):
                self.cells2d[i][j].setAlive()

    def draw_special_gosper_glider_gun(self):
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

    def draw_hammerhead(self):
        for i in range(30, 35):
            self.cells2d[i][30].setAlive()
            self.cells2d[i][45].setAlive()

        self.cells2d[37][37].setAlive()

        self.cells2d[37][38].setAlive()

        self.cells2d[36][36].setAlive()
        self.cells2d[38][36].setAlive()
        self.cells2d[40][36].setAlive()
        self.cells2d[42][36].setAlive()
        self.cells2d[36][39].setAlive()
        self.cells2d[38][39].setAlive()
        self.cells2d[40][39].setAlive()
        self.cells2d[42][39].setAlive()

        self.cells2d[35][35].setAlive()
        self.cells2d[40][35].setAlive()
        self.cells2d[43][35].setAlive()
        self.cells2d[35][40].setAlive()
        self.cells2d[40][40].setAlive()
        self.cells2d[43][40].setAlive()

        self.cells2d[33][34].setAlive()
        self.cells2d[34][34].setAlive()
        self.cells2d[38][34].setAlive()
        self.cells2d[39][34].setAlive()
        self.cells2d[41][34].setAlive()
        self.cells2d[42][34].setAlive()
        self.cells2d[45][34].setAlive()
        self.cells2d[46][34].setAlive()
        self.cells2d[33][41].setAlive()
        self.cells2d[34][41].setAlive()
        self.cells2d[38][41].setAlive()
        self.cells2d[39][41].setAlive()
        self.cells2d[41][41].setAlive()
        self.cells2d[42][41].setAlive()
        self.cells2d[45][41].setAlive()
        self.cells2d[46][41].setAlive()

        self.cells2d[31][33].setAlive()
        self.cells2d[41][33].setAlive()
        self.cells2d[42][33].setAlive()
        self.cells2d[44][33].setAlive()
        self.cells2d[45][33].setAlive()
        self.cells2d[46][33].setAlive()
        self.cells2d[47][33].setAlive()
        self.cells2d[31][42].setAlive()
        self.cells2d[41][42].setAlive()
        self.cells2d[42][42].setAlive()
        self.cells2d[44][42].setAlive()
        self.cells2d[45][42].setAlive()
        self.cells2d[46][42].setAlive()
        self.cells2d[47][42].setAlive()

        self.cells2d[30][32].setAlive()
        self.cells2d[42][32].setAlive()
        self.cells2d[43][32].setAlive()
        self.cells2d[45][32].setAlive()
        self.cells2d[46][32].setAlive()
        self.cells2d[47][32].setAlive()
        self.cells2d[30][43].setAlive()
        self.cells2d[42][43].setAlive()
        self.cells2d[43][43].setAlive()
        self.cells2d[45][43].setAlive()
        self.cells2d[46][43].setAlive()
        self.cells2d[47][43].setAlive()

        self.cells2d[30][31].setAlive()
        self.cells2d[35][31].setAlive()
        self.cells2d[43][31].setAlive()
        self.cells2d[44][31].setAlive()
        self.cells2d[30][44].setAlive()
        self.cells2d[35][44].setAlive()
        self.cells2d[43][44].setAlive()
        self.cells2d[44][44].setAlive()

    def print_cells(self):
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                print(self.cells2d[i][y].toString())
