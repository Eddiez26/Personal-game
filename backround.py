import pygame

class background:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("42c2518e-997c-49ce-8c7d-4ef6c8eba1a6")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
