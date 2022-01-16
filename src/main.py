import pygame 
from sys import exit

pygame.init() #initialize pygame

# creating the window
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo")

#clock and FPS
clock = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
