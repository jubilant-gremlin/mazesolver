import unittest

from maze import Maze

from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        window = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
                len(m1._cells),
                num_cols,
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 3
        num_rows = 7
        window = Window(400, 200)
        m1 = Maze(0, 0, num_rows, num_cols, 15, 15, window)
        self.assertEqual(
                len(m1._cells),
                num_cols,
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        window = Window(400, 200)
        m1 = Maze(2, 2, num_rows, num_cols, 40, 40, window)
        m1._break_entrance_and_exit()
        self.assertEqual(
                m1._cells[0][0].has_top_wall,
                False,
        )
        self.assertEqual(
                m1._cells[-1][-1].has_bottom_wall,
                False,
        )

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        window = Window(400, 200)
        m1 = Maze(2, 2, num_rows, num_cols, 40, 40, window)
        for i in range(0, len(m1._cells)):
            for j in range(0, len(m1._cells[i])):
                self.assertEqual(m1._cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
