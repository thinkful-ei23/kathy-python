import pygame
import pygame.display
import os
import sys
from random import randint

pygame.init()
pygame.display.init()
# -----------------------------------------

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music House - Blue door")
done = False
# -----------------------------------------BACKGROUND
# screen.fill((0, 0, 204))


class Background(pygame.sprite.Sprite):
    def __init__(self, navy, screen):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load("img/blue_dark.jpg")
        self.Simage = pygame.transform.scale(self.image, (640, 480))
        self.rect = self.Simage.get_rect()
        self.rect.left, self.rect.top = 0, 0


BackGround = Background("img/navy_bokeh_scene.jpeg", [0, 0])

bottom_dash = pygame.draw.rect(screen, (0, 0, 0), (0, 350, 640, 440), 0)

# -----------------------------------------VARIABLES
# list of numbers relating to CS Unit 1 patterns
dicPatt = {1: 1211, 2: 2121, 3: 2211,
           + 4: 2122, 5: 2221, 6: 1221,
           + 7: 2111, 8: 1121}
dicImage = {1: "img/CS_Unit1/1.jpg", 2: "img/CS_Unit1/2.jpg", 3: "img/CS_Unit1/3.jpg",
            + 4: "img/CS_Unit1/4.jpg", 5: "img/CS_Unit1/5.jpg", 6: "img/CS_Unit1/6.jpg",
            + 7: "img/CS_Unit1/7.jpg", 8: "img/CS_Unit1/8.jpg"}
# quarter1 = pygame.image.load('img/quarter1.png')
# eighth2 = pygame.image.load('img/eighth2.png')
# Seighth2 = pygame.transform.scale(eighth2, (90, 84))
eighth2 = pygame.image.load('img/eighth2.png')
Seighth2 = pygame.transform.scale(eighth2, (90, 84))
box1 = pygame.draw.rect(screen, (255, 255, 255), (50, 100, 100, 100), 3)
box2 = pygame.draw.rect(screen, (255, 255, 255), (190, 100, 100, 100), 3)
box3 = pygame.draw.rect(screen, (255, 255, 255), (340, 100, 100, 100), 3)
box4 = pygame.draw.rect(screen, (255, 255, 255), (480, 100, 100, 100), 3)

screen.blit(Seighth2, (534, 380))
pygame.display.update()

# num = dicPatt[value]
# pic = dicImage[value]
quarter_clicks = 0
eighth_clicks = 0
font = pygame.font.SysFont("Arial", 30)
running = True

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
font = pygame.font.SysFont("Ariel", 28)
# text = ("String", True, (color))
text1 = font.render("1.  Listen to the pattern", True, (245, 245, 245))
text2 = font.render("2.  Decode the pattern in your head",
                    True, (245, 245, 245))
text3 = font.render("3.  Click the buttons on the right",
                    True, (245, 245, 245))
text4 = font.render("     to write the rhythm pattern", True, (245, 245, 245))
# blit(text, (location x,y))
screen.blit(text1, (5, 353))
screen.blit(text2, (5, 383))
screen.blit(text3, (5, 413))
screen.blit(text4, (5, 443))
pygame.display.update()
# -----------------------------------------EVENT for BTN

# -----------------------------------------

# -----------------------------------------


def update_patt(clicks):

    playerList.append(clicks)
    pygame.draw.rect(screen, (255, 153, 000), (25, 100, 75, 50), 0)
    screen.blit(font.render(str(playerList), True, (000, 000, 255)), (50, 100))
# -----------------------------------------


while running:
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x > 399 and x < 501 and y > 369 and y < 470:
                quarter_clicks = 1
                # update_disp(font, quarter_clicks)
                update_patt(quarter_clicks)
            elif x > 529 and x < 630 and y > 369 and y < 470:
                eighth_clicks = 2
                # update_disp(font, eighth_clicks)
                update_patt(eighth_clicks)
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
