import random
from block import Block
from settings import *

SHAPES = {
    "I": [(0,0),(1,0),(2,0),(3,0)],
    "O": [(0,0),(1,0),(0,1),(1,1)],
    "T": [(1,0),(0,1),(1,1),(2,1)],
    "L": [(0,0),(0,1),(0,2),(1,2)],
    "J": [(1,0),(1,1),(1,2),(0,2)],
    "S": [(1,0),(2,0),(0,1),(1,1)],
    "Z": [(0,0),(1,0),(1,1),(2,1)]
}

COLORS = {
    "I": (0,255,255),
    "O": (255,255,0),
    "T": (128,0,128),
    "L": (255,165,0),
    "J": (0,0,255),
    "S": (0,255,0),
    "Z": (255,0,0)
}

class Tetromino:
    def __init__(self, grid):
        self.grid = grid
        self.type = random.choice(list(SHAPES.keys()))
        self.color = COLORS[self.type]
        self.blocks = [Block(x + 3, y, self.color) for (x,y) in SHAPES[self.type]]
        self.fall_time = 0

    def move(self, dx, dy):
        if not self.can_move(dx, dy):
            return False
        
        for b in self.blocks:
            b.x += dx
            b.y += dy

        return True
    
    def rotate(self):
        pivot = self.blocks[0]
        new_positions = []

        for b in self.blocks:
            x = b.y - pivot.y
            y = b.x - pivot.x
            new_x = pivot.x - x
            new_y = pivot.y + y
            new_positions.append((new_x, new_y))

        if all(0 <= x < COLS and 0 <= y < ROWS and self.grid.cells[y][x] == (0,0,0) for x,y in new_positions):
            for i, b in enumerate(self.blocks):
                b.x, b.y = new_positions[i]

    def can_move(self, dx, dy):
        for b in self.blocks:
            new_x = b.x + dx
            new_y = b.y + dy

            if new_x < 0 or new_x >= COLS:
                return False
            
            if new_y >= ROWS or self.grid.cells[new_y][new_x] != (0, 0, 0):
                return False
            
        return True

    def draw(self, screen):
        for b in self.blocks:
            b.draw(screen)
