import pygame
import random
import time
from background import Background
from apple import Apple


# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 450
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


r = 50
g = 0
b = 100




B = Background(40, 40)


A=Apple(20,20)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:



    ## FILL SCREEN, and BLIT here ##
    screen.fill((r, g, b))
    screen.blit(B.image, B.rect)
    screen.blit(A.image, A.rect)
    pygame.display.update()
    ## END OF WHILE LOOP



# Once we have exited the main program loop we can stop the game engine:
pygame.quit()



