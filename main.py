from tkinter import *
from window import *
from cell import *
from maze import *

def main():
    win = Window(1800, 1600)
    num_rows = 10
    num_cols = 12
    new_maze = Maze(0,0,num_rows,num_cols,100,100)
    print(f"COLUMNS: {len(new_maze._cells)}")
    print(f"ROWS: {len(new_maze._cells[0])}")
    win.wait_for_close()

if __name__ == "__main__":
    main()