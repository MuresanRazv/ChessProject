import pygame, os


def get_png():
    white_pieces_png = [filename for filename in os.listdir('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces')
                        if filename.endswith("lt60.png")]
    white_pieces = []
    for piece in white_pieces_png:
        white_pieces.append(pygame.image.load('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())

    black_pieces_png = [filename for filename in os.listdir('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces')
                        if filename.endswith("dt60.png")]
    black_pieces = []
    for piece in black_pieces_png:
        black_pieces.append(pygame.image.load('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())

    return white_pieces, black_pieces
