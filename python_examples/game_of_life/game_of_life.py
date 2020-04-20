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
import time
import logging
import time


class GameOfLife:

    max_matrix_x = 5  # 120
    max_matrix_y = 3  # 70

    step = 10
    max_x = max_matrix_x * step
    max_y = max_matrix_y * step

    start = step
    line_width = 1
    win = None
    status_grid = None
    next_grid = None
    i = 0
    j = 0

    # Create logger
    logging.basicConfig(filename='life_log.log', level=logging.DEBUG)

    logger = logging.getLogger()

    def __init__(self):
        """Initialize the Class."""
        self.status_grid = self.initialze_status_grid()
        self.next_grid = self.initialze_status_grid()

    def initialze_status_grid(self):
        return [[0 for self.i in range(self.max_matrix_x)] for self.j in range(self.max_matrix_y)]

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
        j = j + self.step
        if j > self.max_y - self.step:
            j = 0
        return self.scale(j)

    def check_down_y(self, j):
        """Check y cell below the current cell."""
        j = j - self.step
        if j < 0:
            j = self.max_y - self.step
        return self.scale(j)

    def check_left_x(self, i):
        """Check the x cell to the left of the current cell."""
        i = i - self.step
        if i < 0:
            i = self.max_x - self.step
        return self.scale(i)

    def check_right_x(self, i):
        """Check the x cell to the right of the current cell."""
        i = i + self.step
        if i > self.max_x - self.step:
            i = 0
        return self.scale(i)

    def log_position(self, cell_name, x, y, i, j):
        rows = len(self.status_grid)
        cols = len(self.status_grid[0])
        self.logger.debug('status_grid [rows][columns] = ['+str(rows) + '][' + str(cols) + ']')
        self.logger.debug(cell_name +
                          ' : (x, y) = (' +
                          str(x) + ', ' +
                          str(y) + ')')
        self.logger.debug(cell_name +
                          ' : (i, j) = (' +
                          str(i) + ', ' +
                          str(j) + ')')
        self.logger.debug("(i,j) = (" + str(x) + "," + str(y) + ") " + str(self.status_grid))
        self.logger.debug('cell value = ' + str(self.status_grid[i][j]))

    def upper_left(self, x, y):
        """Get value of the upper left cell."""
        i, j = self.check_up_y(y), self.check_left_x(x)
        self.log_position('upper_left', x, y, i, j)
        return self.status_grid[i][j]

    def scale(self, v):
        return int(v/self.step)

    def above(self, x, y):
        """Get value of the cell above."""
        i, j = self.check_up_y(y), self.scale(x)
        self.log_position('above', x, y, i, j)
        return self.status_grid[i][j]

    def upper_right(self, x, y):
        """Get value of the upper right cell."""
        i, j = self.check_up_y(y), self.check_right_x(x)
        self.log_position('upper_right', x, y, i, j)
        return self.status_grid[i][j]

    def right(self, x, y):
        """Get value of the cell to the right."""
        i, j = self.scale(y), self.check_right_x(x)
        self.log_position('right', x, y, i, j)
        return self.status_grid[i][j]

    def lower_right(self, x, y):
        """Get value of the cell to the lower right"""
        i, j = self.check_down_y(y), self.check_right_x(x)
        self.log_position('lower_right', x, y, i, j)
        return self.status_grid[i][j]

    def below(self, x, y):
        """Get the value of the cell below."""
        i, j = self.check_down_y(y), self.scale(x)
        self.log_position('lower', x, y, i, j)
        return self.status_grid[i][j]

    def lower_left(self, x, y):
        """Get the value of the cell to the lower left."""
        i, j = self.check_down_y(y), self.check_left_x(x)
        self.log_position('lower left', x, y, i, j)
        return self.status_grid[i][j]

    def left(self, x, y):
        """Get the value of the cell to the left."""
        i, j = self.scale(y), self.check_left_x(x)
        self.log_position('left', x, y, i, j)
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
        """Update the grid array that keeps track of the state."""
        self.status_grid = self.next_grid
        for x in range(0, self.max_x - self.step, self.step):
            for y in range(0, self.max_y + self.step, self.step):
                self.logger.debug('------------------------------------')
                self.logger.debug('refresh_grid ===> x = ' + str(x) + ' y = ' + fmstr(y))
                low_point = Point(x, y)
                high_point = Point(x + self.step, y + self.step)
                if self.status_grid[x][y] == 1:
                    self.cell(low_point, high_point)
                else:
                    self.clear_cell(low_point, high_point)

    def mouse_test(self):
        setup_grid = 1
        while 1 == setup_grid:
            point = self.win.getMouse()
            low_point = Point(self.round_down(point.x), self.round_down(point.y))
            high_point = Point(self.round_up(point.x), self.round_up(point.y))
            self.logger.debug('low_point = ' + str(low_point) + ' high_point = ' + str(high_point))
            matrix_x = self.scale(low_point.x)
            matrix_y = self.scale(low_point.y)
            self.logger.debug('matrix_x = ' + str(matrix_x) + ' matrix_y= ' + str(matrix_y))
            self.show_grids()
            if self.status_grid[matrix_x][matrix_y] == 0:
                self.cell(low_point, high_point)
                self.status_grid[matrix_x][matrix_y] = 1
            else:
                self.clear_cell(low_point, high_point)
                self.status_grid[matrix_x][matrix_y] = 0
            if matrix_x == 0 and matrix_y == 0 and setup_grid == 1:
                for x in range(0, self.max_x + self.step, self.step):

                    for y in range(0, self.max_y + self.step, self.step):
                        self.logger.debug('-------------------- check neighbor loop ---------')
                        self.logger.debug('if matrix loop x = ' + str(x) + ' y = ' + str(y))
                        live = self.status_grid[self.scale(x)][self.scale(y)]
                        count = self.count_neighbors(x, y)
                        tkMessageBox.showinfo(title="Debug", message="(x,y) = (" + str(x) + ',' + str(y) +
                                                                     ') count = ' + str(count))
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
                setup_grid = 0
        while 1 == 1:
            self.refresh_grid()

    def show_grids(self):
        self.logger.debug('status_grid = ' + str(self.status_grid))
        self.logger.debug('next_grid   = ' + str(self.next_grid))

    def main(self):

        self.win = GraphWin('The Game Of Life', self.max_x, self.max_y)  # give title and dimensions
        self.win.setCoords(0, 0, self.max_x, self.max_y)

        self.draw_horizontal_lines()
        self.draw_vertical_lines()

        self.show_grids()

        # self.draw_boxes()

        self.mouse_test()

        self.message_box()


if __name__ == '__main__':

    g = GameOfLife()
    g.main()
