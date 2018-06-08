import pygame
from pygame.locals import *


class Agent(pygame.sprite.Sprite):
    """
    Class Agent

    This is the simulation controller. Like a robot.
    Its controlled from the brain.py class what inherits this.
    Don't recommended to touch!

    """
    images = []
    speed = 20
    bounce = 24
    gun_offset = -11

# *********************************************************

    def __init__(self, sensorW, sensorH, step):
        # Init stuff
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Set basic constants
        self.image = self.images[0]
        self.x = 0
        self.y = 0
        self.w = self.images[0].get_rect().w
        self.h = self.images[0].get_rect().h
        self.screenrect = Rect(self.x, self.y, self.w, self.h)
        self.rect = self.image.get_rect(midbottom=self.screenrect.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
        self.sensorMap = None
        self.sensorW = sensorW
        self.sensorH = sensorH
        self.step = step
        print(self.w, self.h)

# *********************************************************

    def move(self, direction):
        """
        Update the player location and iterate properties
        """
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screenrect)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce % 2)

# *********************************************************

    def setPos(self, x, y, w, h):
        """
        Sets player position
        """
        self.screenrect = Rect(x, y, w, h)
        self.rect = self.image.get_rect(midbottom=self.screenrect.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
        self.x = x
        self.y = y
        self.w = w
        self.h = h

# *********************************************************

    def moveUp(self, increment):
        """
        Displace the player up
        """
        self.setPos(self.x, self.y - increment, self.w, self.h)

    def moveDown(self, increment):
        """
        Displace the player down
        """
        self.setPos(self.x, self.y + increment, self.w, self.h)

    def moveLeft(self, increment):
        """
        Displace the player left
        """
        self.setPos(self.x - increment, self.y, self.w, self.h)

    def moveRight(self, increment):
        """
        Displace the player right
        """
        self.setPos(self.x + increment, self.y, self.w, self.h)

# *********************************************************

    def getSensor(self, data):
        """
        Loads the sensor data into the agent class
        """
        self.sensorMap = data
        # print(data)

    def getSensorSize(self):
        """
        Gets the size of the sensor
        """
        return self.sensorW, self.sensorH

# *********************************************************

    def getPos(self):
        """
        Gets the agent location
        """
        return self.x, self.y

    def getSize(self):
        """
        Gets the agent size
        """
        return self.w, self.h

# *********************************************************
#END#