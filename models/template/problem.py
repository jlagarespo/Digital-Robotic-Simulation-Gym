# *********************************************************

# Digital Robotic Simulation Gym Space
# Welcome to the code
# Hope you enjoy! :D

# *********************************************************

"""
Digital Robotic Simulation Gym Space
Authors: Jacob Lagares and Sergi Valverde
Contact at jlagarespo@iebesalu.cat or sergivalv@gmail.com
Started date: Some day in April of 2018
Last Release date:??/??/??

Digital Robotic Simulation Gym is a tool for simulating robotic behaviours, such as an
automated controller what needs to avoid a set of obstacles, an agent what wants to get
out of a maze, or similar.

For doing this, we program the brain.py class in what you change the behaviour of everything
and we can test a lot of algorythms, from the most simplistic ones, like random direction
choosing, to more advanced things, like Machine Learning or this kind of things(what we
going to start working in it in the future!). Perfect place to test cool stuff.

Controls:
ESC    - exit
R      - reset everything
"""

# start

import sys
sys.path.insert(0, "../../")

import os.path
import pygame
import numpy as np
from pygame.locals import *
from brain import Brain as Agent
from obstacle import Obstacle as Obstacle
from problemMap import ProblemMap as ProblemMap
from goal import Goal as Goal
from PIL import Image

# *********************************************************
# IMPLEMENTATION
# *********************************************************

# Main simulator constants

# problem variables
problemW = 400
problemH = 400
framerate = 10

# the number of obstacles can be set
NUM_OBSTACLES = 5

# agent
agentPosX = np.random.randint(0, problemW)
agentPosY = np.random.randint(0, problemH)

sensorW = 50
sensorH = 50
speed = 5

#goal
goalX = problemW / 2
goalY = problemH / 2

# *********************************************************

# Get the rect of the screen
SCREENRECT = Rect(0, 0, problemW, problemH)

# main dir has to be re-defined if new exercises are called from the
# examples/name/ folder
main_dir = os.path.split(os.path.abspath('../'))[0]
print(main_dir)
clock = pygame.time.Clock()

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


def load_image(file):
    """
    This would load an image from files
    (PNG, JPEG or BITMAP)
    Used as sprites base
    """
    print("Loading: " + file + " images")
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' %(file, pygame.get_error()))
    return surface.convert()


# Load image"s"
def load_images(*files):
    """
    Uses load_image(file) to load multiple images
    """

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
imgObstacle = load_image('obstacle.png')
imgGoal = load_image("goal.png")
# imgGoal = load_image('obstacle.png')
Agent.images = [img, pygame.transform.flip(img, 1, 0)]
Obstacle.images = [imgObstacle, pygame.transform.flip(img, 1, 0)]
Goal.images = [imgGoal, pygame.transform.flip(img, 1, 0)]

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
Goal.containers = all

agent = Agent(sensorW, sensorH, speed)

# generate the map
mp = ProblemMap()
mp.setMapSize(SCREENRECT.width, SCREENRECT.height)

# generate obstacles and assign them to random positions
obstacles = [Obstacle() for obs in range(NUM_OBSTACLES)]

# set goal
goal = Goal()
goal.setPos(goalX, goalY, 50, 50)
mp.setGoal(goalX, goalY, 50, 50)

# assign positions to obstacles and add them to the map
for obs in obstacles:
    x_pos = np.random.randint(0, problemW)
    y_pos = np.random.randint(0, problemH)
    obs.setPos(x_pos, y_pos, 10, 10)
    mp.setObstacle(obs.getX(),
                   obs.getY(),
                   obs.getW(),
                   obs.getH())

agent.setPos(agentPosX, agentPosY, 10, 10)

# the agent is iteratively asking for a new position
# while it's finding the goal. If it touches an obstacle
# the game is finished

agent_w, agent_h = agent.getSize()

print("--------------------------------------------------")
print("AGENT POS:", agent.getPos())
print("SENSOR POS:", sensorW, sensorH)
print("--------------------------------------------------")
print(agent_w, agent_h)

if agent_w > sensorW:
    print("Agent too big!")
    exit()

if agent_h > sensorH:
    print("Agent too big!")
    exit()

# save map as bitmap
data = mp.getMap(0, 0, problemW, problemH)

dataRGB = np.stack([data, np.zeros_like(data), data], axis=2)

img = Image.fromarray(dataRGB.astype("uint8") * 255, "RGB")
img.save("map.png")
img.show()

while agent.alive():
    # get current state
    agentPosX, agentPosY = agent.getPos()
    sensor_info = mp.getMap(agentPosX - sensorW / 2,
                            agentPosY - sensorH / 2,
                            sensorW,
                            sensorH)

    if mp.evaluate_goal(agentPosX, agentPosY, agent_w, agent_h):
        print("PARTYYYY :D")
        pygame.time.wait(2000)
        pygame.quit()

    # evaluate the agent position
    # if the agent is touching one of the obstacles, stop
    # the problem. If still alive, get sensory information and move
    if mp.evaluate_map(agentPosX, agentPosY, agent_w, agent_h, 5):
        print("Agent messed up :(")
        pygame.time.wait(2000)
        pygame.quit()
    else:
        agent.getSensor(sensor_info)
        agent.nextState(speed)

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
            if event.key == K_r:
                # Reset game
                print("reset")

# END