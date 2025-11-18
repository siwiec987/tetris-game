import pygame
from settings import *

class Dodo:
    def __init__(self, x, y):
        sheet = pygame.image.load('resources/dodo.png').convert_alpha()
        sw, sh = sheet.get_size()
        self.cols = 3
        self.rows = 4
        self.frame_width = sw // self.cols
        self.frame_height = sh // self.rows

        row_map = { "back": 0, "right": 1, "front": 2, "left": 3 }
        self.frames = {}
        for direction, row in row_map.items():
            self.frames[direction] = []
            for col in range(self.cols):
                frame = sheet.subsurface(
                    col * self.frame_width,
                    row * self.frame_height,
                    self.frame_width,
                    self.frame_height
                )
                self.frames[direction].append(frame)

        self.sequence = [0, 1, 2]
        self.sequence_index = 0
        self.frame_ms = 150
        self.last_frame_tick = pygame.time.get_ticks()

        self.x = x
        self.y = y + self.frame_height
        self.vx = 2

        self.direction = "left"

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_frame_tick >= self.frame_ms:
            self.sequence_index = (self.sequence_index + 1) % len(self.sequence)
            self.last_frame_tick = now

        self.x += self.vx
        if self.x + self.frame_width >= GRID_WIDTH or self.x <= 0:
            self.vx = -self.vx
            if self.vx > 0:
                self.direction = "left"
            else:
                self.direction = "right"

    def draw(self, screen):
        frame = self.frames[self.direction][self.sequence[self.sequence_index]]
        rotated = pygame.transform.rotate(frame, 180)
        screen.blit(rotated, (self.x, self.y - self.frame_height))