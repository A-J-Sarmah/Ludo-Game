import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,image,block_width,block_height):
        super().__init__()
        self.image = image
        self.image = self.image.get_rect(topleft=(block_width,block_height))
