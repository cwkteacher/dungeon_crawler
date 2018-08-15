import pygame, sys
from pygame.locals import *
from level import *

pygame.init()

# sets width and height to the dimensions of any screen
size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
images = {"w": "images/tiles/wall12.gif", "f": "images/tiles/floor13.gif"}


def main():
    global screen
    level = RandomLevel(images)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                # screen controls
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
        level.update()
        screen.fill(color)
        level.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
