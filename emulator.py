# Alternative smoother remake of the kandinsky emulator
# Fonts directly taken from the original lib

import pygame
import sys
import os
import time

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 222

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Works (emulator)")

clock = pygame.time.Clock()

def resource_path(relative: str):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

large_font = pygame.font.Font(resource_path("resources/large_font.ttf"), 16)
small_font = pygame.font.Font(resource_path("resources/small_font.ttf"), 14)

def fill_rect(x: int, y: int, w: int, h: int, color: tuple[int, int, int]):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))

def draw_string(text: str, x: int, y: int, color: tuple[int, int, int], background: tuple[int, int, int], font: bool | None = False):
    if not font:
        text_surface = large_font.render(text, True, color, background)
    else:
        text_surface = small_font.render(text, True, color, background)
    screen.blit(text_surface, (x, y))

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(30)

def sleep(seconds: float):
    start = time.time()
    while time.time() - start < seconds:
        pygame.event.pump()
        pygame.time.delay(1)
