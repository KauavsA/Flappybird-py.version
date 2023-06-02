import pygame
from pygame.locals import *
import Grownd,Canos,Cfp
from Grownd import ground

screen_width = 400
screen_height = 720

ground_width = 2*screen_width
ground_height = 2*screen_height

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('imagens/fundo.png')
background = pygame.transform.scale(background,(screen_width,screen_height))

ground_group = pygame.sprite.Group()
for i in range (2):
    Ground = ground(ground_width * i, ground_width, ground_height,screen_height)
    ground_group.add(Ground)
clock = pygame.time.Clock()
gameover = False
while not gameover:
    clock.tick(30)

    for event in pygame.event.get(): 
     if event.type == QUIT:
        gameover = True

    screen.blit(background,(0,0))
    ground_group.update()
    ground_group.draw(screen)
    pygame.display.update()