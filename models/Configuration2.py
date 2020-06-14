import tkinter as tk
from tkinter import ttk
import models.Start
import models.Configuration


class Configuration2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Configuration page 2")
        label.grid(row=0, column=4, padx=10, pady=10)

        game_button = ttk.Button(self, text="Go To Game", command=lambda: controller.show_frame(models.Configuration.Configuration))
        game_button.grid(row=2, column=1, padx=10, pady=10)
