import pygame, os

INITIAL_POSITIONS_WHITE = {"b1": ((80 - 30) + 80 * 2, 10, 60, 60), "b2": ((80 - 30) + 80 * 5, 10, 60, 60),
                           "k": ((80 - 30) + 80 * 4, 10, 60, 60), "q": ((80 - 30) + 80 * 3, 10, 60, 60),
                           "n1": ((80 - 30) + 80, 10, 60, 60), "n2": ((80 - 30) + 80 * 6, 10, 60, 60),
                           "r1": ((80 - 30), 10, 60, 60), "r2": ((80 - 30) + 80 * 7, 10, 60, 60),
                           "p1": ((80 - 30), 10 + 80, 60, 60), "p2": ((80 - 30) + 80, 10 + 80, 60, 60),
                           "p3": ((80 - 30) + 80 * 2, 10 + 80, 60, 60), "p4": ((80 - 30) + 80 * 3, 10 + 80, 60, 60),
                           "p5": ((80 - 30) + 80 * 4, 10 + 80, 60, 60), "p6": ((80 - 30) + 80 * 5, 10 + 80, 60, 60),
                           "p7": ((80 - 30) + 80 * 6, 10 + 80, 60, 60), "p8": ((80 - 30) + 80 * 7, 10 + 80, 60, 60)}

INITIAL_POSITIONS_BLACK = {"b1": ((80 - 30)+ 80 * 2, 640 - 70, 60, 60), "b2": ((80 - 30) + 80 * 5, 640 - 70, 60, 60),
                           "k": ((80 - 30) + 80 * 4, 640 - 70, 60, 60), "q": ((80 - 30) + 80 * 3, 640 - 70, 60, 60),
                           "n1": ((80 - 30) + 80, 640 - 70, 60, 60), "n2": ((80 - 30) + 80 * 6, 640 - 70, 60, 60),
                           "r1": ((80 - 30), 640 - 70, 60, 60), "r2": ((80 - 30) + 80 * 7, 640 - 70, 60, 60),
                           "p1": ((80 - 30), 640 - 150, 60, 60), "p2": ((80 - 30) + 80, 640 - 150, 60, 60),
                           "p3": ((80 - 30) + 80 * 2, 640 - 150, 60, 60), "p4": ((80 - 30) + 80 * 3, 640 - 150, 60, 60),
                           "p5": ((80 - 30) + 80 * 4, 640 - 150, 60, 60), "p6": ((80 - 30) + 80 * 5, 640 - 150, 60, 60),
                           "p7": ((80 - 30) + 80 * 6, 640 - 150, 60, 60), "p8": ((80 - 30) + 80 * 7, 640 - 150, 60, 60)}


def get_png():
    white_pieces_png = [filename for filename in os.listdir('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces')
                        if filename.endswith("lt60.png")]
    white_pieces = []
    for piece in white_pieces_png:
        if piece.endswith("plt60.png"):
            for i in range(8):
                white_pieces.append(
                    pygame.image.load(
                        'C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())
        if not piece.endswith("qlt60.png") or piece.endswith("klt60.png") or piece.endswith("plt60.png"):
            white_pieces.append(
                pygame.image.load('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())
        white_pieces.append(pygame.image.load('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())

    black_pieces_png = [filename for filename in os.listdir('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces')
                        if filename.endswith("dt60.png")]
    black_pieces = []
    for piece in black_pieces_png:
        print(piece)
        if piece.endswith("pdt60.png"):
            for i in range(8):
                black_pieces.append(
                    pygame.image.load(
                        'C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())
        if not piece.endswith("qdt60.png") or piece.endswith("kdt60.png") or not piece.endswith("pdt60.png"):
            black_pieces.append(
                pygame.image.load('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())
        black_pieces.append(pygame.image.load('C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/' + piece).convert_alpha())

    return zip(white_pieces, INITIAL_POSITIONS_WHITE.values()), zip(black_pieces, INITIAL_POSITIONS_BLACK.values())
