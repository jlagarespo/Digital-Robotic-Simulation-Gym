import pygame
import random, os.path

from player import Player
from obstacle import *
from pygame.locals import *

#Here is the behaviour of the controller
class Agent():
    #Main agent constants
    #If you need to create a variable or a data structure, do it here
    speed = 2

    player = Player()
    clock = pygame.time.Clock()
    
    #Init agent
    def __init__(self):
        self.clock.tick(60)
        self.action()

    #The main agent code
    #Here is the behaviour
    #For example, here is a basic key controlling algorythm.
    #You can find examples of pre-made codes in the "examples folder"
    def action(self):
        pygame.init()

        pressed = pygame.key.get_pressed()
        keystate = pygame.key.get_pressed()

        #Set the direction
        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        
        #Take player input
        pygame.display.update()
        if(pressed[pygame.K_UP]):
            self.player.moveUp(self.speed)
        if(pressed[pygame.K_DOWN]):
            self.player.moveDown(self.speed)
        if(pressed[pygame.K_LEFT]):
            self.player.moveLeft(self.speed)
        if(pressed[pygame.K_RIGHT]):
            self.player.moveRight(self.speed)
        self.player.move(direction)