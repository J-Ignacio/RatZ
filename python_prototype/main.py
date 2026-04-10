import pygame
import sys

# 1. Configuración inicial del motor
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rat-Z: Survival en el Block")
clock = pygame.time.Clock()

# --- Propiedades del Jugador (The Rat) ---
player_color = (200, 200, 200) # Gris Rata
player_width = 40
player_height = 60
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 7

# --- Variables de Física ---
player_y_speed = 0    
gravity = 0.8         # Fuerza que te tira hacia abajo
jump_force = -18      # Potencia de salto (negativo para subir)
is_grounded = False   # Sensor de suelo

# 2. Bucle principal (Game Loop)
running = True
while running:
    # --- 1. Manejo de Eventos (Cerrar ventana) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- 2. Lógica de Movimiento y Física ---
    keys = pygame.key.get_pressed()
    
    # Movimiento Horizontal (A/D o Flechas)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed

    # Aplicar Gravedad constante
    player_y_speed += gravity    
    player_y += player_y_speed   

    # COLISIÓN CON EL SUELO (Límite inferior de la pantalla)
    # Importante: Esto ocurre ANTES del salto para resetear el is_grounded
    if player_y >= SCREEN_HEIGHT - player_height:
        player_y = SCREEN_HEIGHT - player_height
        player_y_speed = 0       
        is_grounded = True       
    else:
        is_grounded = False      

    # MECÁNICA DE SALTO (Solo si está tocando el suelo)
    if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and is_grounded:
        player_y_speed = jump_force
        is_grounded = False # Despegamos inmediatamente

    # LÍMITES LATERALES (Paredes de la pantalla)
    if player_x < 0: 
        player_x = 0
    if player_x > SCREEN_WIDTH - player_width: 
        player_x = SCREEN_WIDTH - player_width
        
    # Límite superior (Techo invisible)
    if player_y < 0:
        player_y = 0
        player_y_speed = 0

    # --- 3. Renderizado (Dibujo) ---
    screen.fill((30, 30, 30))  # Fondo oscuro post-apocalíptico
    
    # Dibujar a la Rata (Rectángulo gris)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    
    pygame.display.flip()  # Actualizar pantalla
    clock.tick(60)         # Mantener 60 cuadros por segundo

pygame.quit()
sys.exit()   