class Cell:
    id = 0

    def __init__(self, x, y, alive=False, cell_size=10):
        self.row = x
        self.col = y

        self.x = x * cell_size
        self.y = y * cell_size

        self.alive = alive

        Cell.id += 1
        self.id = Cell.id

    def set_alive(self):
        self.alive = True

    def to_string(self):
        return 'Cell n°{} (Cells[r: {}, c: {}], Position (X={}, Y={}),alive = {})'.format(self.id, self.row, self.col, self.x, self.y, self.alive)
