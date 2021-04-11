import pygame
import maps
from entities import grass, rock, hole, player, box, empty

black = (0, 0, 0)
which = (255, 255, 255)
gray = (192, 192, 192)
green = (0, 128, 0)
brown = (150, 75, 0)
player = (255, 255, 255)

def make_grid(surf):
    size_block = width / rows
    x, y = 0, 0
    for line in range(rows):
        x += size_block
        y += size_block
        pygame.draw.line(surf, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surf, (255, 255, 255),(0, y), (width, y))

def re_make_window(surf, level):
    surf.fill((255, 255, 255))
    make_grid(surf)
    for pos, ent in level.items():
        ent.draw(surf, pos, block_size)
    pygame.display.update()

def game():
    global width, rows, block_size
    width = 800
    rows = 8
    block_size = width / rows
    window = pygame.display.set_mode((width, width))
    clock = pygame.time.Clock()
    game_on = True
    level, p, b1, b2, b3, h1, h2, h3 = maps.get_level_1()
    while game_on:
        pygame.event.pump()
        pygame.time.delay(5)
        clock.tick(10)
        re_make_window(window, level)

game()