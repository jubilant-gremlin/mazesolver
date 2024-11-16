from window import Window
from point import Point, Line
from cell import Cell

def main():
    window = Window(800, 600)
    cell1 = Cell(1, 50, 1, 50, window, has_right_wall=False)
    cell1.draw()
    window.wait_for_close()


main()
