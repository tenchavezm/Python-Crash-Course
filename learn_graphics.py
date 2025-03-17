from graphics import *

def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 49)
    c.draw(win)
    win.getMouse()
    win.close()

main()