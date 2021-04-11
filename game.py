import pygame
import maps
from entities import grass, rock, hole, player, box, empty

def make_grid(surf):
    size_block = width / rows
    x, y = 0, 0
    for line in range(rows):
        x += size_block
        y += size_block
        pygame.draw.line(surf, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surf, (255, 255, 255),(0, y), (width, y))

def re_make_window(surf):
    surf.fill((255, 255, 255))
    make_grid(surf)
    pygame.display.update()

def game():
    global width, rows, block_size
    width = 800
    rows = 100
    block_size = width / rows
    window = pygame.display.set_mode((width, width))
    clock = pygame.time.Clock()
    game_on = True
    level, p, b1, b2, b3, h1, h2, h3 = maps.get_level_1()
    while game_on:
        pygame.event.pump()
        pygame.time.delay(5)
        clock.tick(10)
        re_make_window(window)

game()