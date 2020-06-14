import tkinter as tk
import models.Configuration
import models.Configuration2


class Start(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=1280, height=720)
        container.pack(fill=None, expand=False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (models.Configuration.Configuration, models.Configuration2.Configuration2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(models.Configuration.Configuration)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
