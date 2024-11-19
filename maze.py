import time
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
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
        for i in range(0, self.num_cols):
            new_list = []
            for j in range(0, self.num_rows):
                new_list.append(Cell(0, 0, 0, 0, self.win))
            self._cells.append(new_list)
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        cell = self._cells[i][j]
        if i == 0 and j == 0:
            cell._x1 = self.x1
            cell._x2 = self.x1 + self.cell_size_x
            cell._y1 = self.y1
            cell._y2 = self.y1 + self.cell_size_y
            cell.draw()
            self._animate()

        elif i == 0 and j > 0:
            previous = self._cells[i][j-1]
            cell._x1 = previous._x2
            cell._x2 = cell._x1 + self.cell_size_x
            cell._y1 = previous._y1
            cell._y2 = previous._y2
            cell.draw()
            self._animate()

        elif i > 0 and j == 0:
            previous = self._cells[i-1][j]
            cell._x1 = previous._x1
            cell._x2 = previous._x2 
            cell._y1 = previous._y2
            cell._y2 = cell._y1 + self.cell_size_y
            cell.draw()
            self._animate()

        elif i > 0 and j > 0:
            previous = self._cells[i-1][j-1]
            cell._x1 = previous._x2
            cell._x2 = cell._x1 + self.cell_size_x
            cell._y1 = previous._y2
            cell._y2 = cell._y1 + self.cell_size_y
            cell.draw()
            self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
    
