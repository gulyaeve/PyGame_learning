import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
rectangle = pygame.Rect(50, 50, 100, 50)


while True:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rectangle.move_ip(0, -5)
            if event.key == pygame.K_DOWN:
                pass

    pygame.draw.rect(screen, "white", rectangle, 0)

    pygame.display.flip()