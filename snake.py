import pygame

class Snake:
    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move(self):
        if self.direction == 'UP':
            self.snake_position[1] -= 30
        if self.direction == 'DOWN':
            self.snake_position[1] += 30
        if self.direction == 'LEFT':
            self.snake_position[0] -= 30
        if self.direction == 'RIGHT':
            self.snake_position[0] += 30

        self.snake_body.insert(0, list(self.snake_position))

    def draw(self, surface):
        for pos in self.snake_body:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(pos[0], pos[1], 30, 30))
