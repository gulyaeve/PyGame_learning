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

        if event.type == pygame.KEYUP:
            rectangle.move_ip(0, -5)

    pygame.draw.rect(screen, "white", rectangle, 0)

    pygame.display.flip()
