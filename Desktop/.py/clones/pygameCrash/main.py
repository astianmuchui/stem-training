import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invader')
icon = pygame.image.load("rocket.png")
ship = pygame.image.load("space-invaders.png")
x = 370
y = 480
changeX = 0
pygame.display.set_icon(icon)
running = True

bot = pygame.image.load("chat.png")
a = random.randint(0,500)
b = random.randint(50,150)
en_changeX = 0.3
en_changeY = 0
def player(m,n):
    screen.blit(ship,(m,n))
def enemy(c,d):
    screen.blit(bot,(c,d))
while running:
    screen.fill((1,0,5))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -0.3
            if event.key == pygame.K_RIGHT:
                changeX = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0
            
            
    x +=changeX
    if x <=0:
        x = 0
    elif y >= 736:
        y = 736
        
    a+=en_changeX
    
    if a <=0:
        en_changeX = 0.3
    elif b >= 734:
        en_changeX = -0.3
    enemy(a,b)
    player(x,y)
    pygame.display.update()
