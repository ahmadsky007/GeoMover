import pygame
import sys

pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
white = (255, 255, 255)
square_size = 20
square_color = white
square_x = screen_width // 2
square_y = screen_height // 2
square_speed = 5

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_y -= square_speed
    if keys[pygame.K_s]:
        square_y += square_speed
    if keys[pygame.K_a]:
        square_x -= square_speed
    if keys[pygame.K_d]:
        square_x += square_speed

    
    square_x = max(0, min(screen_width - square_size, square_x))
    square_y = max(0, min(screen_height - square_size, square_y))

    screen.fill(black)

    pygame.draw.rect(screen, square_color, [square_x, square_y, square_size, square_size])

    pygame.display.flip()


    clock.tick(60)

pygame.quit()
sys.exit()
