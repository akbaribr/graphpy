from graphics import *
import math

pi = math.pi
sin = math.sin
cos = math.cos

# Sutherland-Hodgman polygon clipping
# receives input subjectPolygon which is an array of polygons to be clipped
# and clipPolygon which is an array of frames
# with the form of an array [(x1,y1),(x2,y2),(xn,yn)]

def clip(subjectPolygon, clipPolygon):
   def inside(p):
      return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
 
   def computeIntersection():
      dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
      dp = [ s[0] - e[0], s[1] - e[1] ]
      n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
      n2 = s[0] * e[1] - s[1] * e[0] 
      n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
      return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
 
   outputList = subjectPolygon
   cp1 = clipPolygon[-1]
 
   for clipVertex in clipPolygon:
      cp2 = clipVertex
      inputList = outputList
      outputList = []
      s = inputList[-1]
 
      for subjectVertex in inputList:
         e = subjectVertex
         if inside(e):
            if not inside(s):
               outputList.append(computeIntersection())
            outputList.append(e)
         elif inside(s):
            outputList.append(computeIntersection())
         s = e
      cp1 = cp2
   return(outputList)

# x and y conversion from coordinates to viewport
def c_to_v(xc,yc):
    xcmin = -10; xcmax = 10; ycmin = -10; ycmax = 10
    xvmin = 100; xvmax = 500; yvmin = 100; yvmax = 500

    # frame polygon array, i.e. a viewport formed by
    batas = [(100,100),(500,100),(500,500),(100,500)]

    n = len(xc)
    cxv=[0]*n; cyv=[0]*n; pv=[0]*n
    for i in range(0,n):
        cxv[i] = xvmin + (xc[i] - xcmin)*(xvmax-xvmin)/(xcmax-xcmin)
        cyv[i] = 600-(yvmin + (yc[i] - ycmin)*(yvmax-yvmin)/(ycmax-ycmin))
        #600-nilai untuk menyesuaikan letak y agar dari bawah ke atas

        pv[i] = (cxv[i],cyv[i])
        
    pvc = clip(pv,batas) #melakukan clipping terhadap titik2 polygon dengan bingkai batas(viewport)
    k = len(pvc)

    #membentuk array polygon dengan format [Point(x1,y1),Point(x2,y2),Point(xn,yn)]
    #agar bisa di-draw
    pvclipped = [0]*k
    for i in range(0,k):
        pvclipped[i] = Point(pvc[i][0],pvc[i][1])

    return pvclipped

#membuat polygon dari array x dan array y
def createpolygon(arrx,arry,win,fill):
    n = len(arrx)
    vertices = [0]*n

    pv = c_to_v(arrx,arry) #memanggil c_to_v untuk konversi nilai koordinat ke viewport

    obj = Polygon(pv)
    obj.setFill(fill)
    obj.setOutline('white')
    obj.draw(win)
   
def rotate(x,y,win,t):
    n = len(x)
    cxt=[0]*n; cyt=[0]*n
    for i in range(0,n):
        cxt[i] = x[i]*cos(t*pi/180)-y[i]*sin(t*pi/180)
        cyt[i] = x[i]*sin(t*pi/180)+y[i]*cos(t*pi/180)
        
    createpolygon(cxt,cyt,win,'blue') #membuat polygon baru dengan titik2 yg telah dirotasi
    pt = [cxt,cyt]
    return pt

def scale(x,y,win,sx,sy):
    n = len(x)
    cxs=[0]*n; cys=[0]*n
    for i in range(0,n):
        cxs[i] = x[i]*sx
        cys[i] = y[i]*sy

    createpolygon(cxs,cys,win,'green') #membuat polygon baru dengan titik2 yg telah discale
    ps = [cxs,cys]
    return ps

def shearx(x,y,win,shx):
    n = len(x)
    cxsh=[0]*n; cysh=[0]*n
    for i in range(0,n):
        cxsh[i] = x[i]+shx*y[i]
        cysh[i] = y[i]

    createpolygon(cxsh,cysh,win,'red') #membuat polygon baru dengan titik2 yg dishear trhadap x
    psh = [cxsh,cysh]
    return psh   

def sheary(x,y,win,shy):
    n = len(x)
    cxsh=[0]*n; cysh=[0]*n
    for i in range(0,n):
        cxsh[i] = x[i]
        cysh[i] = y[i]+shy*x[i]

    createpolygon(cxsh,cysh,win,'red') #membuat polygon baru dengan titik2 yg dishear trhadap y
    psh = [cxsh,cysh]
    return psh

def main():
    win = GraphWin('Clip', 600, 600)

    vp = Rectangle(Point(100,100), Point(500,500))
    vp.setOutline('red')
    vp.setFill('black')
    vp.draw(win)

    sbx = Line(Point(100,300), Point(500,300)); sbx.setOutline('white')
    sbx.draw(win)
    sby = Line(Point(300,100), Point(300,500)); sby.setOutline('white')
    sby.draw(win)

#koordinat objek dalam array x dan y
    cx=[1,1.25,1.75,1.5,1.75,2.25,2.75,3,2.75,3.25,3.5,3.5,2.75,3,3,3.25,3.25,3,2.75,2.5,2,1.75,1.5,1.25,1.25,1.5,1.5,1.75,1]
    cy=[2.25,2.25,2.75,1.25,1,2,1,1.25,2.75,2.25,2.25,2.5,3.5,3.75,4.25,4.5,4.75,5,5,4.75,4.75,5,5,4.75,4.5,4.25,3.75,3.5,2.5]
         
    createpolygon(cx,cy,win,'brown')

#membuat menu program
    m = 0
    while m<6:
        print('1. rotasi\n2. scale\n3. shear x\n4. shear y\n5. Reset window\n6. Exit\nPilih menu :')
        m = int(input())
        if(m==1):
            print('Masukkan sudut rotasi:')
            t = int(input())
            pt = rotate(cx,cy,win,t)
            cx = pt[0]
            cy = pt[1]

        if(m==2):
            print('Masukkan skala x:')
            sx = float(input())
            print('Masukkan skala y:')
            sy = float(input())
            ps = scale(cx,cy,win,sx,sy)
            cx = ps[0]
            cy = ps[1]

        if(m==3):
            print('Masukkan sh x:')
            shx = float(input())
            psh = shearx(cx,cy,win,shx)
            cx = psh[0]
            cy = psh[1]

        if(m==4):
            print('Masukkan sh y:')
            shy = float(input())
            psh = sheary(cx,cy,win,shy)
            cx = psh[0]
            cy = psh[1]

        if(m==5):
            win.close()
            main()

        if(m==6):
            win.close()
            break
main()
