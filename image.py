import pygame
import os
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Image for buttons")
done = False

# create empty pygame surface
background = pygame.Surface(screen.get_size())
# fill the background with color
background.fill((0, 51, 153))
# Convert Surface object to make blitting faster.
background = background.convert()
# Copy background to screen (position (0, 0) is upper left corner).
screen.blit(background, (0, 0))

# create game area above and below
# (surface, (color), (x,y, width, height), lineWidth(0=fill))
pygame.draw.rect(screen, (51, 102, 153), (0, 350, 640, 440), 0)
# create rectangle buttons
# pygame.draw.rect(screen, color, (x,y,width,height), thickness)
pygame.draw.rect(screen, (230, 255, 229), (200, 360, 100, 100),  0)
pygame.draw.rect(screen, (204, 204, 255), (400, 360, 100, 100),  0)

print("Click on the notes to build a pattern")
quarter1 = pygame.image.load('img/quarter1.png')
screen.blit(quarter1, (210, 360))
eighth2 = pygame.image.load('img/eighth2.png')
screen.blit(eighth2, (404, 365))


# dicPatt = pygame.image.load('img/CS_Unit1/1.jpg')
# screen.blit(dicPatt, (0, 100))
# dicPatt2 = pygame.image.load('img/CS_Unit1/2.jpg')
# screen.blit(dicPatt2, (0, 200))
# dicPatt3 = pygame.image.load('img/CS_Unit1/3.jpg')
# screen.blit(dicPatt3, (0, 300))
# surface = pygame.Surface((100, 100), pygame.SRCALPHA)
# while True:

print("I'm a game board")
# render("I'm the board, not you!")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

# Finish Pygame.
pygame.quit()
