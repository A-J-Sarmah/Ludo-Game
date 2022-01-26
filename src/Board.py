import pygame
from utils import initial_positions 

class Board(pygame.sprite.Sprite):
    def __init__(self,color,board):
        super().__init__()
        self.image = board
        self.color = color
        if self.color == 'Red':
            self.rect = self.image.get_rect()
        elif self.color == 'Yellow':
            self.rect = self.image.get_rect(bottomright=(547,547))
        elif self.color == 'Green':
            self.rect = self.image.get_rect(topright=(547,0))
        elif self.color == 'Blue':
            self.rect = self.image.get_rect(bottomleft=(0,547))
        else:
            self.rect = self.image.get_rect(topright=(327,215))

    # Generate the initial starting positions for game positions
    def initial_index_per_color(self):
        initial_positions_color = initial_positions()
        for key in initial_positions_color:
            current_list = initial_positions_color[key]
            if self.color == "Red" or self.color == "Green":
                for i in range(len(current_list)):
                    if i == 0: current_list[i] += self.rect.x
            elif self.color == "Yellow":
                for i in range(len(current_list)):
                    current_list[i] += self.rect.x
            elif self.color == "Blue":
                for i in range(len(current_list)):
                    if i == 1: current_list[i] += self.rect.y
            else:
                pass
        return initial_positions_color

class Status_Board(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(0,547))
