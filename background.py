import pygame

class Background:
    def __init__(self, window_width, window_height, tile_image_path):
        self.window_width = window_width
        self.window_height = window_height
        self.tile_image = pygame.image.load(tile_image_path)
        self.tile_width, self.tile_height = self.tile_image.get_size()

    def draw(self, surface):
        for x in range(0, self.window_width, self.tile_width):
            for y in range(0, self.window_height, self.tile_height):
                surface.blit(self.tile_image, (x, y))