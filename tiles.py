import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.path = path
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def save(self):
        self.image = None

    def load(self):
        self.image = pygame.image.load(self.path)


class Door(Tile):
    def __init__(self, images, pos, unlocked):
        super().__init__(images[unlocked], pos)
        self.images = images
        self.unlocked = unlocked

    def unlock(self):
        self.unlocked = True
        self.image = pygame.image.load(self.images[self.unlocked])

    def load(self):
        self.image = pygame.image.load(self.images[self.unlocked])
