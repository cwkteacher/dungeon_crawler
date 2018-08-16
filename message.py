import pygame


class Message(pygame.sprite.Sprite):
    def __init__(self, text, pos, color=(230, 230, 230)):
        super().__init__()
        font = pygame.font.SysFont('oldenglishtext', 25)
        self.text = text
        self.color = color
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.time = 0

    def update(self):
        self.time += 1
        if self.time > 120:
            self.kill()

    def save(self):
        self.image = None

    def load(self):
        font = pygame.font.SysFont('oldenglishtext', 25)
        self.image = font.render(self.text, True, self.color)


class MovingMessage(Message):
    def __init__(self, text, pos, color=(230, 230, 230)):
        super().__init__(text, pos, color)

    def update(self):
        super().update()
        self.rect.move_ip((0, -1))
