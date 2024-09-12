from cell import *
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            new_column = []
            for j in range(self.num_rows):
                new_column.append(Cell(self.win))
            self._cells.append(new_column)
        if self.win is None:
            return
        for i in self._cells:
            for j in i:
                column= self._cells.index(i)
                row = self._cells[column].index(j)
                self._draw_cell(row, column)

    def _draw_cell(self, i, j):
        if j == 0:
            x = self.x1
        else:
            x = (j * self.cell_size_x) + self.x1
        if i == 0:
            y = self.y1
        else:
            y = (i * self.cell_size_y) + self.y1
        self._cells[j][i]._x1 = x
        self._cells[j][i]._y1 = y
        self._cells[j][i]._x2 = x + self.cell_size_x
        self._cells[j][i]._y2 = y + self.cell_size_y
        self._cells[j][i].draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)