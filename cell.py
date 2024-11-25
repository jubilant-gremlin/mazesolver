from point import Point, Line


class Cell:
    def __init__(self, _x1, _x2, _y1, _y2, _win, has_left_wall=True,
                 has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.visited = False

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(self._x1, self._y2)
        left = Line(top_left, bottom_left)
        right = Line(top_right, bottom_right)
        top = Line(top_left, top_right)
        bottom = Line(bottom_left, bottom_right)

        if self.has_left_wall is True:
            left.draw(self._win.canvas, "black")
        elif self.has_left_wall is False:
            left.draw(self._win.canvas, "#d9d9d9")

        if self.has_right_wall is True:
            right.draw(self._win.canvas, "black")
        elif self.has_right_wall is False:
            right.draw(self._win.canvas, "#d9d9d9")

        if self.has_top_wall is True:
            top.draw(self._win.canvas, "black")
        elif self.has_top_wall is False:
            top.draw(self._win.canvas, "#d9d9d9")

        if self.has_bottom_wall is True:
            bottom.draw(self._win.canvas, "black")
        elif self.has_bottom_wall is False:
            bottom.draw(self._win.canvas, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1
        
        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        if undo is False:
            line.draw(self._win.canvas, "red")
        elif undo is True:
            line.draw(self._win.canvas, "#d9d9d9")
