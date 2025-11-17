import pygame
from settings import *
from grid import Grid
from tetromino import Tetromino

class Tetris:
    def __init__(self, screen):
        self.screen = screen
        self.grid = Grid()
        self.current_piece = Tetromino(self.grid)
        self.last_fall = pygame.time.get_ticks()
        self.score = 0
        self.level = 1
        self.game_over = False
        self.play_again_rect = pygame.Rect(GRID_WIDTH + 10, 270, 180, 40)

        try:
            self.game_over_sound = pygame.mixer.Sound('resources/game-over.mp3')
        except Exception:
            self.game_over_sound = None

    def update(self):
        if self.game_over:
            self.draw_game_over()
            return

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

        self.score += self.grid.clear_lines()
        if self.score // 10 + 1 > self.level:
            self.level += 1

    def new_piece(self):
        self.current_piece = Tetromino(self.grid)
        if not self.current_piece.can_move(0, 0):
            self.game_over = True
            if self.game_over_sound:
                self.game_over_sound.play()

    def draw_game_over(self):
        font = pygame.font.SysFont("comicsans", 40, bold=True)

        text1 = font.render("KONIEC", True, (255, 0, 0))
        text2 = font.render("GRY", True, (255, 0, 0))
        self.screen.blit(text1, (GRID_WIDTH + 10, 150))
        self.screen.blit(text2, (GRID_WIDTH + 10, 200))

        button_font = pygame.font.SysFont("comicsans", 15, bold=True)
        if self.play_again_rect.collidepoint(pygame.mouse.get_pos()):
            button_color = (0, 255, 0)
        else:
            button_color = (0, 200, 0)

        pygame.draw.rect(self.screen, button_color, self.play_again_rect)
        pygame.draw.rect(self.screen, (200,200,200), self.play_again_rect, 2)

        buton_text = button_font.render("ZAGRAJ PONOWNIE", True, (255, 255, 255))
        text_rect = buton_text.get_rect(center=self.play_again_rect.center)
        self.screen.blit(buton_text, text_rect)

    def draw(self):
        self.grid.draw(self.screen)
        self.current_piece.draw(self.screen)

        font = pygame.font.SysFont("comicsans", 30)
        score_label = font.render(f"WYNIK: {self.score}", 1, (255,255,255))
        level_label = font.render(f"POZIOM: {self.level}", 1, (255,255,255))

        self.screen.blit(score_label, (GRID_WIDTH + 10, 10))
        self.screen.blit(level_label, (GRID_WIDTH + 10, 50))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.current_piece.move(-1, 0)
            if event.key == pygame.K_RIGHT:
                self.current_piece.move(1, 0)
            if event.key == pygame.K_DOWN:
                self.current_piece.move(0, 1)
            if event.key == pygame.K_UP:
                self.current_piece.rotate()

        if event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
            if self.play_again_rect.collidepoint(event.pos):
                self.reset()

    def reset(self):
        self.grid = Grid()
        self.current_piece = Tetromino(self.grid)
        self.last_fall = pygame.time.get_ticks()
        self.score = 0
        self.level = 1
        self.game_over = False

        if self.game_over_sound:
            self.game_over_sound.stop()
