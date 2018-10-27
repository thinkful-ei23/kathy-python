import pygame
import pygame.display
import os
import sys
from random import randint

pygame.init()
pygame.display.init()
# -----------------------------------------
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music House - Blue room")
done = False
# -----------------------------------------BACKGROUND
screen.fill([0, 0, 255])


# class Background(pygame.sprite.Sprite):
#     def __init__(self, navy, screen):
#         pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
#         self.image = pygame.image.load("img/blue_dark.jpg")
#         self.Simage = pygame.transform.scale(self.image, (640, 480))
#         self.rect = self.Simage.get_rect()
#         self.rect.left, self.rect.top = 0, 0


# BackGround = Background("img/navy_bokeh_scene.jpeg", [0, 0])
bottom_dash = pygame.draw.rect(screen, (0, 0, 0), (0, 350, 640, 440), 0)
pygame.display.update()
# -----------------------------------------VARIABLES
# list of numbers and images of CS Unit 1 patterns
dicPatt = {1: 1211, 2: 2121, 3: 2211,
           + 4: 2122, 5: 2221, 6: 1221,
           + 7: 2111, 8: 1121}
dicImage = {1: "img/CS_Unit1/1.jpg", 2: "img/CS_Unit1/2.jpg", 3: "img/CS_Unit1/3.jpg",
            + 4: "img/CS_Unit1/4.jpg", 5: "img/CS_Unit1/5.jpg", 6: "img/CS_Unit1/6.jpg",
            + 7: "img/CS_Unit1/7.jpg", 8: "img/CS_Unit1/8.jpg"}
# -------------------------------------IMAGES of notes
quarter1 = pygame.image.load('img/quarter1.png')
eighth2 = pygame.image.load('img/eighth2.png')
Seighth2 = pygame.transform.scale(eighth2, (90, 84))
quarter_sm = pygame.transform.scale(quarter1, (24, 48))
eighth_sm = pygame.transform.scale(eighth2, (45, 42))
# -------------------------------------BOXES as frames for pattern
box1 = pygame.draw.rect(screen, (255, 255, 255), (40, 100, 140, 100), 0)
box2 = pygame.draw.rect(screen, (255, 255, 255), (180, 100, 140, 100), 0)
box3 = pygame.draw.rect(screen, (255, 255, 255), (320, 100, 140, 100), 0)
box4 = pygame.draw.rect(screen, (255, 255, 255), (460, 100, 140, 100), 0)

# num = dicPatt[value]
# pic = dicImage[value]
quarter_click = 0
eighth_click = 0
font = pygame.font.SysFont("Arial", 30)
running = True
pygame.display.update()

# -----------------------------------------BUTTONS
# btn1 = pygame.draw.rect(screen, (255, 255, 255), (400, 370, 100, 100), 0)
# screen.blit(quarter1, (420, 370))

# btn2 = pygame.draw.rect(screen, (255, 255, 255), (530, 370, 100, 100), 0)
# screen.blit(Seighth2, (534, 380))

btn3_1 = pygame.draw.rect(screen, (220, 220, 220), (50, 225, 50, 50), 0)
screen.blit(quarter_sm, (50, 225))
btn3_2 = pygame.draw.rect(screen, (220, 220, 220), (200, 225, 50, 50), 0)
screen.blit(quarter_sm, (200, 225))
btn3_3 = pygame.draw.rect(screen, (220, 220, 220), (350, 225, 50, 50), 0)
screen.blit(quarter_sm, (350, 225))
btn3_4 = pygame.draw.rect(screen, (220, 220, 220), (500, 225, 50, 50), 0)
screen.blit(quarter_sm, (500, 225))

btn4_1 = pygame.draw.rect(screen, (220, 220, 220), (100, 225, 50, 50), 0)
screen.blit(eighth_sm, (100, 225))
btn4_2 = pygame.draw.rect(screen, (220, 220, 220), (250, 225, 50, 50), 0)
screen.blit(eighth_sm, (250, 225))
btn4_3 = pygame.draw.rect(screen, (220, 220, 220), (400, 225, 50, 50), 0)
screen.blit(eighth_sm, (400, 225))
btn4_4 = pygame.draw.rect(screen, (220, 220, 220), (550, 225, 50, 50), 0)
screen.blit(eighth_sm, (550, 225))

pygame.draw.line(screen, (0, 0, 0), (315, 110), (315, 190), 3)
pygame.draw.line(screen, (0, 0, 0), (585, 110), (585, 190), 3)
pygame.draw.line(screen, (0, 0, 0), (597, 110), (597, 190), 7)

pygame.display.update()
# -----------------------------------------FONT-TEXT
# font ("name", size)
font = pygame.font.SysFont("Ariel", 28)
# text = ("String", True, (color))
text1 = font.render("1.  Listen to the pattern", True, (245, 245, 245))
text2 = font.render("2.  Decode the pattern in your head",
                    True, (245, 245, 245))
text3 = font.render("3.  Click the button underneath each beat",
                    True, (245, 245, 245))
text4 = font.render("     to write the rhythm pattern", True, (245, 245, 245))
# blit(text, (location x,y))
screen.blit(text1, (9, 353))
screen.blit(text2, (9, 383))
screen.blit(text3, (9, 413))
screen.blit(text4, (9, 443))
pygame.display.update()
# -----------------------------------------EVENT for BTN


# -----------------------------------------

# -----------------------------------------


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x > 49 and x < 100 and y > 224 and y < 276:
                quarter1 = pygame.image.load("img/quarter1.png")
                screen.blit(quarter1, (40, 105))
                pygame.display.update()
            elif x > 199 and x < 251 and y > 224 and y < 276:
                quarter1 = pygame.image.load("img/quarter1.png")
                screen.blit(quarter1, (180, 105))
                pygame.display.update()
            elif x > 349 and x < 401 and y > 224 and y < 276:
                quarter1 = pygame.image.load("img/quarter1.png")
                screen.blit(quarter1, (320, 105))
                pygame.display.update()
            elif x > 449 and x < 551 and y > 224 and y < 276:
                quarter1 = pygame.image.load("img/quarter1.png")
                screen.blit(quarter1, (450, 105))
                pygame.display.update()
                # -------------------
# pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                # -----------

            elif x > 99 and x < 151 and y > 224 and y < 276:
                eighth2 = pygame.image.load("img/eighth2.png")
                screen.blit(eighth2, (40, 105))
                pygame.display.update()
            elif x > 249 and x < 301 and y > 224 and y < 276:
                eighth2 = pygame.image.load("img/eighth2.png")
                screen.blit(eighth2, (180, 105))
                pygame.display.update()
            elif x > 399 and x < 451 and y > 224 and y < 276:
                eighth2 = pygame.image.load("img/eighth2.png")
                screen.blit(eighth2, (320, 105))
                pygame.display.update()
            elif x > 549 and x < 601 and y > 224 and y < 276:
                eighth2 = pygame.image.load("img/eighth2.png")
                screen.blit(eighth2, (450, 105))
                pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                click = 0
# -----------------------------------------
pygame.display.flip()

# Finish Pygame.
pygame.quit()
