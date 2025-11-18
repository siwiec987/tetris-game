import pygame
from settings import *

class Background:
    def __init__(self, image_path, text, text2):
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        except Exception:
            self.image = None

        self.text = text
        self.font = pygame.font.SysFont("comicsans", 40, bold=True)
        self.text_surface = self.font.render(self.text, True, (0, 255, 0))
        text_width, text_height = self.text_surface.get_size()
        self.text_x = (WIDTH - text_width) // 2
        self.text_y = (HEIGHT - text_height) // 2
        self.vx = 1.5
        self.vy = 1.5

        self.text2 = text2
        self.text2_font = pygame.font.SysFont("comicsans", 20, bold=True)
        self.text2_surface = self.text2_font.render(self.text2, True, (255, 255, 255))
        self.text2_angle = 0.0
        self.text2_va = 1.8
        self.text2_padding = 12

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (0, 0))
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.fill((0, 0, 0))
            overlay.set_alpha(120)
            screen.blit(overlay, (0, 0))

        self.text_x += self.vx
        self.text_y += self.vy

        text_width, text_height = self.text_surface.get_size()

        if self.text_x + text_width >= WIDTH or self.text_x <= 0:
            self.vx = -self.vx
        elif self.text_y + text_height >= HEIGHT or self.text_y <= 0:
            self.vy = -self.vy

        screen.blit(self.text_surface, (self.text_x, self.text_y))

        self.text2_angle = (self.text2_angle + self.text2_va) % 360
        rotated = pygame.transform.rotate(self.text2_surface, self.text2_angle)
        rotated_rect = rotated.get_rect()
        # rotated_rect.bottomright = (WIDTH - self.text2_padding, HEIGHT - self.text2_padding)
        screen.blit(rotated, (WIDTH - rotated_rect.width - self.text2_padding, HEIGHT - rotated_rect.height - self.text2_padding))