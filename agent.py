import pygame

from pygame.locals import *

class Agent(pygame.sprite.Sprite):
    images = []
    speed = 20
    bounce = 24
    gun_offset = -11

    def __init__(self, sensorW, sensorH, step):
        #Init stuff
        pygame.sprite.Sprite.__init__(self, self.containers)
        #Set basic constants
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

    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screenrect)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2) 

    def setPos(self, x, y, w, h):
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
        self.setPos(self.x, self.y - increment, self.w, self.h)

    def moveDown(self, increment):
        self.setPos(self.x, self.y + increment, self.w, self.h)

    def moveLeft(self, increment):
        self.setPos(self.x - increment, self.y, self.w, self.h)

    def moveRight(self, increment):
        self.setPos(self.x + increment, self.y, self.w, self.h)

    def getSensor(self, data):
        self.sensorMap = data
        # print(data)

    def getSensorSize(self):
        return self.sensorW , self.sensorH

    def getPos(self):
        return self.x, self.y
    
    def getSize(self):
        return self.w, self.h

    def nextState(self):
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    self.moveUp(self.step)
            if event.type == pygame.KEYUP:
                if event.key == K_DOWN:
                    self.moveDown(self.step)
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    self.moveLeft(self.step)
            if event.type == pygame.KEYUP:
                if event.key == K_RIGHT:
                    self.moveRight(self.step)
