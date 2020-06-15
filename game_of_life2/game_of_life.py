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

import sys, pygame
from pygame.locals import*

import time
import math
import logging
from Point import Point

class GameOfLife:

    max_matrix_x = 50  # 120
    max_matrix_y = 30  # 70

    step = 10

    Color_screen = (49, 150, 170)
    Color_line = (0, 0, 0)
    screen = None

    max_x = max_matrix_x * step
    max_y = max_matrix_y * step

    start = step
    line_width = 1
    win = None
    status_grid = None
    next_grid = None
    changed_items = []
    i = 0
    j = 0
    generation = 0

    # Create logger
    logging.basicConfig(filename='life_log.log', level=logging.INFO)

    logger = logging.getLogger()

    def __init__(self):
        """Initialize the Class."""
        self.status_grid = self.initialze_status_grid()
        self.next_grid = self.initialze_status_grid()

    def initialze_status_grid(self):
        return [[0 for self.j in range(self.max_matrix_y)] for self.i in range(self.max_matrix_x)]

    def round_up(self, x):
        """Round up to the nearest step-th"""
        return int(int(math.ceil(x / float(self.step))) * self.step)

    def round_down(self, x):
        """Round down to the nearest step-th"""
        return int(int(math.floor(x / float(self.step))) * self.step)

    def cell(self, p1, p2):
        """Draw the box."""
        """box = Rectangle(p1, p2)  # set endpoints
        box.setFill('black')
        box.draw(self.win)"""
        rect = Rect(p1.x, p2.y, self.step, self.step)
        pygame.draw.rect(self.screen, self.Color_line, rect, 0)
        pygame.display.flip()

    def clear_cell(self, p1, p2):
        """Clear the box."""
        """box = Rectangle(p1, p2)  # set endpoints
        box.setFill('gainsboro')
        box.draw(self.win)"""
        rect = Rect(p1.x, p2.y, self.step, self.step)
        pygame.draw.rect(self.screen, self.Color_screen, rect, 0)
        pygame.display.flip()

    def draw_horizontal_lines(self):
        """Draw the horizontal lines in the window."""
        for y in range(self.start, self.max_y, self.step):
            """px = point(0, y)
            py = point(self.max_x, y)
            line1 = Line(px, py)
            line1.setWidth(self.line_width)
            line1.draw(self.win)"""

            pygame.draw.line(self.screen, self.Color_line, (0, y), (self.max_x, y))
            #pygame.display.flip()

    def draw_vertical_lines(self):
        """Draw the vertical lines in the window."""
        for x in range(self.start, self.max_x, self.step):
            """px = point(x, 0)
            py = point(x, self.max_y)
            line1 = Line(px, py)
            line1.setWidth(self.line_width)
            line1.draw(self.win)"""
            pygame.draw.line(self.screen, self.Color_line, (x, 0), (x, self.max_y))
            #pygame.display.flip()

    #"""def draw_boxes(self):"""
    #    """Proof of concept.  Draw cells on the grid"""
    #    """self.cell(point(10, 10), point(20, 20))
    #    self.cell(point(100, 100), point(110, 110))
    #    self.cell(point(240, 240), point(250, 250))
    #    self.cell(point(500, 40), point(510, 50))
    #    self.cell(point(340, 200), point(350, 210))
    #    self.cell(point(700, 600), point(710, 610))
    #    self.cell(point(900, 480), point(910, 490))
    #    self.cell(point(1000, 600), point(1010, 610))"""

    @staticmethod
    def message_box():
        pass
        #window = Tk()
        #window.wm_withdraw()
        # message at x:200,y:200
        #window.geometry("1x1+200+200")  # remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
        #tkMessageBox.showerror(title="info", message="Click to Exit", parent=window)

    #@staticmethod
    #def point(x, y):
    #    return x, y

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
        """Check the y cell to the left of the current cell."""
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

    def scale(self, v):
        return int(v/self.step)

    def upper_left(self, x, y):
        """Get value of the upper left cell."""
        j, i = self.check_up_y(y), self.check_left_x(x)
        return self.status_grid[i][j]

    def above(self, x, y):
        """Get value of the cell above."""
        j, i = self.check_up_y(y), self.scale(x)
        return self.status_grid[i][j]

    def upper_right(self, x, y):
        """Get value of the upper right cell."""
        j, i = self.check_up_y(y), self.check_right_x(x)
        # self.log_position('upper_right', x, y, i, j)
        return self.status_grid[i][j]

    def right(self, x, y):
        """Get value of the cell to the right."""
        j, i = self.scale(y), self.check_right_x(x)
        return self.status_grid[i][j]

    def lower_right(self, x, y):
        """Get value of the cell to the lower right"""
        j, i = self.check_down_y(y), self.check_right_x(x)
        return self.status_grid[i][j]

    def below(self, x, y):
        """Get the value of the cell below."""
        j, i = self.check_down_y(y), self.scale(x)
        return self.status_grid[i][j]

    def lower_left(self, x, y):
        """Get the value of the cell to the lower left."""
        j, i = self.check_down_y(y), self.check_left_x(x)
        return self.status_grid[i][j]

    def left(self, x, y):
        """Get the value of the cell to the left."""
        j, i = self.scale(y), self.check_left_x(x)
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
        # for y in range(0, self.max_y - self.step, self.step):
        #     for x in range(0, self.max_x - self.step, self.step):
        for point in self.changed_items:
            x = point[0]
            y = point[1]
            low_point = Point(x, y)
            high_point = Point(x + self.step, y + self.step)
            if self.status_grid[self.scale(x)][self.scale(y)] == 1:
                self.cell(low_point, high_point)
            else:
                self.clear_cell(low_point, high_point)

        """def refresh_grid(self):"""
        """Update the grid array that keeps track of the state."""
        """self.status_grid = self.next_grid
        for y in range(0, self.max_y - self.step, self.step):
            for x in range(0, self.max_x - self.step, self.step):
                low_point = point(x, y)
                high_point = point(x + self.step, y + self.step)
                if self.status_grid[self.scale(x)][self.scale(y)] == 1:
                    self.cell(low_point, high_point)
                else:
                    self.clear_cell(low_point, high_point)"""

    def next_generation(self):
        self.next_grid = self.initialze_status_grid()
        for y in range(0, self.max_y, self.step):
            for x in range(0, self.max_x, self.step):
                x_scale = self.scale(x)
                y_scale = self.scale(y)
                #  live = self.status_grid[self.scale(x_scale)][self.scale(y_scale)]
                live = self.status_grid[x_scale][y_scale]
                count = self.count_neighbors(x, y)
                if live == 1 and count < 2:
                    self.next_grid[x_scale][y_scale] = 0
                elif live == 1 and count > 3:
                    self.next_grid[x_scale][y_scale] = 0
                elif live == 1 and count in [2, 3]:
                    self.next_grid[x_scale][y_scale] = self.status_grid[x_scale][y_scale]
                elif live == 0 and count == 3:
                    self.next_grid[x_scale][y_scale] = 1
                else:
                    self.next_grid[x_scale][y_scale] = self.status_grid[x_scale][y_scale]

                if live != self.next_grid[x_scale][y_scale]:
                    self.changed_items.append([x, y])
        return

    def update_grid(self, setup_grid):
        while True:
            ev = pygame.event.get()

            # proceed events
            for event in ev:

                matrix_x = 0
                matrix_y = 0

                # handle MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    # pos = pygame.mouse.get_pos()

                    # get a list of all sprites that are under the mouse cursor
                    #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
                    # do something with the clicked sprites...
                    point = pygame.mouse.get_pos()
                    low_point = Point(self.round_down(point[0]), self.round_down(point[1]))
                    high_point = Point(self.round_up(point[0]), self.round_up(point[1]))
                    matrix_x = self.scale(low_point.x)
                    matrix_y = self.scale(low_point.y)
                    self.show_grids()

                    #if setup_grid == 0:
                    if self.status_grid[matrix_x][matrix_y] == 0:
                        self.cell(low_point, high_point)
                        self.status_grid[matrix_x][matrix_y] = 1
                    else:
                        self.clear_cell(low_point, high_point)
                        self.status_grid[matrix_x][matrix_y] = 0

                    if matrix_x == 0 and matrix_y == 0 and setup_grid == 1:
                        self.next_generation()
                        return


    def mouse_test(self):
        setup_grid = 1

        self.update_grid(setup_grid)
        self.refresh_grid()
        setup_grid = 0

        while True:
            self.logger.info('Generation: ' + str(self.generation))
            self.next_generation()
            self.refresh_grid()
            self.generation += 1

    def show_grids(self):
        self.logger.debug('status_grid = ' + str(self.status_grid))
        self.logger.debug('next_grid   = ' + str(self.next_grid))

    def main(self):

        """self.win = GraphWin('The Game Of Life', self.max_x, self.max_y)  # give title and dimensions
        self.win.setCoords(0, 0, self.max_x, self.max_y)
        self.show_grids()"""

        self.screen = pygame.display.set_mode((self.max_x, self.max_y))
        self.screen.fill(self.Color_screen)

        #self.draw_horizontal_lines()
        #self.draw_vertical_lines()
        #pygame.display.flip()


        """while True:
            for events in pygame.event.get():
                if events.type == QUIT:
                    sys.exit(0)"""

        #time.sleep(10)
        #self.message_box()
        # self.draw_boxes()

        self.mouse_test()




if __name__ == '__main__':

    g = GameOfLife()
    g.main()
