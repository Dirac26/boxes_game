import pygame
import maps
import tkinter as tk
import map_run
import buttons
from tkinter import messagebox
from entities import grass, rock, hole, player, box, empty

class Game:
    def __init__(self, width=800):
        self.width = width
        self.window = pygame.display.set_mode((self.width, self.width))
        self.clock = pygame.time.Clock()
        self.buttons = []
        self.maps = [maps.Map1(), maps.Map1(), maps.Map1()]
        pygame.init()
        for i, m in enumerate(self.maps):
            button_width = self.width/10
            spacing_width = self.width/20
            self.buttons.append(buttons.Button(button_width, button_width, (1.5*i*button_width+spacing_width, spacing_width), m.get_name, m))
        self.selected_level = self.select_level()
        self.run_game(self.selected_level)
        

    def select_level(self):
        not_selected = True
        sel_map = None
        while not_selected:
            pygame.event.pump()
            pygame.time.delay(5)
            self.clock.tick(10)
            for butt in self.buttons:
                sel_map = butt.check()
                if not sel_map:
                    self.re_make_selection_window(self.window)
                    continue
                else:
                    not_selected = False
                    break
        return sel_map

    
    def re_make_selection_window(self, surf):
        surf.fill((255, 255, 255))
        self.make_buttons(surf)
        pygame.display.update()

    def make_buttons(self, surf):
        for butt in self.buttons:
            butt.draw(surf)
        

    def run_game(self, map_to_play):
        map_run.RunMap(map_to_play, self.window, self.width, self.clock).run_map()


    def print_message(self, subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass

game = Game()
