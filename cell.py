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

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(self._x1, self._y2)

        if self.has_left_wall is True:
            left = Line(top_left, bottom_left)
            left.draw(self._win.canvas, "black")
        if self.has_right_wall is True:
            right = Line(top_right, bottom_right)
            right.draw(self._win.canvas, "black")
        if self.has_top_wall is True:
            top = Line(top_left, top_right)
            top.draw(self._win.canvas, "black")
        if self.has_bottom_wall is True:
            bottom = Line(bottom_left, bottom_right)
            bottom.draw(self._win.canvas, "black")

    def draw_move(self, to_cell, undo=False):
        center = Point(self._x2/2, self._y2/2)
        center_to = Point((to_cell._x2/2)+(self._x2/2),
                          (to_cell._y2/2)+(self._y2/2))
        line = Line(center, center_to)
        if undo is False:
            line.draw(self._win.canvas, "red")
        elif undo is True:
            line.draw(self._win.canvas, "gray")
