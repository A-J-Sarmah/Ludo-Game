import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,image,block_pos_x,block_pos_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(block_pos_x,block_pos_y))
