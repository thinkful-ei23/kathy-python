import pygame
import pygame.display
import os
import sys
from random import randint

pygame.init()
pygame.display.init()
# -----------------------------------------

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music House - Red door")
done = False
# -----------------------------------------BACKGROUND
screen.fill((204, 0, 0))
bottom_dash = pygame.draw.rect(screen, (0, 0, 0), (0, 350, 640, 440), 0)

# -----------------------------------------BUTTONS
quarter1 = pygame.image.load('img/quarter1.png')
btn1 = pygame.draw.rect(screen, (255, 255, 255), (400, 370, 100, 100), 0)
screen.blit(quarter1, (420, 370))

eighth2 = pygame.image.load('img/eighth2.png')
Seighth2 = pygame.transform.scale(eighth2, (90, 84))
btn2 = pygame.draw.rect(screen, (255, 255, 255), (530, 370, 100, 100), 0)
screen.blit(Seighth2, (534, 380))
pygame.display.update()
# -----------------------------------------FONT-TEXT
# font ("name", size)
font = pygame.font.SysFont("Ariel", 32)
# text = ("String", True, (color))
text1 = font.render("Click the buttons on the right", True, (111, 111, 111))
text2 = font.render(" to build a rhythm pattern", True, (111, 111, 111))
# blit(text, (location x,y))
screen.blit(text1, (10, 380))
screen.blit(text2, (10, 415))
pygame.display.update()


# -----------------------------------------VARIABLES
# list of numbers relating to CS Unit 1 patterns
dicPatt = {1: 1211, 2: 2121, 3: 2211,
           + 4: 2122, 5: 2221, 6: 1221,
           + 7: 2111, 8: 1121}
dicImage = {1: "img/CS_Unit1/1.jpg", 2: "img/CS_Unit1/2.jpg", 3: "img/CS_Unit1/3.jpg",
            + 4: "img/CS_Unit1/4.jpg", 5: "img/CS_Unit1/5.jpg", 6: "img/CS_Unit1/6.jpg",
            + 7: "img/CS_Unit1/7.jpg", 8: "img/CS_Unit1/8.jpg"}

start = 1
end = 8
value = randint(start, end)

num = dicPatt[value]
pic = dicImage[value]
playerList = []
quarter_clicks = 0
eighth_clicks = 0
font = pygame.font.SysFont("Arial", 50)
running = True

# -----------------------------------------

# -----------------------------------------EVENT for BTN



# -----------------------------------------
def update_patt(clicks):
    playerList.insert(-1, )
    pygame.draw.rect(screen, (255, 153, 000), (25, 100, 75, 50), 0)
    screen.blit(font.render(str(clicks),
                            True, (000, 255, 000)), (25, 100))
    screen.blit(font.render(str(playerList), True, (000, 000, 255)), (50, 100))

# insert
# -----------------------------------------


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x > 399 and x < 501 and y > 369 and y < 470:
                clicks = 1
                # update_disp(font, quarter_clicks)
                update_patt(clicks)
            elif x > 529 and x < 630 and y > 369 and y < 470:
                clicks = 2
                # update_disp(font, eighth_clicks)
                update_patt(clicks)
        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                clicks = 0
                # update_disp(font, quarter_clicks, eighth_clicks)
# -----------------------------------------
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

    pygame.display.flip()

# Finish Pygame.
pygame.quit()
