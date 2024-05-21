import pygame
import random
import time
from fruit import Pineapple


# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 450
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
snake=0

snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50] ]


direction="right"
change_to=direction

r = 50
g = 0
b = 100



P=Pineapple(20,30)



clock=pygame.time.clock()

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
for event in pygame.event.get():
    pygame.display.flip()

# -------- Main Program Loop -----------
while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'

            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

if snake_body==Pineapple:
    snake_body+=1



    ## FILL SCREEN, and BLIT here ##
    screen.fill((r, g, b))
    screen.blit(B.image, B.rect)
    screen.blit(A.image, A.rect)
    screen.blit(P.image, P.rect)
    pygame.display.update()
    ## END OF WHILE LOOP



# Once we have exited the main program loop we can stop the game engine:
pygame.quit()