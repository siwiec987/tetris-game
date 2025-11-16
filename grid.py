import pygame
from settings import *

class Grid:
    def __init__(self):
        self.cells = [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]

    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                color = self.cells[row][col]
                pygame.draw.rect(
                    screen,
                    color,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    0
                )

                pygame.draw.rect(
                    screen,
                    (40, 40, 40),
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    1
                )
