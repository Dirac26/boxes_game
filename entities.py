import pygame
from abc import ABC, abstractclassmethod

black = (0, 0, 0)
which = (255, 255, 255)
graj = (192, 192, 192)
green = (0, 128, 0)
brown = (150, 75, 0)
red = (255, 0, 0)

class block(ABC):
    def __init__(self, content):
        self.content = content
    
    @abstractclassmethod
    def draw(self, surf, pos, block_size):
        pass

class grass(block):
    def draw(self, surf,  pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, green, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
        self.content.draw(surf,  pos, block_size)


class hole(block):
    def draw(self, surf,  pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, green, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
        r = block_size / 2
        color = black
        center = (i*block_size + r, j*block_size + r)
        pygame.draw.circle(surf, color, center, r)
        self.content.draw(surf,  pos, block_size)


class content(ABC):
    @abstractclassmethod
    def get_color(self):
        pass

    @abstractclassmethod
    def draw(self, surf, pos, block_size):
        pass

class rock(content):
    def get_color(self):
        return graj
    
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        pygame.draw.rect(surf, color, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
        

class box(content):
    def get_color(self):
        return brown

    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        redu = block_size / 6
        pygame.draw.rect(surf, color, ((i*block_size+1)+redu, j*block_size+1+redu, block_size-2- 2*redu, block_size-2- 2*redu))

class player(content):
    def get_color(self):
        return red
    
    def move(self, level):
        dir_x, dir_y, backward = self.get_input()
        self.pos = self.get_position(level)
        i = self.pos[0]
        j = self.pos[1]
        current = level[(i, j)]
        next_elm = level[(i + dir_x, j + dir_y)]
        next_ent = next_elm.content
        back_elm = level[(i - dir_x, j - dir_y)]
        back_ent = back_elm.content
        try:
            next_next_elm = level[(i + 2*dir_x, j + 2*dir_y)]
        except:
            next_next_elm = grass(rock())
        next_next_ent = next_next_elm.content
        if not backward:
            if isinstance(next_ent, rock):
                return
            elif isinstance(next_ent, empty):
                current.content = empty()
                next_elm.content = self
            elif isinstance(next_ent, box) and isinstance(next_next_ent, box):
                return
            elif isinstance(next_ent, box) and isinstance(next_next_ent, rock):
                return
            elif isinstance(next_ent, box) and isinstance(next_next_ent, empty):
                current.content = empty()
                next_elm.content = self
                next_next_elm.content = box()
        else:
            if isinstance(back_ent, box) and isinstance(next_ent, empty):
                current.content = box()
                back_elm.content = empty()
                next_elm.content = self

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                c_key = True if keys[pygame.K_c] else False
                if keys[pygame.K_LEFT]:
                    return -1, 0, c_key
                
                elif keys[pygame.K_RIGHT]:
                    return 1, 0, c_key

                elif keys[pygame.K_UP]:
                    return 0, -1, c_key

                elif keys[pygame.K_DOWN]:
                    return 0, 1, c_key
        return 0, 0, False


    def get_position(self, level):
        for pos, ent in level.items():
            if isinstance(ent.content, player):
                return pos

    def draw(self, surf, pos, block_size):
        i = pos[0] * block_size
        j = pos[1] * block_size
        half_block = block_size / 2
        color = self.get_color()
        redu = block_size / 4
        # Head
        pygame.draw.ellipse(surf, red, [block_size/2 + i- redu/2, j+block_size/4, redu, 10], 0)
    
        # Legs
        pygame.draw.line(surf, red,  [i+block_size/2, j+block_size/2],  [i+block_size*.75, j+block_size], 4)
        pygame.draw.line(surf, red,  [i+block_size/2, j+block_size/2],  [i+block_size/4, j+block_size+block_size/4], 4)
    
        # Body
        pygame.draw.line(surf, red, [i+block_size/2, j+block_size/4], [i+block_size/2, j+block_size/2], 4)
    
        # Arms
        pygame.draw.line(surf, red, [i+block_size/2, j+block_size/4], [i+block_size*.75, j+block_size-block_size*.4], 4)
        pygame.draw.line(surf, red, [i+block_size/2, j+block_size/4], [i+block_size/4, j+block_size+block_size/8-block_size/2], 4)

class empty(content):
    def get_color(self):
        return green
    def draw(self, surf, pos, block_size):
        pass