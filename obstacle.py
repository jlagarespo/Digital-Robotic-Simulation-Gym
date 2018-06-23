import pygame
import random

from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):
    """
    Class Obstacle

    Obstacle. Needed to be avoided by the agent.
    Don't change it unless you want to change the problem to solve.
    """
    
    images = []
    speed = 20
    bounce = 24
    gun_offset = -11

    def __init__(self):
        #Init stuff
        pygame.sprite.Sprite.__init__(self, self.containers)
        #Set basic constants
        self.image = self.images[0]
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.screenrect = Rect(self.x, self.y, self.w, self.h)
        self.rect = self.image.get_rect(midbottom=self.screenrect.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def draw(self, direction):
        """
        Draw the obstacle
        """
        self.rect = self.rect.clamp(self.screenrect)
        self.image = self.images[0]
        if direction: self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screenrect)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)

    def setPos(self, x, y, w, h):
        """
        Set a new location for the obstacle
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
    
    def moveUp(self, increment):
        """
        Displace obstacle up
        """
        self.setPos(self.x, self.y - increment, self.w, self.h)

    def moveDown(self, increment):
        """
        Displace obstacle down
        """
        self.setPos(self.x, self.y + increment, self.w, self.h)

    def moveLeft(self, increment):
        """
        Displace obstacle left
        """
        self.setPos(self.x - increment, self.y, self.w, self.h)

    def moveRight(self, increment):
        """
        Displace obstacle right
        """
        self.setPos(self.x + increment, self.y, self.w, self.h)

    def getX(self):
        """
        Get obstacle X location
        """
        return self.x

    def getY(self):
        """
        Get obstacle Y location
        """
        return self.y
    
    def getW(self):
        """
        Get obstacle width
        """
        return self.w
    
    def getH(self):
        """
        Get obstacle height
        """
        return self.h

# END