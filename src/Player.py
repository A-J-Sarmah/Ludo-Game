import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,color,image,x_position,y_position,is_on_game,number):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x_position,y_position))
        self.color = color
        self.is_on_game = is_on_game
        self.number = number
