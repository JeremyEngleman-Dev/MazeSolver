from tkinter import Tk, BOTH, Canvas
from point import *

class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2)