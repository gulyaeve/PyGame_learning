import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

rectangle = pygame.Rect(50, 50, 100, 50)
pygame.draw.rect(screen, "white", rectangle, 0)


while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
