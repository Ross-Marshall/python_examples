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


class GameOfLife:

    max_x = 1200
    max_y = 700
    step = 10
    start = 10
    line_width = 1
    win = None

    def __init__(self):
        pass

    def life_box(self, p1, p2):
        box = Rectangle(p1, p2)  # set endpoints
        box.setFill('black')
        box.draw(self.win)

    def draw_horizontal_lines(self):
        for y in range(self.start, self.max_y, self.step):
            px = Point(0, y)
            py = Point(self.max_x, y)
            line1 = Line(px, py)
            line1.setWidth(self.line_width)
            line1.draw(self.win)

    def draw_vertical_lines(self):
        for x in range(self.start, self.max_x, self.step):
            px = Point(x, 0)
            py = Point(x, self.max_y)
            line1 = Line(px, py)
            line1.setWidth(self.line_width)
            line1.draw(self.win)

    def draw_boxes(self):
        self.life_box(Point(10, 10), Point(20, 20))
        self.life_box(Point(100, 100), Point(110, 110))
        self.life_box(Point(240, 240), Point(250, 250))
        self.life_box(Point(500, 40), Point(510, 50))
        self.life_box(Point(340, 200), Point(350, 210))
        self.life_box(Point(700, 600), Point(710, 610))
        self.life_box(Point(900, 480), Point(910, 490))
        self.life_box(Point(1000, 600), Point(1010, 610))

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
            print('Point = ' + str(point))

    def main(self):

        self.win = GraphWin('Life Prototype', 1200, 700)  # give title and dimensions
        self.win.setCoords(0, 0, self.max_x, self.max_y)

        self.draw_horizontal_lines()
        self.draw_vertical_lines()

        self.draw_boxes()

        self.mouse_test()

        self.message_box()


if __name__ == '__main__':

    g = GameOfLife()
    g.main()
