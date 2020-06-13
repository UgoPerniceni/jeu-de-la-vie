from tkinter import *
from math import *


class Board:
    # Configurations
    width = 800
    height = 600

    # Create main windows
    windows = Tk()
    windows.title('Conway\'s Game of Life')

    time = StringVar()
    counter = 0

    def generateBoard(self):
        # Create widget Canvas
        canvas = Canvas(self.windows, width=self.width, height=self.height, background='white')
        canvas.pack(padx=5, pady=5)

        self.addTimer()
        self.addButtons()

        self.refreshTime()

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

    def addTimer(self):
        Label(self.windows, textvariable=self.time).pack()

    def formatTime(self):
        h = floor(self.counter / 3600)
        m = floor((self.counter / 60))
        s = floor((self.counter % 60))

        if h < 10: h = '0' + str(h)
        if m < 10: m = '0' + str(m)
        if s < 10: s = '0' + str(s)

        return '{}:{}:{}'.format(h, m, s)

    def refreshTime(self):
        self.counter = self.counter + 1
        self.time.set(self.formatTime())
        self.windows.after(1000, self.refreshTime)
