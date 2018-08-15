import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.path = path
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = [0, 0]
        self.level = None

    def update(self):
        self.rect.move_ip(self.movement)
        if len(pygame.sprite.spritecollide(self, self.level.walls, False)) >= 1:
            if pygame.sprite.collide_rect(self, self.level.exit)and self.level.exit.unlocked:
                return 1
            if pygame.sprite.collide_rect(self, self.level.start):
                return -1
            self.movement[0] *= -1
            self.movement[1] *= -1
            self.rect.move_ip(self.movement)
        self.movement[0] = 0
        self.movement[1] = 0

    def up_level(self, level):
        self.movement = [0, 0]
        self.level = level
        self.rect.topleft = level.start_pos

    def back_level(self, level):
        self.movement = [0, 0]
        self.level = level
        self.rect.topleft = level.end_pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def change_x(self, change):
        self.movement[0] = change

    def change_y(self, change):
        self.movement[1] = change

    def save(self):
        self.image = None
        self.level = None

    def load(self):
        self.image = pygame.image.load(self.path)
