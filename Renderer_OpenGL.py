import pygame
from pygame.locals import *
from shaders import *

from gl import Renderer, Model

width = 960
height = 540

deltaTime = 0.0

zoomIn = 70
zoomOut = 90
moveUp = 230
moveDown = 200

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)


face = Model("models\plant.obj", "models\plant_COL.bmp")

face.position.z -= 13

face.scale.x = 1
face.scale.y = 1
face.scale.z = 1


rend.scene.append( face )


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_1:
                rend.filledMode()

            elif event.key == pygame.K_2:
                rend.wireframeMode()

                    #MOVEMENTS 
    #Left
    if keys[K_a]:
        rend.camPosition.x -= 10 * deltaTime
    #Right
    elif keys[K_d]:
        rend.camPosition.x += 10 * deltaTime
    #Up
    elif keys[K_w]:
        if moveUp <= 350:
            rend.camPosition.y += 10 * deltaTime
            moveUp += 3
        else:
            print("limit reached")
    #DownZ
    elif keys[K_s]:
        if moveDown > 0:
            rend.camPosition.y -= 10 * deltaTime
            moveDown -= 3
        else:
            print("limit reached")
    #Out
    elif keys[K_z]:
        if zoomOut >= 0:
            rend.camPosition.z += 10 * deltaTime
            zoomOut -=1
        else:
            print("limit reached")
            zoomOut = 90
    #In
    elif keys[K_x]:
        if zoomIn >= 0:
            rend.camPosition.z -= 10 * deltaTime
            zoomIn -= 1
        else:
            print("limit reached")
            


                    #LIGHT
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime

    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime

    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()


pygame.quit()