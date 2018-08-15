import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.path = path
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
