from math import *
from tkinter import *

import os
import pygame

from models.Cells import Cells
from models.FileInfos import FileInfos


class Board:
    def __init__(self):
        conf = FileInfos()
        # Get .conf variables
        self.width = conf.width
        self.height = conf.height
        self.cellSize = conf.cellSize
        self.numberOfCellGenerate = conf.numberOfCellGenerate
        self.speed = conf.speed

        # Data
        self.cellsX = int(floor(self.width / self.cellSize))
        self.cellsY = int(floor(self.height / self.cellSize))

        # Board's array
        self.cells = Cells(self.cellsX, self.cellsY, self.cellSize)

        # get project's root
        ROOT_DIR = (os.path.dirname(os.path.abspath(__file__)))[0:-7]

        # Create main windows
        self.windows = Tk()
        self.windows.title('Conway\'s Game of Life')
        self.windows.resizable(False, False)

        # Pygame music
        pygame.mixer.init()
        pygame.mixer.music.load(str(ROOT_DIR) + "/assets/music.mp3")
        pygame.mixer.music.set_volume(0.5)

        self.music = IntVar()
        self.music.set(0)

        # Canvas
        self.canvas = Canvas(self.windows, width=self.width, height=self.height, background='#bcbcbc')

        self.time = StringVar()
        self.counter = 0

    def generate_board(self):
        self.canvas.pack(padx=5, pady=5)

        self.add_timer()
        self.add_buttons()

        self.cells.generate_random_cells_alive(self.numberOfCellGenerate)

        self.timer()
        self.cycle()

        self.windows.mainloop()

    def add_buttons(self):
        menubar = Menu(self.windows)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Glider", command=self.cells.draw_spaceship_glider)
        menu1.add_command(label="Light-weight", command=self.cells.draw_spaceship_light_weight)
        menu1.add_command(label="Hammerhead", command=self.cells.draw_spaceship_hammerhead)
        menubar.add_cascade(label="Spaceships", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Bee hive", command=self.cells.draw_still_life_bee_hive)
        menu2.add_command(label="Block", command=self.cells.draw_still_life_block)
        menu2.add_command(label="Boat", command=self.cells.draw_still_life_boat)
        menu2.add_command(label="Loaf", command=self.cells.draw_still_life_loaf)
        menu2.add_command(label="Tube", command=self.cells.draw_still_life_tube)
        menubar.add_cascade(label="Still Lifes", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Blinker", command=self.cells.draw_oscillator_blinker)
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
        self.update_timer()
        self.windows.after(1000, self.timer)

    def add_timer(self):
        Label(self.windows, textvariable=self.time).pack()

    def update_timer(self):
        self.counter = self.counter + 1
        self.time.set(
            "{}\nCells alive: {}".format(self.format_time(), self.cells.count_cells_alive()))

    def format_time(self):
        h = floor(self.counter / 3600)
        m = floor((self.counter / 60))
        s = floor((self.counter % 60))

        if h < 10: h = '0' + str(h)
        if m < 10: m = '0' + str(m)
        if s < 10: s = '0' + str(s)

        return '{}:{}:{}'.format(h, m, s)

    def cycle(self):
        self.draw_canvas()
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

    def draw_canvas(self):
        self.canvas.delete(ALL)
        self.grid()

        self.cells.update_cell_state()
        self.show_cells_alive()

    def play_music(self):
        # print(self.music.get())
        if self.music.get() == 1:
            # 1 (ON) loop
            pygame.mixer.music.play(-1, 3)
        else:
            # 0 (OFF)
            pygame.mixer.music.stop()
