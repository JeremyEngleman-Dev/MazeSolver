from tkinter import *
from window import *
from cell import *
from maze import *

def main():
    margin = 50
    num_rows = 15
    num_cols = 15
    cell_size = 100
    window_width = cell_size * num_cols + (margin * 2)
    window_height = cell_size * num_rows + (margin * 2)
    win = Window(window_width, window_height)
    new_maze = Maze(margin,margin,num_rows,num_cols,cell_size,cell_size,win)
    solveable = new_maze.solve()
    if solveable:
        print("The maze is solveable!")
    else:
        print("This maze is not solveable, sorry bro...")
    win.wait_for_close()

if __name__ == "__main__":
    main()