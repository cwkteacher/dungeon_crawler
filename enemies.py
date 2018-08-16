import pygame
import random
from message import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, pos, level):
        super().__init__()
        self.path = path
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.heading = None
        self.movement = pygame.math.Vector2(0, 2)
        self.movement.rotate_ip(random.randint(0, 360))
        self.level = level
        self.health = 10
        self.attack_damage = 3
        self.defense = 1
        self.reload = 20
        self.target = None

    def update(self):
        if pygame.sprite.collide_rect(self, self.level.player) and self.level.player.alive:
            self.target = self.level.player
        else:
            self.target = None
        if self.target is not None:
            self.reload -= 1
            if self.reload == 0:
                self.reload = 60
                self.attack(self.target)
            return
        self.rect.move_ip(self.movement)
        if len(pygame.sprite.spritecollide(self, self.level.walls, False)) >= 1:
            self.movement.rotate_ip(180)
            self.rect.move_ip(self.movement)
            self.movement.rotate_ip(random.randint(0, 360))

    def attack(self, player):
        player.defend(self.attack_damage)

    def defend(self, damage):
        if random.randint(1, 20) > self.defense:
            self.health -= damage
            if self.health <= 0:
                self.kill()
                if len(self.level.enemies) == 0 and not self.level.exit.unlocked:
                    self.level.messages.add(Message("Level Cleared,", (self.rect.centerx, self.rect.centery-30)))
                    self.level.messages.add(Message("Exit Unlocked!", self.rect.center))
                    self.level.exit.unlock()
                return True

    def save(self):
        self.image = None
        self.level = None
        self.heading = [self.movement[0], self.movement[1]]
        self.movement = None

    def load(self, level):
        self.image = pygame.image.load(self.path)
        self.level = level
        self.movement = pygame.math.Vector2(self.heading[0], self.heading[1])
