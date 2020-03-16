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

    max_x = 200  #  1200
    max_y = 100  # 700
    step = 10
    start = step
    line_width = 1
    win = None
    status_grid = None
    next_grid = None
    i = 0
    j = 0

    def __init__(self):
        """Initialize the Class."""
        self.status_grid = self.initialze_status_grid()
        self.next_grid = self.initialze_status_grid()

    def initialze_status_grid(self):
        return [[0 for self.i in range(self.max_y)] for self.j in range(self.max_x)]

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

    def check_up_y(self, j):
        """Check y cell above the current cell."""
        j = j + 1
        if j > self.max_y - self.step:
            j = 0
        return j

    def check_down_y(self, j):
        """Check y cell below the current cell."""
        j = j + 1
        if j < 0:
            j = self.max_y - self.step
        return j

    def check_left_x(self, i):
        """Check the x cell to the left of the current cell."""
        i = i - 1
        if i < 0:
            i = self.max_x - self.step
        return i

    def check_right_x(self, i):
        """Check the x cell to the right of the current cell."""
        i = i + 1
        if i > self.max_x - self.step:
            i = 0
        return i

    def upper_left(self, x, y):
        """Get value of the upper left cell."""
        print('DEBUG x = ' + str(x) + ' y = ' + str(y))
        i = self.check_left_x(x)
        j = self.check_up_y(y)
        print('DEBUG i = ' + str(i) + ' j = ' + str(j))
        return self.status_grid[i][j]

    def above(self, x, y):
        """Get value of the cell above."""
        i = x
        j = self.check_up_y(y)
        return self.status_grid[i][j]

    def upper_right(self, x, y):
        """Get value of the upper right cell."""
        i = self.check_right_x(x)
        j = self.check_up_y(y)
        return self.status_grid[i][j]

    def right(self, x, y):
        """Get value of the cell to the right."""
        i = self.check_right_x(x)
        j = y
        return self.status_grid[i][j]

    def lower_right(self, x, y):
        """Get value of the cell to the lower right"""
        i = self.check_right_x(x)
        j = self.check_down_y(y)
        print('DEBUG i = ' + str(i))
        print('DEBUG j = ' + str(j))
        return self.status_grid[i][j]

    def below(self, x, y):
        """Get the value of the cell below."""
        i = x
        j = self.check_down_y(y)
        return self.status_grid[i][j]

    def lower_left(self, x, y):
        """Get the value of the cell to the lower left."""
        i = self.check_left_x(x)
        j = self.check_down_y(y)
        return self.status_grid[i][j]

    def left(self, x, y):
        """Get the value of the cell to the left."""
        i = self.check_left_x(x)
        j = y
        return self.status_grid[i][j]

    def count_neighbors(self, x, y):
        """Count the number of active surrounding the cell."""
        neighbor_count = sum([self.upper_left(x, y),
                              self.above(x, y),
                              self.upper_right(x, y),
                              self.right(x, y),
                              self.lower_right(x, y),
                              self.below(x, y),
                              self.lower_left(x, y),
                              self.left(x, y)])
        return neighbor_count

    def refresh_grid(self):
        self.status_grid = self.next_grid
        for x in range(0, self.max_x - self.step, self.step):
            for y in range(0, self.max_y - self.step, self.step):
                low_point = Point(x, y)
                high_point = Point(x + 10, y + 10)
                if self.status_grid[x][y] == 1:
                    self.cell(low_point, high_point)
                else:
                    self.clear_cell(low_point, high_point)

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
                        live = self.status_grid[x][y]
                        count = self.count_neighbors(x, y)
                        if count < 2 and live == 1:
                            self.next_grid[x][y] = 0
                        elif count in [2, 3] and live == 1:
                            self.next_grid[x][y] = 1
                        elif count > 3 and live == 1:
                            self.next_grid[x][y] = 0
                        elif count == 3 and live == 0:
                            self.next_grid[x][y] = 1
                        else:
                            self.next_grid[x][y] = self.status_grid[x][y]
                self.refresh_grid()

    def main(self):

        self.win = GraphWin('The Game Of Life', self.max_x, self.max_y)  # give title and dimensions
        self.win.setCoords(0, 0, self.max_x, self.max_y)

        self.draw_horizontal_lines()
        self.draw_vertical_lines()

        # self.draw_boxes()

        self.mouse_test()

        self.message_box()


if __name__ == '__main__':

    g = GameOfLife()
    g.main()
