import pygame
import random
import time

from pygame.locals import *

#THE PLAYER
class Player():
    #Init pygame
    pygame.init()

    #Main game constants
    images = []
    speed = 20
    bounce = 24
    gun_offset = -11

    #Screen objects
    size = [1000, 500]
    screen = pygame.display.set_mode(size)

    #Colors
    orange = (255, 128, 0)

    #Text constants
    font1 = pygame.font.SysFont("calibri",40)

    #Main clock object
    clock = pygame.time.Clock()

    #Player constants
    playerW = 50
    playerH = 50

    #Init player
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 50
        self.h = 50
        self.clock.tick(60)
        self.drawSensor()

    #Draw the player
    def drawPlayer(self, px, py, pw, ph, pcolor, pwidth):
        pygame.draw.rect(self.screen, pcolor, [px, py, pw, ph], pwidth)
        pygame.display.update()

    #Draw the sensor
    def drawSensor(self):
        pygame.draw.line(self.screen, self.orange, [self.x + self.playerW / 2, self.y], [self.x + self.playerW / 2, self.y - 100], 5)
        pygame.display.update()

    #Repaint on movement
    def move(self, direction):
        self.drawPlayer(self.x, self.y, self.playerW, self.playerH, self.orange, 5)
        pygame.display.update()
        self.drawSensor()
        pygame.display.update()

        t = str(self.x) + ", " + str(self.y)

        text = self.font1.render(t, True, (255, 255, 255))
        self.screen.blit(text, [0, 0])
        pygame.display.update()

        print(self.x, self.y, self.w, self.h)

    #Set pos of the player
    def setPos(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        pygame.display.update()
    
    #Move stuff
    def moveUp(self, increment):
        if self.y > 0:
            self.setPos(self.x, self.y - increment, self.w, self.h)

    def moveDown(self, increment):
        if self.y < 500:
            self.setPos(self.x, self.y + increment, self.w, self.h)

    def moveLeft(self, increment):
        if self.x > 0:
            self.setPos(self.x - increment, self.y, self.w, self.h)

    def moveRight(self, increment):
        if self.x < 1000:
            self.setPos(self.x + increment, self.y, self.w, self.h)
