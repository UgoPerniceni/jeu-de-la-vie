import tkinter as tk
from tkinter import ttk
from math import *
import models.Start
import models.Board
import models.Configuration2


class Configuration(tk.Frame):

    height = models.Board.Board.height
    width = models.Board.Board.width
    cell = models.Board.Board.cell = 0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        height_label = ttk.Label(self, text="Canvas height :")
        height_label.grid(row=1, column=0)

        height_value = ttk.Entry(self)
        height_value.grid(row=1, column=1, padx=10, pady=10)
        height_value.insert(0, self.height)

        width_label = ttk.Label(self, text="Canvas width :")
        width_label.grid(row=2, column=0)

        width_value = ttk.Entry(self)
        width_value.grid(row=2, column=1, padx=10, pady=10)
        width_value.insert(0, self.width)

        cell_label = ttk.Label(self, text="Cell size :")
        cell_label.grid(row=3, column=0)

        cell_value = ttk.Entry(self)
        cell_value.grid(row=3, column=1, padx=10, pady=10)
        cell_value.insert(0, self.cell)

        game_button = ttk.Button(self, text="Go To Game", command=lambda: controller.show_frame(models.Configuration2.Configuration2))
        game_button.grid(row=4, column=2)
