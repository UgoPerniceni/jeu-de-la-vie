from models.Cell import Cell
from random import randint
import numpy as np


class Cells:
    cell_die = []
    cell_born = []

    def __init__(self, cells_x, cells_y, cell_size):
        self.cells_x_max = cells_x
        self.cells_y_max = cells_y

        self.cells2d = np.empty(shape=(cells_x, cells_y), dtype=object)

        for x in range(0, cells_x):
            for y in range(0, cells_y):
                self.cells2d[x, y] = Cell(x, y, False, cell_size)

    def gen_cells(self):
        self.cells2d[40][30].alive = True
        self.cells2d[40][31].alive = True
        self.cells2d[40][32].alive = True

    def generate_random_cells_alive(self, cell_number=400):
        count = 0

        while count < cell_number:
            rand_x = randint(0, 79)
            rand_y = randint(0, 59)

            if not self.cells2d[rand_x][rand_y].alive:
                self.cells2d[rand_x][rand_y].alive = True
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
        neighbour_x = self.cells_x_max - 1
        neighbour_y = self.cells_y_max - 1

        neighbors = [
            (x2, y2)
            for x2 in range(x - 1, x + 2)
            for y2 in range(y - 1, y + 2)
            if (-1 < x <= neighbour_x and -1 < y <= neighbour_y and
                (x != x2 or y != y2) and
                (0 <= x2 <= neighbour_x) and
                (0 <= y2 <= neighbour_y))
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
        if neighbours_alive == 3:
            self.cell_born.append((x, y))
        # elif self.get_neighbours_alive(x, y) == 2:
        #     self.cells2d[x][y].alive = self.cells2d[x][y].alive
        elif neighbours_alive < 2 or neighbours_alive > 3:
            self.cell_die.append((x, y))

    def print_cells(self):
        for i in range(0, self.cells_x_max):
            for y in range(0, self.cells_y_max):
                print(self.cells2d[i][y].toString())

    # Draws
    def draw_spaceship_glider(self):
        self.cells2d[20][20].set_alive()
        self.cells2d[21][20].set_alive()
        self.cells2d[22][20].set_alive()

        self.cells2d[21][18].set_alive()
        self.cells2d[22][19].set_alive()

    def draw_spaceship_light_weight(self):
        self.cells2d[21][20].set_alive()
        self.cells2d[22][20].set_alive()

        self.cells2d[20][21].set_alive()
        self.cells2d[21][21].set_alive()
        self.cells2d[22][21].set_alive()
        self.cells2d[23][21].set_alive()

        self.cells2d[20][22].set_alive()
        self.cells2d[21][22].set_alive()
        self.cells2d[23][22].set_alive()
        self.cells2d[24][22].set_alive()

        self.cells2d[22][23].set_alive()
        self.cells2d[23][23].set_alive()

    def draw_spaceship_hammerhead(self):
        for i in range(30, 35):
            self.cells2d[i][30].set_alive()
            self.cells2d[i][45].set_alive()

        self.cells2d[37][37].set_alive()

        self.cells2d[37][38].set_alive()

        self.cells2d[36][36].set_alive()
        self.cells2d[38][36].set_alive()
        self.cells2d[40][36].set_alive()
        self.cells2d[42][36].set_alive()
        self.cells2d[36][39].set_alive()
        self.cells2d[38][39].set_alive()
        self.cells2d[40][39].set_alive()
        self.cells2d[42][39].set_alive()

        self.cells2d[35][35].set_alive()
        self.cells2d[40][35].set_alive()
        self.cells2d[43][35].set_alive()
        self.cells2d[35][40].set_alive()
        self.cells2d[40][40].set_alive()
        self.cells2d[43][40].set_alive()

        self.cells2d[33][34].set_alive()
        self.cells2d[34][34].set_alive()
        self.cells2d[38][34].set_alive()
        self.cells2d[39][34].set_alive()
        self.cells2d[41][34].set_alive()
        self.cells2d[42][34].set_alive()
        self.cells2d[45][34].set_alive()
        self.cells2d[46][34].set_alive()
        self.cells2d[33][41].set_alive()
        self.cells2d[34][41].set_alive()
        self.cells2d[38][41].set_alive()
        self.cells2d[39][41].set_alive()
        self.cells2d[41][41].set_alive()
        self.cells2d[42][41].set_alive()
        self.cells2d[45][41].set_alive()
        self.cells2d[46][41].set_alive()

        self.cells2d[31][33].set_alive()
        self.cells2d[41][33].set_alive()
        self.cells2d[42][33].set_alive()
        self.cells2d[44][33].set_alive()
        self.cells2d[45][33].set_alive()
        self.cells2d[46][33].set_alive()
        self.cells2d[47][33].set_alive()
        self.cells2d[31][42].set_alive()
        self.cells2d[41][42].set_alive()
        self.cells2d[42][42].set_alive()
        self.cells2d[44][42].set_alive()
        self.cells2d[45][42].set_alive()
        self.cells2d[46][42].set_alive()
        self.cells2d[47][42].set_alive()

        self.cells2d[30][32].set_alive()
        self.cells2d[42][32].set_alive()
        self.cells2d[43][32].set_alive()
        self.cells2d[45][32].set_alive()
        self.cells2d[46][32].set_alive()
        self.cells2d[47][32].set_alive()
        self.cells2d[30][43].set_alive()
        self.cells2d[42][43].set_alive()
        self.cells2d[43][43].set_alive()
        self.cells2d[45][43].set_alive()
        self.cells2d[46][43].set_alive()
        self.cells2d[47][43].set_alive()

        self.cells2d[30][31].set_alive()
        self.cells2d[35][31].set_alive()
        self.cells2d[43][31].set_alive()
        self.cells2d[44][31].set_alive()
        self.cells2d[30][44].set_alive()
        self.cells2d[35][44].set_alive()
        self.cells2d[43][44].set_alive()
        self.cells2d[44][44].set_alive()

    def draw_still_life_bee_hive(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[41][30].set_alive()
        self.cells2d[39][29].set_alive()
        self.cells2d[42][29].set_alive()
        self.cells2d[40][28].set_alive()
        self.cells2d[41][28].set_alive()

    def draw_still_life_block(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[40][31].set_alive()
        self.cells2d[41][30].set_alive()
        self.cells2d[41][31].set_alive()

    def draw_still_life_boat(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[41][30].set_alive()
        self.cells2d[40][29].set_alive()
        self.cells2d[42][29].set_alive()
        self.cells2d[41][28].set_alive()

    def draw_still_life_loaf(self):
        self.cells2d[42][29].set_alive()
        self.cells2d[40][28].set_alive()
        self.cells2d[42][28].set_alive()
        self.cells2d[41][27].set_alive()
        self.cells2d[40][30].set_alive()
        self.cells2d[41][30].set_alive()
        self.cells2d[39][29].set_alive()

    def draw_still_life_tube(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[39][29].set_alive()
        self.cells2d[41][29].set_alive()
        self.cells2d[40][28].set_alive()

    def draw_oscillator_blinker(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[41][30].set_alive()
        self.cells2d[42][30].set_alive()

    def draw_oscillator_beacon(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[40][31].set_alive()
        self.cells2d[41][30].set_alive()
        self.cells2d[41][31].set_alive()
        self.cells2d[42][32].set_alive()
        self.cells2d[42][33].set_alive()
        self.cells2d[43][32].set_alive()
        self.cells2d[43][33].set_alive()

    def draw_oscillator_penta_decathlon(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[40][31].set_alive()
        self.cells2d[39][32].set_alive()
        self.cells2d[41][32].set_alive()
        self.cells2d[40][33].set_alive()
        self.cells2d[40][34].set_alive()
        self.cells2d[40][35].set_alive()
        self.cells2d[40][36].set_alive()
        self.cells2d[39][37].set_alive()
        self.cells2d[41][37].set_alive()
        self.cells2d[40][38].set_alive()
        self.cells2d[40][39].set_alive()

    def draw_oscillator_pulsar(self):
        self.cells2d[40][30].set_alive()
        self.cells2d[41][30].set_alive()
        self.cells2d[42][30].set_alive()
        self.cells2d[46][30].set_alive()
        self.cells2d[47][30].set_alive()
        self.cells2d[48][30].set_alive()
        self.cells2d[40][35].set_alive()
        self.cells2d[41][35].set_alive()
        self.cells2d[42][35].set_alive()
        self.cells2d[46][35].set_alive()
        self.cells2d[47][35].set_alive()
        self.cells2d[48][35].set_alive()
        self.cells2d[40][37].set_alive()
        self.cells2d[41][37].set_alive()
        self.cells2d[42][37].set_alive()
        self.cells2d[46][37].set_alive()
        self.cells2d[47][37].set_alive()
        self.cells2d[48][37].set_alive()
        self.cells2d[40][42].set_alive()
        self.cells2d[41][42].set_alive()
        self.cells2d[42][42].set_alive()
        self.cells2d[46][42].set_alive()
        self.cells2d[47][42].set_alive()
        self.cells2d[48][42].set_alive()
        self.cells2d[38][32].set_alive()
        self.cells2d[38][33].set_alive()
        self.cells2d[38][34].set_alive()
        self.cells2d[43][32].set_alive()
        self.cells2d[43][33].set_alive()
        self.cells2d[43][34].set_alive()
        self.cells2d[45][32].set_alive()
        self.cells2d[45][33].set_alive()
        self.cells2d[45][34].set_alive()
        self.cells2d[50][32].set_alive()
        self.cells2d[50][33].set_alive()
        self.cells2d[50][34].set_alive()
        self.cells2d[38][38].set_alive()
        self.cells2d[38][39].set_alive()
        self.cells2d[38][40].set_alive()
        self.cells2d[43][38].set_alive()
        self.cells2d[43][39].set_alive()
        self.cells2d[43][40].set_alive()
        self.cells2d[45][38].set_alive()
        self.cells2d[45][39].set_alive()
        self.cells2d[45][40].set_alive()
        self.cells2d[50][38].set_alive()
        self.cells2d[50][39].set_alive()
        self.cells2d[50][40].set_alive()

    def draw_oscillator_toad(self):
        self.cells2d[38][30].set_alive()
        self.cells2d[39][30].set_alive()
        self.cells2d[39][31].set_alive()
        self.cells2d[38][31].set_alive()
        self.cells2d[37][30].set_alive()
        self.cells2d[40][31].set_alive()

    def draw_special_gosper_glider_gun(self):
        self.cells2d[20][25].set_alive()
        self.cells2d[20][26].set_alive()
        self.cells2d[21][25].set_alive()
        self.cells2d[21][26].set_alive()
        self.cells2d[30][25].set_alive()
        self.cells2d[30][26].set_alive()
        self.cells2d[30][27].set_alive()
        self.cells2d[31][24].set_alive()
        self.cells2d[31][28].set_alive()
        self.cells2d[32][23].set_alive()
        self.cells2d[32][29].set_alive()
        self.cells2d[33][23].set_alive()
        self.cells2d[33][29].set_alive()
        self.cells2d[34][26].set_alive()
        self.cells2d[35][24].set_alive()
        self.cells2d[35][28].set_alive()
        self.cells2d[36][25].set_alive()
        self.cells2d[36][26].set_alive()
        self.cells2d[36][27].set_alive()
        self.cells2d[37][26].set_alive()
        self.cells2d[40][23].set_alive()
        self.cells2d[40][24].set_alive()
        self.cells2d[40][25].set_alive()
        self.cells2d[41][23].set_alive()
        self.cells2d[41][24].set_alive()
        self.cells2d[41][25].set_alive()
        self.cells2d[42][22].set_alive()
        self.cells2d[42][26].set_alive()
        self.cells2d[44][21].set_alive()
        self.cells2d[44][22].set_alive()
        self.cells2d[44][26].set_alive()
        self.cells2d[44][27].set_alive()
        self.cells2d[54][23].set_alive()
        self.cells2d[54][24].set_alive()
        self.cells2d[55][23].set_alive()
        self.cells2d[55][24].set_alive()

    def draw_special_benjamin(self):
        for i in range(10, 20):
            for j in range(10, 20):
                self.cells2d[i][j].set_alive()
        for i in range(35, 45):
            for j in range(10, 20):
                self.cells2d[i][j].set_alive()
        for i in range(20, 35):
            for j in range(20, 37):
                self.cells2d[i][j].set_alive()
