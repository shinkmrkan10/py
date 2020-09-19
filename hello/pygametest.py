# pygame.display.update()
import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("This is pygame sample")
while(True):
    screen.fill((0,0,0,))
    pygame.draw.rect(screen, (255,255,0), Rect(10,10,20,50))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()