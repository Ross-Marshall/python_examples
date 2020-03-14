"""
From Wikipedia

The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970.[1]

The game is a zero-player game, meaning that its evolution is determined by
its initial state, requiring no further input. One interacts with the
Game of Life by creating an initial configuration and observing how it evolves.
It is Turing complete and can simulate a universal constructor or any
other Turing machine.

"""

from graphics import *
from Tkinter import *
import tkMessageBox
import math


class GameOfLife:

    max_x = 1200
    max_y = 700
    step = 10
    start = step
    line_width = 1
    win = None
    status_grid = [[0 for i in range(max_y)] for j in range(max_x)]

    def __init__(self):
        """Initialize the Class."""
        pass

    def round_up(self, x):
        """Round up to the nearest step-th"""
        return int(int(math.ceil(x / float(self.step))) * self.step)

    def round_down(self, x):
        """Round down to the nearest step-th"""
        return int(int(math.floor(x / float(self.step))) * self.step)

    def cell(self, p1, p2):
        """Draw the box."""
        box = Rectangle(p1, p2)  # set endpoints
        box.setFill('black')
        box.draw(self.win)

    def clear_cell(self, p1, p2):
        """Clear the box."""
        box = Rectangle(p1, p2)  # set endpoints
        box.setFill('gainsboro')
        box.draw(self.win)

    def draw_horizontal_lines(self):
        """Draw the horizontal lines in the window."""
        for y in range(self.start, self.max_y, self.step):
            px = Point(0, y)
            py = Point(self.max_x, y)
            line1 = Line(px, py)
            line1.setWidth(self.line_width)
            line1.draw(self.win)

    def draw_vertical_lines(self):
        """Draw the vertical lines in the window."""
        for x in range(self.start, self.max_x, self.step):
            px = Point(x, 0)
            py = Point(x, self.max_y)
            line1 = Line(px, py)
            line1.setWidth(self.line_width)
            line1.draw(self.win)

    def draw_boxes(self):
        """Proof of concept.  Draw cells on the grid"""
        self.cell(Point(10, 10), Point(20, 20))
        self.cell(Point(100, 100), Point(110, 110))
        self.cell(Point(240, 240), Point(250, 250))
        self.cell(Point(500, 40), Point(510, 50))
        self.cell(Point(340, 200), Point(350, 210))
        self.cell(Point(700, 600), Point(710, 610))
        self.cell(Point(900, 480), Point(910, 490))
        self.cell(Point(1000, 600), Point(1010, 610))

    @staticmethod
    def message_box():
        window = Tk()
        window.wm_withdraw()
        # message at x:200,y:200
        window.geometry("1x1+200+200")  # remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
        tkMessageBox.showerror(title="info", message="Click to Exit", parent=window)

    def mouse_test(self):
        while 1 == 1:
            point = self.win.getMouse()
            low_point = Point(self.round_down(point.x), self.round_down(point.y))
            high_point = Point(self.round_up(point.x), self.round_up(point.y))
            print('low_point = ' + str(low_point) + ' high_point = ' + str(high_point))
            matrix_x = int(low_point.x)
            matrix_y = int(low_point.y)
            if self.status_grid[matrix_x][matrix_y] == 0:
                self.cell(low_point, high_point)
                self.status_grid[matrix_x][matrix_y] = 1
            else:
                self.clear_cell(low_point, high_point)
                self.status_grid[matrix_x][matrix_y] = 0
            if matrix_x == 0 and matrix_y == 0:
                for x in range(self.max_x):
                    for y in range(self.max_y):
                        

    def main(self):

        self.win = GraphWin('Life Prototype', self.max_x, self.max_y)  # give title and dimensions
        self.win.setCoords(0, 0, self.max_x, self.max_y)
        self.win.setBackground = 'white'

        self.draw_horizontal_lines()
        self.draw_vertical_lines()

        # self.draw_boxes()

        self.mouse_test()

        self.message_box()


if __name__ == '__main__':

    g = GameOfLife()
    g.main()
