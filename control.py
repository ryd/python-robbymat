
import serial, string
import pygame
from pygame.locals import *

class Robbymat:
    def __init__(self, serial_instance):
        self.serial = serial_instance

    def move_up(self):
        ser.write("Z MOVE -10\n")
        print ser.readline()[:-1]


    def move_down(self):
        ser.write("Z MOVE 10\n")
        print ser.readline()[:-1]

    def move_left(self):
        ser.write("X MOVE -200\n")
        print ser.readline()[:-1]


    def move_right(self):
        ser.write("X MOVE 200\n")
        print ser.readline()[:-1]

    def move_forward(self):
        ser.write("Y MOVE 200\n")
        print ser.readline()[:-1]

    def move_backward(self):
        ser.write("Y MOVE -200\n")
        print ser.readline()[:-1]


if __name__ == '__main__':
    print "Let's go"
    ser = serial.Serial('/dev/ttyUSB0', 19200, 8, 'N', 1, timeout=1)

    robby = Robbymat(ser)

    pygame.init()
    screen = pygame.display.set_mode((120, 120))
    pygame.display.set_caption('Robymat')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    action = None

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    action = robby.move_backward
                if event.key == K_DOWN:
                    action = robby.move_forward
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



