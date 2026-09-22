import pygame
from config import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,
                     (255, 255, 255),
                     (ARENA_LEFT, ARENA_TOP, (ARENA_RIGHT - ARENA_LEFT), (ARENA_BOTTOM - ARENA_TOP)),
                     2
                     )

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
