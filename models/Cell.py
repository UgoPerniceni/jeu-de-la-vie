class Cell:
    def __init__(self, x, y, alive=False):
        self.x = x
        self.y = y
        self.alive = alive

    def toString(self):
        return 'x = {}, y = {}, state = {}'.format(self.x, self.y, self.alive)
