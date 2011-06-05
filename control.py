
import serial, string, pygame, Robbymat
from pygame.locals import *

if __name__ == '__main__':
    print "Let's go"
    robby = Robbymat.Robbymat()

    pygame.init()
    screen = pygame.display.set_mode((120, 120))
    pygame.display.set_caption('Robymat')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    action = None

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

