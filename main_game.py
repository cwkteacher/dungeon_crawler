import pygame, sys
from pygame.locals import *
from level import *
from player import *

pygame.init()

# sets width and height to the dimensions of any screen
size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
images = {"w": "images/tiles/wall12.gif", "f": "images/tiles/floor13.gif",
          "s": {True: "images/tiles/openDoor31.gif", False: "images/tiles/door31.gif"},
          "e": {True: "images/tiles/openDoor12.gif", False: "images/tiles/door12.gif"}}
player = Player("images/player/superhero.gif", (16, 16))
levels = []
level_num = 0
current_level = None


def change_level(change):
    global level_num, current_level
    if change == 1:
        if level_num == len(levels) - 1:
            levels.append(RandomLevel(player, images))
        level_num += 1
        current_level = levels[level_num]
        player.up_level(current_level)
    elif change == -1:
        if level_num > 0:
            level_num -= 1
            current_level = levels[level_num]
            player.back_level(current_level)


def main():
    global screen, level_num, current_level
    levels.append(RandomLevel(player, images))
    current_level = levels[level_num]
    player.up_level(current_level)
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
                # player movement controls
                elif event.key == K_UP:
                    player.change_y(-32)
                elif event.key == K_DOWN:
                    player.change_y(32)
                elif event.key == K_RIGHT:
                    player.change_x(32)
                elif event.key == K_LEFT:
                    player.change_x(-32)
        change_level(current_level.update())
        screen.fill(color)
        current_level.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
