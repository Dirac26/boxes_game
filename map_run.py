import pygame
import maps
import tkinter as tk
from tkinter import messagebox
from entities import grass, rock, hole, player, box, empty


class RunMap:
    def __init__(self, map_obj, surf, width, clock):
        self.map = map_obj
        self.surf = surf
        self.width = width
        self.rows = len(map_obj)
        self.clock = clock
        self.player = self.map.get_player()
        self.level = self.make_level_dict()

    def make_level_dict(self):
        level = {}
        for j, row in enumerate(self.map.level):
            for i, ent in enumerate(row):
                level[(i, j)] = ent
        return level


    def make_grid(self, surf):
        self.block_size = self.width / self.rows
        x, y = 0, 0
        for line in range(self.rows):
            x += self.block_size
            y += self.block_size
            pygame.draw.line(surf, (255, 255, 255), (x, 0), (x, self.width))
            pygame.draw.line(surf, (255, 255, 255),(0, y), (self.width, y))

    def re_make_window(self, surf, level):
        surf.fill((255, 255, 255))
        self.make_grid(surf)
        for pos, ent in level.items():
            ent.draw(surf, pos, self.block_size)
        pygame.display.update()

    def check_win_con(self, level):
        for pos, ent in level.items():
            if isinstance(ent, hole):
                if not isinstance(ent.content, box):
                    return False
        return True
    
    def run_map(self):
        level_not_done = True
        while level_not_done:
            pygame.event.pump()
            pygame.time.delay(5)
            self.clock.tick(10)
            self.player.move(self.level)
            win_con = self.check_win_con(self.level)
            if win_con:
                return
            self.re_make_window(self.surf, self.level)


