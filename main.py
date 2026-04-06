import pygame
import sys

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rat-Z")
clock = pygame.time.Clock()

player_color = (200, 200, 200) 
player_width = 40
player_height = 60
player_x = SCREEN_WIDTH // 2  
player_y = SCREEN_HEIGHT // 2
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed

    screen.fill((30, 30, 30))  
    
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()