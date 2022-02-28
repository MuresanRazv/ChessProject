import pygame
from Utils import draw


class Pieces(pygame.sprite.Sprite):
    def __init__(self, group, dim, type_of_piece):
        self.groups = group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.type_of_piece = type_of_piece
        self.__dim = dim
        self.image = pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/" +
                                       type_of_piece).convert_alpha()
        self.rect = pygame.Rect(dim)





