from math import *
from tkinter import *

import os
import pygame

from models.Cells import Cells


class Board:
    # Configurations
    width = 800
    height = 600
    cellSize = 10
    numberOfCellGenerate = 750
    speed = 500

    # Data
    cellsX = int(floor(width / cellSize))
    cellsY = int(floor(height / cellSize))

    # Board's array
    cells = Cells(cellsX, cellsY, cellSize)

    # Create main windows
    windows = Tk()
    windows.title('Conway\'s Game of Life')
    windows.resizable(False, False)

    # get project's root
    ROOT_DIR = (os.path.dirname(os.path.abspath(__file__)))[0:-7]
    # pygame
    pygame.mixer.init()
    pygame.mixer.music.load(str(ROOT_DIR) + "/assets/music.mp3")
    pygame.mixer.music.set_volume(0.5)

    music = IntVar()
    music.set(0)

    # Canvas
    canvas = Canvas(windows, width=width, height=height, background='#bcbcbc')

    time = StringVar()
    counter = 0

    def generateBoard(self):

        self.canvas.pack(padx=5, pady=5)

        self.addTimer()
        self.addButtons()

        # self.cells.draw_spaceship_Glider()
        self.cells.generate_random_cells_alive(self.numberOfCellGenerate)

        self.timer()
        self.cycle()

        self.windows.mainloop()

    def addButtons(self):
        menubar = Menu(self.windows)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Glider", command=self.cells.draw_spaceship_Glider)
        menu1.add_command(label="Light-weight", command=self.windows.quit)
        menu1.add_separator()
        menu1.add_command(label="Heavy-weight", command=self.windows.quit)
        menubar.add_cascade(label="Spaceships", menu=menu1)

        self.windows.config(menu=menubar, padx=20, pady=20)

        btnClear = Button(self.windows, text='Clear cells', height=2, width=12, command=self.cells.kill_cells)
        btnClear.pack(side=LEFT, padx=5, pady=5)

        btnConfiguration = Button(self.windows, text='Configuration', height=2, width=12, command=self.windows.destroy)
        btnConfiguration.pack(side=LEFT, padx=5, pady=5)

        Checkbutton(self.windows, text="Music", variable=self.music, command=self.play_music).pack(side=LEFT, padx=5,
                                                                                                   pady=5)
        btnLeave = Button(self.windows, text='Leave', height=2, width=6, command=self.windows.destroy)
        btnLeave.pack(side=RIGHT, padx=5, pady=5)

    # Timer
    def timer(self):
        self.updateTimer()

        self.windows.after(1000, self.timer)

    def addTimer(self):
        Label(self.windows, textvariable=self.time).pack()

    def updateTimer(self):
        self.counter = self.counter + 1
        self.time.set(
            "{}\nCells alive: {}".format(self.formatTime(), self.cells.count_cells_alive()))

    def formatTime(self):
        h = floor(self.counter / 3600)
        m = floor((self.counter / 60))
        s = floor((self.counter % 60))

        if h < 10: h = '0' + str(h)
        if m < 10: m = '0' + str(m)
        if s < 10: s = '0' + str(s)

        return '{}:{}:{}'.format(h, m, s)

    def cycle(self):
        self.reDrawCanvas()
        self.windows.after(self.speed, self.cycle)

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
        for i in range(0, self.cells.cells_x_max):
            for y in range(0, self.cells.cells_y_max):
                if self.cells.cells2d[i][y].alive:
                    cell = self.cells.cells2d[i][y]
                    self.canvas.create_rectangle(cell.x, cell.y, cell.x + self.cellSize, cell.y + self.cellSize,
                                                 fill='black')

    def reDrawCanvas(self):
        self.canvas.delete(ALL)
        self.grid()

        self.cells.update_cell_state()

        self.show_cells_alive()

    def play_music(self):
        print(self.music.get())
        if self.music.get() == 1:
            # 1 (ON)
            # loop
            pygame.mixer.music.play(-1, 3)
        else:
            # 0 (OFF)
            pygame.mixer.music.stop()