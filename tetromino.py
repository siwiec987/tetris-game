import random
from block import Block

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
        for b in self.blocks:
            b.x += dx
            b.y += dy

    def draw(self, screen):
        for b in self.blocks:
            b.draw(screen)
