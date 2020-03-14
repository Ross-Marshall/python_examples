'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import *
from Tkinter import *
import tkMessageBox

def lifeBox(win, p1, p2):
    box = Rectangle(p1, p2)  # set endpoints
    box.setFill('black')
    box.draw(win)

def main():
    max_x = 1200
    max_y = 700
    step = 10
    win = GraphWin('Life Prototype', 1200, 700) # give title and dimensions
    win.setCoords(0, 0, 1200, 700)
    for y in range(10, max_y, step):
        px = Point(0, y)
        py = Point(1200, y)
        line1 = Line(px, py)
        line1.setWidth(1)
        line1.draw(win)

    for x in range(10, max_x, step):
        px = Point(x, 0)
        py = Point(x, 700)
        line1 = Line(px, py)
        line1.setWidth(1)
        line1.draw(win)

    lifeBox(win, Point(10, 10), Point(20, 20))
    lifeBox(win, Point(100, 100), Point(110, 110))
    lifeBox(win, Point(240, 240), Point(250, 250))
    lifeBox(win, Point(500, 40), Point(510, 50))
    lifeBox(win, Point(340, 200), Point(350, 210))

    window = Tk()
    window.wm_withdraw()

    # message at x:200,y:200
    window.geometry("1x1+200+200")  # remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
    tkMessageBox.showerror(title="info", message="Click to Exit", parent=window)


""" 
    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()
    """

main()