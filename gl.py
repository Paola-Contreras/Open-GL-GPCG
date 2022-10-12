import glm #math library 
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Renderer(object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()

        glEnable(GL_DEPTH_TEST)
        glViewport(0,0, self.width, self.height)

    #Function that draw the frameBuffer, so I have to call it in a loop 
    def render(self):
        #Set a background color as init, alpha means transparency 
        glClearColor(0.2,0.2,0.2,1)
        #Clear color and depth buffer 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

