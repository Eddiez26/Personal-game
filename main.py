import pygame
import random
from background import Background
from snake import Snake
from fruit import Fruit

# Initialize pygame
pygame.init()

# Window size
window_x = 720
window_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')

# Game settings
fps = pygame.time.Clock()
snake_speed = 15
score = 0

# Fonts
font = pygame.font.SysFont('arial', 36)

# Background setup
background = Background(window_x, window_y, 'tile_image.png')

# Title Screen
# Title Screen
def title_screen():
    while True:
        game_window.fill(black)
        title_text = font.render('Snake Game', True, white)
        game_window.blit(title_text, (window_x // 2 - title_text.get_width() // 2, window_y // 4))

        play_button = pygame.Rect(window_x // 2 - 50, window_y // 2, 100, 50)
        pygame.draw.rect(game_window, green, play_button)
        play_text = font.render('Play', True, black)
        game_window.blit(play_text, (play_button.x + (play_button.width - play_text.get_width()) // 2,
                                     play_button.y + (play_button.height - play_text.get_height()) // 2))

        # Load snakey image
        snakey_image = pygame.image.load('snakey.png').convert_alpha()
        snakey_image = pygame.transform.scale(snakey_image, (60, 60))
        game_window.blit(snakey_image, (play_button.x - 70, play_button.y))

        # Load apple image
        apple_image = pygame.image.load('apple.png').convert_alpha()
        apple_image = pygame.transform.scale(apple_image, (60, 60))
        game_window.blit(apple_image, (play_button.x + play_button.width + 10, play_button.y))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return True

# End Screen
def end_screen():
    global score
    while True:
        game_window.fill(black)
        game_over_text = font.render('Game Over', True, red)
        score_text = font.render('Your Score is: ' + str(score), True, white)
        game_window.blit(game_over_text, (window_x // 2 - game_over_text.get_width() // 2, window_y // 4))
        game_window.blit(score_text, (window_x // 2 - score_text.get_width() // 2, window_y // 2 - 50))

        play_again_button = pygame.Rect(window_x // 2 - 100, window_y // 2, 200, 50)
        pygame.draw.rect(game_window, green, play_again_button)
        play_again_text = font.render('Play Again', True, black)
        game_window.blit(play_again_text, (play_again_button.x + (play_again_button.width - play_again_text.get_width()) // 2,
                                           play_again_button.y + (play_again_button.height - play_again_text.get_height()) // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    score = 0
                    return True

# Show score
def show_score(surface):
    score_text = font.render('Score: ' + str(score), True, black)
    surface.blit(score_text, (10, 10))

# Main game loop
def run_game():
    global score

    while True:
        if title_screen():
            score = 0
            snake = Snake(window_x, window_y)
            fruit = Fruit(window_x, window_y, 'apple.png')
            fruit.spawn()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            snake.change_direction('UP')
                        if event.key == pygame.K_DOWN:
                            snake.change_direction('DOWN')
                        if event.key == pygame.K_LEFT:
                            snake.change_direction('LEFT')
                        if event.key == pygame.K_RIGHT:
                            snake.change_direction('RIGHT')

                snake.move()
                if snake.snake_position[0] == fruit.apple_position[0] and snake.snake_position[1] == fruit.apple_position[1]:
                    score += 10
                    fruit.spawn()
                else:
                    snake.snake_body.pop()

                background.draw(game_window)
                snake.draw(game_window)
                fruit.draw(game_window)

                # Game over conditions
                if snake.snake_position[0] < 0 or snake.snake_position[0] > window_x - 30:
                    if end_screen():
                        break
                if snake.snake_position[1] < 0 or snake.snake_position[1] > window_y - 30:
                    if end_screen():
                        break

                for block in snake.snake_body[1:]:
                    if snake.snake_position[0] == block[0] and snake.snake_position[1] == block[1]:
                        if end_screen():
                            break

                # Display score
                show_score(game_window)

                # Refresh game screen
                pygame.display.update()

                # Frame Per Second / Refresh Rate
                fps.tick(snake_speed)

# Run the game
run_game()
