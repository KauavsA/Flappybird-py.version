from typing import Any
import pygame
from pygame.locals import *

class pipe(pygame.sprite.Sprite):
    def __init__(self,inverted,xpos,ysize,width,height,screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagens/pipe-red.png').convert_alpha
        self.image = pygame.transform.scale (self.image, (width,height))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        if inverted:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect[1] = -(self.rect[3] - ysize)
        else:
            self.Rect[1] = screen_height - ysize
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,game_speed):
        self.rect[0] -= game_speed