from window import Window
from point import Point, Line
from cell import Cell


def main():
    window = Window(800, 600)
    cell1 = Cell(0, 50, 0, 50, window)
    cell2 = Cell(50, 100, 50, 100, window)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2, undo=True)
    window.wait_for_close()


main()
