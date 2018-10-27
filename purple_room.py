import pygame
import pygame.display
import os
import sys
from random import randint

pygame.init()
pygame.display.init()
# -----------------------------------------
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music House - Purple room")
done = False
# -----------------------------------------BACKGROUND
# background = pygame.image.load("img/purple_cosmos.jpg")
# screen.blit(background, (0, 0))
# bottom_dash = pygame.draw.rect(screen, (212, 212, 212), (0, 350, 640, 440), 0)
# pygame.display.update()
# -----------------------------------------VARIABLES
square = pygame.draw.rect(screen, (212, 212, 212), (0, 350, 640, 440), 0)
circle = pygame.draw.circle(screen, (212, 212, 212), (240, 400), 50, 0)
pygame.display.update()

# -----------------------------------------


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.display.flip()

# Finish Pygame.
pygame.quit()
