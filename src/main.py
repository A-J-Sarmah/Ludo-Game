import pygame 
from sys import exit
from board import Board

pygame.init() #initialize pygame

# creating the window
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo")

#game imports
red_board = pygame.image.load('../assets/red_board.png').convert_alpha()
yellow_board = pygame.image.load('../assets/yellow_board.png').convert_alpha()
green_board = pygame.image.load('../assets/green_board.png').convert_alpha()
blue_board = pygame.image.load('../assets/blue_board.png').convert_alpha()

# creating board
board = pygame.sprite.Group()
board.add(Board('Red',red_board))
board.add(Board('Green',green_board))
board.add(Board('Blue',blue_board))
board.add(Board('Yellow',yellow_board))

#clock and FPS
clock = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('White')
    board.draw(screen)  
    pygame.display.update()
    clock.tick(60)
