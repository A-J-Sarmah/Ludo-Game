import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self,color,board):
        super().__init__()
        self.image = board
        if color == 'Red':
            self.rect = self.image.get_rect()
        elif color == 'Yellow':
            self.rect = self.image.get_rect(bottomright=(600,600))
        elif color == 'Green':
            self.rect = self.image.get_rect(topright=(600,0))
        else:
            self.rect = self.image.get_rect(bottomleft=(0,600))
