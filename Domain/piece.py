import pygame


class Pieces(pygame.sprite.Sprite):
    def __init__(self, group, pos, type_of_piece):
        super().__init__()
        self.type_of_piece = type_of_piece
        self.__pos = pos
        self.image = pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/" +
                                       type_of_piece).convert_alpha()
        self.rect = pygame.Rect(pos)

    def move_piece(self, new_pos):
        self.__pos = new_pos
        self.rect = pygame.Rect(new_pos)

    def collides(self, pos):
        return self.__pos[0] == pos[0] + 10 and self.__pos[1] == pos[1] + 10




