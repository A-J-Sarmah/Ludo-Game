import pygame

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

class Status_Board(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(0,547))
