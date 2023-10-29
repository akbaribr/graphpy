from graphics import *
import math
import time


def main():
    win = GraphWin('Circle', 800, 800)
    win.setBackground('black')
    
    Xc = 400
    Yc = 400
    R = 300

    pi = math.pi
    cos = math.cos
    sin = math.sin

    t = 0
    while t<=2*pi:
        X = Xc + R*cos(t)
        Y = Yc - R*sin(t)
        pt = Point(X,Y)
        pt.setFill('green')
        pt.draw(win)
        time.sleep(0.0075)
        t = t+(1/R)
    
main()
