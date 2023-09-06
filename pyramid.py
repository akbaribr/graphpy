import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = ((0,5,0),(5,0,5),(-5,0,5),(-5,0,-5),(5,0,-5))
edges = ((0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4),(1,4))
fields = ((0,1,2),(0,2,3),(0,3,4),(0,4,1),(1,2,3,4))

def wire_obj():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def solid_obj():
    glBegin(GL_POLYGON)
    for field in fields:
        for vertex in field:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(90, (display[0]/display[1]), 0.5, 50)
    glTranslatef(0,0,-10)
    glRotatef(25, 2, 1, 0)

    wire_obj()
    solid_obj()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

if __name__ == '__main__':
    main()
