import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
# rectangle = pygame.Rect(50, 50, 100, 50)
player_sprite = pygame.image.load("test_sprite.png")

player_x = 50
player_y = 50

while True:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= 5
            if event.key == pygame.K_DOWN:
                player_y += 5
            if event.key == pygame.K_RIGHT:
                player_x += 5
            if event.key == pygame.K_LEFT:
                player_x -= 5

    # pygame.draw.rect(screen, "white", rectangle, 0)
    screen.blit(player_sprite, (player_x, player_y))

    pygame.display.flip()
