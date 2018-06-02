# Digital Robotic Simulation Gym Space
# Authors: Jacob Lagares and Sergi Valverde
# Contact at jlagarespo@iebesalu.cat or sergivalv@gmail.com
# Started date: Some day in April of 2018
# Last Release date:??/??/??

import os.path
import pygame
from pygame.locals import *

from brain import Brain as Agent
from obstacle import Obstacle
from problemMap import ProblemMap

# *********************************************************
# problem variables
problemW = 1000
problemH = 500
framerate = 10

# obstacle
obsPosX = problemW / 2
obsPosY = problemH / 2

# agent
agentPosX = 50
agentPosY = 50

sensorW = 12
sensorH = 12
step = 20

# *********************************************************

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

# Get he rect of the screen
SCREENRECT = Rect(0, 0, problemW, problemH)
main_dir = os.path.split(os.path.abspath(__file__))[0]
clock = pygame.time.Clock()


# Load image
def load_image(file):
    print("Loading: " + file + " images")
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()


# Load image"s"
def load_images(*files):
    print("Loading every: " + files + " images")
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


# Initialize pygame
pygame.init()

# Set the display mode
winstyle = 0  # FULLSCREEN
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

# Load images, assign to sprite classes
# (do this before the classes are used, after screen setup)
img = load_image('player1.gif')
imgObstacle = load_image('chimp.bmp')
Agent.images = [img, pygame.transform.flip(img, 1, 0)]
Obstacle.images = [imgObstacle, pygame.transform.flip(img, 1, 0)]

# decorate the game window
icon = pygame.transform.scale(Agent.images[0], (32, 32))
pygame.display.set_icon(icon)
pygame.display.set_caption('Gym 10.0')
pygame.mouse.set_visible(0)

# create the background, tile the bgd image
bgdtile = load_image('background.gif')
background = pygame.Surface(SCREENRECT.size)

# Render the background
for x in range(0, SCREENRECT.width, bgdtile.get_width()):
    for y in range(0, SCREENRECT.height, bgdtile.get_height()):
        background.blit(bgdtile, (x, y))

# Blit the background
screen.blit(background, (0, 0))
pygame.display.flip()

# assign default groups to each sprite class
all = pygame.sprite.RenderUpdates()
Agent.containers = all
Obstacle.containers = all

agent = Agent(sensorW, sensorH, step)
obstacle = Obstacle()
mp = ProblemMap()
agent.setPos(agentPosX, agentPosY, 10, 10)
obstacle.setPos(obsPosX, obsPosY, 10, 10)

x, y = obstacle.getX(), obstacle.getY()
mp.setMapSize(SCREENRECT.width, SCREENRECT.height)
mp.setObstacle(obstacle.getX(),
               obstacle.getY(),
               obstacle.getW(),
               obstacle.getH())
print(mp.getSize())

# the agent is iteratively asking for a new position
# while it's finding the goal. If it touches an obstacle
# the game is finished

sensor_w, sensor_h = agent.getSensorSize()
agent_w, agent_h = agent.getSize()

while agent.alive():

    # get current state
    agentPosX, agentPosY = agent.getPos()
    sensor_info = mp.getMap(agentPosX, agentPosY, sensor_w, sensor_h)

    # evaluate the agent position
    # if the agent is touching one of the obstacles, stop
    # the problem. If still alive, get sensory information and move
    if mp.evaluate_map(agentPosX, agentPosY, agent_w, agent_h):
        print("Agent messed up :(")
        pygame.time.wait(2000)
        pygame.quit()
    else:
        agent.getSensor(sensor_info)
        agent.nextState()

    # update all the sprites and draw the scene
    all.clear(screen, background)
    all.update()
    dirty = all.draw(screen)
    pygame.display.update(dirty)

    # cap the framerate
    clock.tick(framerate)

    # finish the game if ESC is pressed
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                exit()

<<<<<<< HEAD
# call the "main" function if running this script
if __name__ == '__main__': main(0)

=======
pygame.time.wait(1000)
pygame.quit()
>>>>>>> f84ea20ddd35db40b859b99c3b20e65b6d2787af
