import pygame
from settings import *
from grid import Grid
from tetromino import Tetromino

class Tetris:
    def __init__(self):
        self.grid = Grid()
        self.current_piece = Tetromino(self.grid)
        self.last_fall = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_fall > FALL_SPEED:
            if not self.current_piece.move(0, 1):
                self.lock_piece()
                self.new_piece()

            self.last_fall = now

    def lock_piece(self):
        for b in self.current_piece.blocks:
            if b.y >= 0:
                self.grid.cells[b.y][b.x] = b.color

    def new_piece(self):
        self.current_piece = Tetromino(self.grid)

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_piece.draw(screen)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.current_piece.move(-1, 0)
            if event.key == pygame.K_RIGHT:
                self.current_piece.move(1, 0)
            if event.key == pygame.K_DOWN:
                self.current_piece.move(0, 1)
