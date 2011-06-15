import pygame
from pygame.locals import *

import hpgl, display, re

print "Let's go"

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Robymat')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
screen.blit(background, (0, 0))

hpgl = hpgl.HPGL()
display = display.Display(pygame.display.get_surface())

#f = open('hpgl/duke_Nukem__by_DeadCamper.prn', 'r')
f = open('hpgl/mauer.prn', 'r')

for line in f:
    token = re.split("\;", line)
    print "len", len(line), " items", len(token)
    for t in token:
        display.parse(t)
        hpgl.parse(t)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_PAGEUP:
                    hpgl.robby.move_z(-1)
                if event.key == K_PAGEDOWN:
                    hpgl.robby.move_z(1)

f.close()

print "printing done"

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                action = robby.move_forward
            if event.key == K_DOWN:
                action = robby.move_backward
            if event.key == K_LEFT:
                action = robby.move_left
            if event.key == K_RIGHT:
                action = robby.move_right
            if event.key == K_PAGEUP:
                action = robby.move_up
            if event.key == K_PAGEDOWN:
                action = robby.move_down
        if event.type == KEYUP:
            action = None

        if action:
            action()
    pygame.display.flip()

