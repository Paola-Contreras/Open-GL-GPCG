import pygame as pygame
from pygame.locals import *
from gl import Renderer

width = 960
height = 540 

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

isRuning = True
deltaTime = 0.0

while isRuning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRuning = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRuning = False
        
    #Clock uses 60 fps per second 
    deltaTime = clock.tick(60) / 1000
    print(deltaTime)

    rend.render()
    #flip changes screen a lot of times 
    pygame.display.flip()

pygame.quit()
