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
positionXchange = 0
def player(x,y):
    screen.blit(playerImg,(x,y))

pygame.display.set_caption("Space Invaders")
running = True
while running:

    screen.fill((12,43,23))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                positionXchange = -0.3
            
            if event.key == pygame.K_RIGHT and playerX < 736:
                positionXchange = 0.3
                
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    positionXchange = 0
                    
        
        
    #print(positionXchange)
    
    playerX += positionXchange
    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736

    player(playerX,playerY)
    pygame.display.update()       
