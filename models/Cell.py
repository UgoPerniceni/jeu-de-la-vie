class Cell:
    id = 0

    def __init__(self, x, y, alive=False, cellSize=10):
        self.row = x
        self.col = y

        self.x = x * cellSize
        self.y = y * cellSize

        self.alive = alive

        Cell.id += 1
        self.id = Cell.id

    def toString(self):
        return 'Cell n°{} (Cells[{}, {}], Position (X={}Y={}),alive = {})'.format(self.id, self.row, self.col, self.x, self.y, self.alive)
