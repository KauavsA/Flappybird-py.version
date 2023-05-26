import pygame
from pygame.locals import *

class bird (pygame.sprite.Sprite):
    def __init__(self,speed,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('imagens/bluebird-unflap.png').convert_alpha (),
                       pygame.image.load('imagens/bluebird-midflap.png').convert_alpha (),
                       pygame.image.load('imagens/bluebird-downflap.png').convert_alpha ()]
        self.speed = speed
        self.current_image = 0
        self.images = pygame.image.load('imagens/bluebird-unflap.png').convert_alpha ()
        self.mask = pygame.mask.from_surface(self.images)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def update(self,gravity):
        self.current_image = (self.current_image +1) % 3
        self.images = self.image[self.current_image]
        self.speed += gravity
        self.rect[1] += self.speed

    def bump(self,speed):
        self.speed = speed