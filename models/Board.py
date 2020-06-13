from tkinter import *


class Board:
    # Configurations
    width = 800
    height = 600

    # Create main windows
    windows = Tk()
    windows.title('Conway\'s Game of Life')

    def generateBoard(self):
        # Create widget Canvas
        canvas = Canvas(self.windows, width=self.width, height=self.height, background='white')
        canvas.pack(padx=5, pady=5)

        self.addButtons()

        self.windows.mainloop()

    def addButtons(self):
        btnStart = Button(self.windows, text='Start', command=self.windows.destroy)
        btnStart.pack(side=LEFT, padx=5, pady=5)

        btnStop = Button(self.windows, text='Stop', command=self.windows.destroy)
        btnStop.pack(side=LEFT, padx=5, pady=5)

        btnConfiguration = Button(self.windows, text='Configuration', command=self.windows.destroy)
        btnConfiguration.pack(side=LEFT, padx=5, pady=5)

        btnLeave = Button(self.windows, text='Leave', command=self.windows.destroy)
        btnLeave.pack(side=RIGHT, padx=5, pady=5)