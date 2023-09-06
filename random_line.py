from graphics import *
import random
import time

width, hight = 1080, 720

win = GraphWin('Random Line', width, hight)
win.setBackground ('black')

#def drawPoint(x, y,color):
#    pt = Point(x,y)
#    pt.setFill(color)
#    pt.draw(win)

def BresenhamLine(x1,y1,x2,y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    grad = dy/float(dx)
    
    x, y = x1, y1
    
    if grad > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    p = 2*dy - dx

    win.plot(x,y,color=color)
#    drawPoint(x, y, color)
 
    for k in range(2, dx):
        if p>0:
            y = y + 1 if y<y2 else y - 1
            p = p + 2*(dy - dx)
        else:
            p = p + 2*dy
 
        x = x + 1 if x < x2 else x - 1
        
        time.sleep(0.005)
        win.plot(x,y,color=color)
#        drawPoint(x, y, color)

def main():
    for i in range(200):    
        r = random.randint(0,255)
        b = random.randint(0,255)
        g = random.randint(0,255)
        color = color_rgb(r, g, b)

        x1 = random.randint(0,width)
        y1 = random.randint(0,hight)
        x2 = random.randint(0,width)
        while(x2 == x1):
            x2 = random.randint(0,width)
        y2 = random.randint(0,hight)
        BresenhamLine(x1, y1, x2, y2, color)
        
if __name__ == "__main__":
    main()
