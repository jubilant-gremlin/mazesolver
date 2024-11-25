from window import Window
from point import Point, Line
from cell import Cell
from maze import Maze


def main():
    window = Window(800, 600)
    maze = Maze(2, 2, 7, 5, 50, 50, window)
    maze.solve()
    window.wait_for_close()


main()
