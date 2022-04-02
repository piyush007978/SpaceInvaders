import pygame

screenWidth = 800
screenHeight = 600
pygame.init()

screen = pygame.display.set_mode((screenWidth,screenHeight))

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('spaceship.png')
playerX = screenWidth/2
playerY = screenHeight*0.9

def player(x,y):
    screen.blit(playerImg,(x,y))

pygame.display.set_caption("Space Invaders")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == py

    screen.fill((12,43,23))
    player(playerX,playerY)
    pygame.display.update()