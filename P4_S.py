import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((210,600))

gun = pygame.Rect(100,500,10,50)
bullet = pygame.Rect(100,500,10,10)
enemy = pygame.Rect(80,100,50,10)

bullet_state = "stable"

enemy_x_change = 1
bullet_y_change = -1

while True:    
    screen.fill((150,75,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_state = "fire"
    
    if bullet_state == "fire":
        bullet.y = bullet.y - 1
     
    if bullet.y < 0:
        bullet.y = 500
        bullet_state = "stable"
    
    if enemy.x > 160:
        enemy_x_change = -1
    if enemy.x < 0:
        enemy_x_change = 1
        
    enemy.x += enemy_x_change
    
    pygame.draw.rect(screen,(255,255,255),bullet)
    pygame.draw.rect(screen,(0,0,0),gun)
    pygame.draw.rect(screen,(0,0,0),enemy)
    
    if bullet.colliderect(enemy):
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()