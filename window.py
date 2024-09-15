from tkinter import Tk, BOTH, Canvas
from point import *
from line import *

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.running_state = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running_state = True
        while self.running_state == True:
            self.redraw()

    def close(self):
        self.running_state = False

    def draw_line(self, line: Line, fill_color = "black"):
        line.draw(self.canvas, fill_color)