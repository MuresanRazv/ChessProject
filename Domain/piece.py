import pygame


def find_piece_by_pos(pos, pieces):
    """
    Function to find a piece by a given position
    """
    for p in pieces:
        if p.collides(pos):
            return p


class Piece(pygame.sprite.Sprite):
    """
    Class for Chess pieces
    """
    def __init__(self, group, pos, type_of_piece):
        super().__init__()
        self.type_of_piece = type_of_piece
        self.__pos = pos
        self.image = pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/" +
                                       type_of_piece).convert_alpha()
        self.rect = pygame.Rect(pos)

    """
    Getter for coordinates
    """
    def get_pos(self):
        return self.__pos[0], self.__pos[1]

    """
    Function to move piece to a new position
    """
    def move_piece(self, new_pos):
        self.__pos = new_pos
        self.rect = pygame.Rect(new_pos)

    """
    Function to check if a piece collides with given position
    """
    def collides(self, pos):
        if type(pos) == bool:
            return False
        return self.__pos[0] == pos[0] + 10 and self.__pos[1] == pos[1] + 10
