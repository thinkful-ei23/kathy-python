import pygame
import pygame.display
import os
import sys
from random import randint

pygame.init()
pygame.display.init()
done = False
running = True
# -----------------------------------------WINDOW
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music House - XX door")

# -----------------------------------------BACKGROUND
screen.fill((204, 0, 0))
background = pygame.image.load("img/red.mist.jpg")
screen.blit(background, (0, 0))
bottom_dash = pygame.draw.rect(screen, (212, 212, 212), (0, 350, 640, 440), 0)
pygame.display.update()

# -----------------------------------------FONT/TEXT

pygame.display.update()

# -----------------------------------------VARIABLES
pygame.display.update()

# -----------------------------------------EVENT


while running:
    # screen.fill([255, 255, 255])
    # screen.blit(BackGround.image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()

pygame.display.flip()

# Finish Pygame.
pygame.quit()
