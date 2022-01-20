import pygame 
from sys import exit
from board import Board
from block import Block
from utils import create_board_block

pygame.init() #initialize pygame

# creating the window
WIDTH = 547
HEIGHT = 547
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo")

#game imports
red_board = pygame.image.load('../assets/red_board.png').convert_alpha()
yellow_board = pygame.image.load('../assets/yellow_board.png').convert_alpha()
green_board = pygame.image.load('../assets/green_board.png').convert_alpha()
blue_board = pygame.image.load('../assets/blue_board.png').convert_alpha()
center_board = pygame.image.load('../assets/center_board.png').convert_alpha()
block_image = pygame.image.load('../assets/game_block.png').convert_alpha()
block_image_red = pygame.image.load('../assets/game_block_red.png').convert_alpha()
block_image_yellow = pygame.image.load('../assets/game_block_yellow.png').convert_alpha()
block_image_green = pygame.image.load('../assets/game_block_green.png').convert_alpha()
block_image_blue = pygame.image.load('../assets/game_block_blue.png').convert_alpha()

# creating board
board = pygame.sprite.Group()
board.add(Board('Red',red_board))
board.add(Board('Green',green_board))
board.add(Board('Blue',blue_board))
board.add(Board('Yellow',yellow_board))
board.add(Board('Center',center_board))

block = pygame.sprite.Group()

#rendering block on board
def render_blocks(is_special,color,position_x,position_y):
    if is_special:
        if color == "red":
            block.add(Block(block_image_red,position_x,position_y))
        elif color == "yellow":
            block.add(Block(block_image_yellow,position_x,position_y))
        elif color == "blue":
            block.add(Block(block_image_blue,position_x,position_y))
        elif color == "green":
            block.add(Block(block_image_green,position_x,position_y))
        else:
            pass
    else:
        block.add(Block(block_image,position_x,position_y))

#clock and FPS
clock = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('White')
    #Drawing board and block
    board.draw(screen) 
    create_board_block("horizontal","red",0,214,render_blocks)
    create_board_block("horizontal","yellow",325,214,render_blocks)
    create_board_block("vertical","green",217,0,render_blocks)
    create_board_block("vertical","blue",217,325,render_blocks)
    block.draw(screen)
    pygame.display.update()
    clock.tick(60)
