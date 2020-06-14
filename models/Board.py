from tkinter import *
from math import *

from models.Cells import Cells


class Board:
    # Configurations
    width = 800
    height = 600
    cellSize = 10

    animation = True

    # Data
    cellsX = int(floor(width / cellSize))
    cellsY = int(floor(height / cellSize))

    # Board's array
    cells = Cells(cellsX, cellsY, cellSize)
    cells.generate_random_cells_alive()
    # cells.print_cells()

    # Create main windows
    windows = Tk()
    windows.title('Conway\'s Game of Life')

    # Canvas
    canvas = Canvas(windows, width=width, height=height, background='#bcbcbc')

    time = StringVar()
    counter = 0

    def generateBoard(self, animation=True):
        # Create grid
        self.grid()
        self.canvas.pack(padx=5, pady=5)

        self.addTimer()
        self.addButtons()

        self.cycle()

        self.windows.mainloop()

    def addButtons(self):
        btnStart = Button(self.windows, text='🞂', height=2, width=6, command=self.windows.destroy)
        btnStart.pack(side=LEFT, padx=5, pady=5)

        btnPause = Button(self.windows, text='⏸', height=2, width=6, command=self.windows.destroy)
        btnPause.pack(side=LEFT, padx=5, pady=5)

        btnStop = Button(self.windows, text='⏹', height=2, width=6, command=self.windows.destroy)
        btnStop.pack(side=LEFT, padx=5, pady=5)

        btnConfiguration = Button(self.windows, text='Configuration', height=2, width=12, command=self.windows.destroy)
        btnConfiguration.pack(side=RIGHT, padx=5, pady=5)

        btnLeave = Button(self.windows, text='Leave', height=2, width=6, command=self.windows.destroy)
        btnLeave.pack(side=RIGHT, padx=5, pady=5)

    # Timer
    def addTimer(self):
        Label(self.windows, textvariable=self.time).pack()

    def updateTimer(self):
        self.counter = self.counter + 1
        self.time.set("{}\nCells alive: {}\n Cycle {}". format(self.formatTime(), self.cells.count_cells_alive(), self.counter))

    def formatTime(self):
        h = floor(self.counter / 3600)
        m = floor((self.counter / 60))
        s = floor((self.counter % 60))

        if h < 10: h = '0' + str(h)
        if m < 10: m = '0' + str(m)
        if s < 10: s = '0' + str(s)

        return '{}:{}:{}'.format(h, m, s)

    def cycle(self):
        self.updateTimer()

        self.reDrawCanvas()

        self.windows.after(1000, self.cycle)

    def grid(self):
        x = 0
        y = 0

        while x < self.cellsX:
            self.canvas.create_line(x * self.cellSize, 0, x * self.cellSize, self.height, width=1, fill='black')
            x += 1

        while y < self.cellsY:
            self.canvas.create_line(0, y * self.cellSize, self.width, y * self.cellSize, width=1, fill='black')
            y += 1

    def show_cells_alive(self):
        for cell in self.cells.rows:
            if cell.alive:
                self.canvas.create_rectangle(cell.x, cell.y, cell.x + self.cellSize, cell.y + self.cellSize,
                                             fill='black')

    def reDrawCanvas(self):
        self.canvas.delete(ALL)
        self.grid()

        self.cells.kill_cells()
        self.cells.generate_random_cells_alive()

        self.show_cells_alive()
