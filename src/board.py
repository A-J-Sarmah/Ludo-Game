import pygame
from utils import initial_positions 

class Board(pygame.sprite.Sprite):
    def __init__(self,color,board):
        super().__init__()
        self.image = board
        if color == 'Red':
            self.rect = self.image.get_rect()
        elif color == 'Yellow':
            self.rect = self.image.get_rect(bottomright=(547,547))
        elif color == 'Green':
            self.rect = self.image.get_rect(topright=(547,0))
        elif color == 'Blue':
            self.rect = self.image.get_rect(bottomleft=(0,547))
        else:
            self.rect = self.image.get_rect(topright=(327,215))

    # Generate the initial starting positions for game positions
    def initial_index_per_color(self):
        initial_positions_color = initial_positions()
        for key in initial_positions_color:
            current_list = initial_positions_color[key]
            for i in range(len(current_list)):
                if i == 0: current_list[i] += self.rect.midleft[0]
                else: current_list[i] += self.rect.midleft[0]
        return initial_positions_color

class Status_Board(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(0,547))
