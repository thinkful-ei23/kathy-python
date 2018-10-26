import pygame
import pygame.display
from pygame.locals import *
import os
import sys


pygame.init()

screen = pygame.display.set_mode((200, 200))

pygame.draw.rect(screen, (000, 255, 000), (25, 25, 50, 50), 0)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
