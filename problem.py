#Digital Robotic Simulation Gym Space
#Authors: Jacob Lagares and Sergi Valverde
#Started date: Some day in April of 2018
#Last Release date:??/??/??

import random
import os.path

import pygame
from agent import Agent
from pygame.locals import *

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#Get he rect of the screen
SCREENRECT = Rect(0, 0, 1000, 500)
print(SCREENRECT.midbottom)

main_dir = os.path.split(os.path.abspath(__file__))[0]

version = "0.14"

agent = Agent()

#Load image
def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

#Load image"s"
def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

#Irrelevent stuff
class dummysound:
    def play(self): pass

#♪♫ Load sounds like music ♪♫
def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()

#Main stuff
def main(winstyle = 0):
    # Initialize pygame
    pygame.init()

    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    #Set the display mode
    winstyle = 0  #FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    #decorate the game window
    pygame.display.set_caption('Digital Robotic Simulation Gym Space', version)
    print("Caption set to:", 'Digital Robotic Simulation Gym Space', version)
    pygame.display.set_icon(load_image('chimp.bmp'))
    pygame.mouse.set_visible(0)

    #create the background, tile the bgd image
    bgdtile = load_image('background.gif')
    background = pygame.Surface(SCREENRECT.size)

    agent.__init__()
    player.__init__()

    #Render the background
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        for y in range(0, SCREENRECT.height, bgdtile.get_height()):
            background.blit(bgdtile, (x, y))
    
    #Blit the background
    screen.blit(background, (0,0))
    pygame.display.flip()

    #assign default groups to each sprite class
    all = pygame.sprite.RenderUpdates()
    player.setPos(SCREENRECT.width / 2, SCREENRECT.height / 2, 10, 10)

    #Setup the mixer
    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()

    while True:
        agent.action()

    all.clear(screen, background)

    #update all the sprites
    all.update()

#Call the "main" function if running this script
main(0)
