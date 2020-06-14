from models.Cell import Cell
import random


class Cells:
    cols = []
    rows = []

    def __init__(self, cellsX, cellsY, cellSize):
        self.cells_x_max = cellsX
        self.cells_y_max = cellsY

        for i in range(0, cellsX):
            for y in range(0, cellsY):
                self.rows.append(Cell(i, y, False, cellSize))
            self.cols.append(self.rows)
        # self.print_cells()

    def generate_random_cells_alive(self):
        for cell in self.rows:
            chance = random.random()
            # 10% chance
            if chance*100 < 10:
                cell.alive = True

    def kill_cells(self):
        for cell in self.rows:
            cell.alive = False

    def print_cells(self):
        for cell in self.rows:
            print(cell.toString())
