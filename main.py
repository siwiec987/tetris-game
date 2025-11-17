import pygame
import sys
from settings import *
from game import Tetris

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

game = Tetris()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        game.handle_input(event)

    screen.fill((0, 0, 0))
    game.update()
    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
