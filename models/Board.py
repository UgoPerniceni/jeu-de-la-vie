from math import *
from tkinter import *

import os
import pygame

from models.Cells import Cells
from models.File import File


class Board:
    f = File()

    # get Configurations var
    if (f.getProp("width") is not None) and (400 < int(f.getProp("width")) < 1000):
        width = int(f.getProp("width"))
    else:
        width = 800

    if (f.getProp("height") is not None) and (400 < int(f.getProp("height")) < 1000):
        height = int(f.getProp("height"))
    else:
        height = 600

    if (f.getProp("cellSize") is not None) and (5 < int(f.getProp("cellSize")) < 50):
        cellSize = int(f.getProp("cellSize"))
    else:
        cellSize = 10

    if (f.getProp("numberOfCellGenerate") is not None) and (50 < int(f.getProp("numberOfCellGenerate")) < 2000):
        numberOfCellGenerate = int(f.getProp("numberOfCellGenerate"))
    else:
        numberOfCellGenerate = 750

    if (f.getProp("speed") is not None) and (50 < int(f.getProp("speed")) < 1000):
        speed = int(f.getProp("speed"))
    else:
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

        self.cells.generate_random_cells_alive(self.numberOfCellGenerate)

        self.timer()
        self.cycle()

        self.windows.mainloop()

    def addButtons(self):
        menubar = Menu(self.windows)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Glider", command=self.cells.draw_spaceship_glider)
        menu1.add_command(label="Light-weight", command=self.cells.draw_spaceship_light_weight)
        menu1.add_separator()
        menu1.add_command(label="Hammerhead", command=self.cells.draw_hammerhead)
        menubar.add_cascade(label="Spaceships", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Bee hive", command=self.cells.draw_still_life_bee_hive)
        menu2.add_command(label="Block", command=self.cells.draw_still_life_block)
        menu2.add_command(label="Boat", command=self.cells.draw_still_life_boat)
        menu2.add_command(label="Loaf", command=self.cells.draw_still_life_loaf)
        menu2.add_command(label="Tube", command=self.cells.draw_still_life_tube)
        menubar.add_cascade(label="Still Lifes", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Blinker", command=self.cells.draw_blinker)
        menu3.add_command(label="Beacon", command=self.cells.draw_oscillator_beacon)
        menu3.add_command(label="Penta Decathlon", command=self.cells.draw_oscillator_penta_decathlon)
        menu3.add_command(label="Pulsar", command=self.cells.draw_oscillator_pulsar)
        menu3.add_command(label="Toad", command=self.cells.draw_oscillator_toad)
        menubar.add_cascade(label="Oscillators", menu=menu3)

        menu4 = Menu(menubar, tearoff=0)
        menu4.add_command(label="Benjamin Raynal", command=self.cells.draw_special_benjamin)
        menu4.add_command(label="Gosper glider gun", command=self.cells.draw_special_gosper_glider_gun)
        menubar.add_cascade(label="Special forms", menu=menu4)

        self.windows.config(menu=menubar, padx=20, pady=20)

        btnGenerate = Button(self.windows, text='Generate', height=2, width=12,
                             command=self.cells.generate_random_cells_alive)
        btnGenerate.pack(side=LEFT, padx=5, pady=5)

        btnClear = Button(self.windows, text='Clear', height=2, width=12, command=self.cells.kill_cells)
        btnClear.pack(side=LEFT, padx=5, pady=5)

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
        # print(self.music.get())
        if self.music.get() == 1:
            # 1 (ON)
            # loop
            pygame.mixer.music.play(-1, 3)
        else:
            # # 0 (OFF)
            pygame.mixer.music.stop()
