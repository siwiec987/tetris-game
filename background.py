import pygame
from settings import *

class Background:
    def __init__(self, image_path, text):
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