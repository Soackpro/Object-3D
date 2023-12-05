import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

angle = -50.0
rotation_speed = 0.5

def draw_rocket():
    # Rocket body
    glPushMatrix()
    glTranslatef(-2.0, -1.0, -2.0)
    glRotatef(90.0, 1.0, 0.0, 0.0)  
    glColor3f(0.1, 0.1, 0.1)
    glutSolidCylinder(0.4, 2.0, 15, 30)
    glPopMatrix()

    # Nose
    glPushMatrix()
    glTranslatef(-2.0, -1.0, -2.0)  
    glRotatef(270.0, 1.0, 0.0, 0.0)  
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCone(0.4, 0.6, 30, 30)
    
    #knalpot
    glPushMatrix()
    glTranslatef(0.0, 0.0, -2.0)  
    glRotatef(0, 1.0, 0.0, .0)  
    glColor3f(0.6, 0.2, 0.0)
    glutSolidCone(0.5, 1.0, 30, 30)
    glPopMatrix()
    
    #nos red
    glPushMatrix()
    glTranslatef(.0, .0, -2.0)  
    glRotatef(180, 1.0, 0.0, .0)  
    glColor3f(0.7, 0.3, 0.0)
    glutSolidCone(0.5, 0.5, 20, 30)
    glPopMatrix()
    
    glBegin(GL_QUADS)
    
    glEnd()
    glPopMatrix()
   


def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 2.0, -8.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    draw_rocket()
    glutSwapBuffers()
    angle += rotation_speed

def init():
    glClearColor(0.3, 0.3, 0.3, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

def reshape(width, height):
    if height == 0:
        height = 1
    aspect = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, aspect, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Rocket - Filach Akbar Arafat - 2113020069")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init()
    glutTimerFunc(10, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
