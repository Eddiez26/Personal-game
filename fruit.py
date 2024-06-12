import pygame
import random

class Fruit:
    def __init__(self, window_x, window_y, image_path):
        self.window_x = window_x
        self.window_y = window_y
        self.apple_image = pygame.image.load(image_path).convert_alpha()
        self.apple_image = pygame.transform.scale(self.apple_image, (30, 30))
        self.spawn()

    def spawn(self):
        self.apple_position = [random.randrange(1, (self.window_x // 30)) * 30,
                               random.randrange(1, (self.window_y // 30)) * 30]

    def draw(self, surface):
        surface.blit(self.apple_image, (self.apple_position[0], self.apple_position[1]))