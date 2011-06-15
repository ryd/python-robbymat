
import string, re
import pygame
from pygame.locals import *

class Display:
    def __init__(self, surface):
        self.x = 0
        self.y = 0
        self.goto_x = 0
        self.goto_y = 0
        self.factor_x = 10
        self.factor_y = 10
        self.color = (200, 200, 200)
        self.surface = surface

    def parse(self, token):
        cmd = token[0:2]
        pos = re.split(",", token[2:])
        if len(pos) == 2 and pos[0].isdigit() and pos[1].isdigit() :
            self.goto_x = int(float(pos[0]) / self.factor_x)
            self.goto_y = int(float(pos[1]) / self.factor_y)
        if cmd == "PD":
            self.draw()
        elif cmd == "PU":
            self.move()

    def draw(self):
        if self.goto_x < 1200 and self.x < 1200 and self.goto_y < 700 and self.y < 700:
            self.distance_x = self.distance(self.goto_x, self.x)
            self.distance_y = self.distance(self.goto_y, self.y)
            pygame.draw.line(self.surface, self.color, (self.x, self.y), (self.goto_x, self.goto_y), 1)
            #pygame.display.flip()
        else:
            print "ignore {0},{1} - {2},{3}".format(self.x, self.y, self.goto_x, self.goto_y)
        self.move()

    def move(self):
        if self.goto_x > 1:
            self.x = self.goto_x
        if self.goto_y > 1:
            self.y = self.goto_y

    def distance(self, point1, point2):
        if (point1 < point2):
            distance = point2 - point1
        else:
            distance = point1 - point2

        return distance

if __name__ == '__main__':
    print "Let's go"
    
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption('Robymat')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    f = open('hpgl/mauer.prn', 'r')
    hpgl = Display(pygame.display.get_surface())
    for line in f:
        token = re.split("\;", line)
        print "len", len(line), " items", len(token)
        for t in token:
            hpgl.parse(t)
    f.close()

    while 1:
        pygame.display.flip()

