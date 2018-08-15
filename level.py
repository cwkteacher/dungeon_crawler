import pygame, random
from tiles import *


class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # groups
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()

    def draw(self, screen):
        self.floor.draw(screen)
        self.walls.draw(screen)


class RandomLevel(Level):
    def __init__(self, images):
        super().__init__()
        self.generate_level(images)

    def generate_level(self, images):
        screen_info = pygame.display.Info()
        game_map = []
        # initialize entire map to walls
        for i in range((screen_info.current_w // 32) + 1):
            game_map.append(["w"] * ((screen_info.current_h // 32) + 1))
        # calculate amount of tiles to convert into floor tiles
        fnum = int((len(game_map) * len(game_map[0])) * .5)
        # current number of floor tiles
        count = 0
        # starting tile for dungeon generation
        tile = [len(game_map) // 2, len(game_map[0]) // 2]
        while count < fnum:
            if game_map[tile[0]][tile[1]] != "f":
                game_map[tile[0]][tile[1]] = "f"
                count += 1
            move = random.randint(1, 4)
            if move == 1 and tile[0] > 1:  # move north
                tile[0] -= 1
            elif move == 2 and tile[0] < (len(game_map) - 3):  # move south
                tile[0] += 1
            elif move == 3 and tile[1] < (len(game_map[0]) - 3):  # move east
                tile[1] += 1
            elif move == 4 and tile[1] > 1:  # move west
                tile[1] -= 1
        # create tiles based on the contents of the map list
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == "w":
                    self.walls.add(Tile(images["w"], (i * 32, j * 32)))
                elif game_map[i][j] == "f":
                    self.floor.add(Tile(images["f"], (i * 32, j * 32)))
