import time
from cell import Cell
import random


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
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            self.seed = random.seed(seed)
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
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cells(self.num_cols - 1, self.num_rows - 1)

    def _is_valid_cell(self, i, j):
        return 0 <= i < self.num_cols and 0 <= j < self.num_rows

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if (self._is_valid_cell(i, j-1) is True and
                    self._cells[i][j-1].visited is False):
                to_visit.append((i, j-1))
            if (self._is_valid_cell(i, j+1) is True and
                    self._cells[i][j+1].visited is False):
                to_visit.append((i, j+1))
            if (self._is_valid_cell(i-1, j) is True and
                    self._cells[i-1][j].visited is False):
                to_visit.append((i-1, j))
            if (self._is_valid_cell(i+1, j) is True and
                    self._cells[i+1][j].visited is False):
                to_visit.append((i+1, j))

            if len(to_visit) == 0:
                self._draw_cells(i, j)
                return
            else:
                destination = random.randrange(0, len(to_visit))
                u = to_visit[destination][0]
                v = to_visit[destination][1]
                if u < i:
                    self._cells[i][j].has_top_wall = False
                    self._cells[u][v].has_bottom_wall = False
                elif u > i:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[u][v].has_top_wall = False
                elif v < j:
                    self._cells[i][j].has_left_wall = False
                    self._cells[u][v].has_right_wall = False
                elif v > j:
                    self._cells[i][j].has_right_wall = False
                    self._cells[u][v].has_left_wall = False

                self._break_walls_r(u, v)

    def _reset_cells_visited(self):
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r()

    def _solve_r(self, i=0, j=0):
        # returns True if the current cell is an end cell OR leads to the end
        # returns False if current cell is a loser cell
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[-1][-1] == self._cells[i][j]:
            return True
        while True:
            to_visit = []
            if (self._is_valid_cell(i, j-1) is True and
                    self._cells[i][j-1].visited is False):
                to_visit.append((i, j-1))
            if (self._is_valid_cell(i, j+1) is True and
                    self._cells[i][j+1].visited is False):
                to_visit.append((i, j+1))
            if (self._is_valid_cell(i-1, j) is True and
                    self._cells[i-1][j].visited is False):
                to_visit.append((i-1, j))
            if (self._is_valid_cell(i+1, j) is True and
                    self._cells[i+1][j].visited is False):
                to_visit.append((i+1, j))

            if len(to_visit) == 0:
                return
            else:
                for cell in to_visit:
                    u = cell[0]
                    v = cell[1]
                    current = self._cells[i][j]
                    next = self._cells[u][v]
                    if u < i:
                        if (current.has_top_wall is False and
                                next.has_bottom_wall is False):
                            current.draw_move(next)
                            if self._solve_r(u, v) is True:
                                return True
                                break
                            else:
                                current.draw_move(next, undo=True)
                    if u > i:
                        if (current.has_bottom_wall is False and
                                next.has_top_wall is False):
                            current.draw_move(next)
                            if self._solve_r(u, v) is True:
                                return True
                                break
                            else:
                                current.draw_move(next, undo=True)
                    if v > j:
                        if (current.has_right_wall is False and
                                next.has_left_wall is False):
                            current.draw_move(next)
                            if self._solve_r(u, v) is True:
                                return True
                                break
                            else:
                                current.draw_move(next, undo=True)
                    if v < j:
                        if (current.has_left_wall is False and
                                next.has_right_wall is False):
                            current.draw_move(next)
                            if self._solve_r(u, v) is True:
                                return True
                                break
                            else:
                                current.draw_move(next, undo=True)
        return False
