from line import *
from point import *
from window import *

class Cell:
    def  __init__(self, window: Window = None, x1=0, y1=0, x2=0, y2=0, left=True, right=True, top=True, bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window

    def draw(self):
        if self._win is None:
            return
        if self.has_left_wall:
            Line(Point(self._x1,self._y1), Point(self._x1, self._y2)).draw(self._win.canvas, "black")
        if self.has_right_wall:
            Line(Point(self._x2,self._y1), Point(self._x2, self._y2)).draw(self._win.canvas, "black")
        if self.has_top_wall:
            Line(Point(self._x1,self._y1), Point(self._x2, self._y1)).draw(self._win.canvas, "black")
        if self.has_bottom_wall:
            Line(Point(self._x1,self._y2), Point(self._x2, self._y2)).draw(self._win.canvas, "black")

    def draw_move(self, to_cell: 'Cell', undo=False):
        if self._win is None:
            return
        if undo:
            color = "gray"
        else:
            color = "red"
        def get_middle(first, second):
            return round((first + second) / 2)
        Line(Point(get_middle(self._x1, self._x2), get_middle(self._y1, self._y2)), Point(get_middle(to_cell._x1, to_cell._x2), get_middle(to_cell._y1, to_cell._y2))).draw(self._win.canvas, color)
