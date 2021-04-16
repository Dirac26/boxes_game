import pygame

black = (0, 0, 0)
which = (255, 255, 255)
gray = (192, 192, 192)
green = (0, 128, 0)
brown = (150, 75, 0)
red = (255, 0, 0)

class Button:
    def __init__(self, width, leng, pos, text, ret_obj):
        self.width = width
        self.length = leng
        self.pos = pos
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.length)
        self.text = self.font.render(text, True, black)
        self.return_obj = ret_obj

    def draw(self, surf):
        pygame.draw.rect(surf, gray, self.rect)
        surf.blit(self.text, (self.pos[0]+self.width/10, self.pos[1]+self.length/4))

    def check(self, pos):
            if self.rect.collidepoint(pos[0], pos[1]):
                return self.return_obj