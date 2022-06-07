import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")
bg = pygame.image.load("background.jpg")
icon = pygame.image.load("iron.jpg")
pygame.display.set_icon(icon)
while True:
    screen.blit(bg,(0,0))
    pygame.display.update()
    
            
if __name__ == "__main__":
    pass