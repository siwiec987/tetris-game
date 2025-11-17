import pygame
from settings import *

class Grid:
    def __init__(self):
        self.cells = [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]

    def clear_lines(self):
        full_rows = 0
        row = ROWS - 1

        while row >= 0:
            if all(self.cells[row][col] != (0, 0, 0) for col in range(COLS)):
                del self.cells[row]
                self.cells.insert(0, [(0, 0, 0) for _ in range(COLS)])
                full_rows += 1
            else:
                row -= 1

        return full_rows


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
