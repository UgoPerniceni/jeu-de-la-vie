##Conway's Game of Life

####Introduction


The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. 
One interacts with the Game of Life by creating an initial configuration and observing how it evolves. 
It is Turing complete and can simulate a universal constructor or any other Turing machine.

####Rules

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


####Nota bene

This project was made in Python 3.8, with :
- [Tkinter](https://docs.python.org/fr/3/library/tkinter.html)
- [Pygame](https://www.pygame.org/news)
- [Numpy](https://numpy.org/)

You can find the documentation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).