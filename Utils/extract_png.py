import pygame, os

INITIAL_POSITIONS_WHITE = {"p1": ((80 - 30), 10 + 80, 80, 80), "p2": ((80 - 30) + 80, 10 + 80, 80, 80),
                           "p3": ((80 - 30) + 80 * 2, 10 + 80, 80, 80), "p4": ((80 - 30) + 80 * 3, 10 + 80, 80, 80),
                           "p5": ((80 - 30) + 80 * 4, 10 + 80, 80, 80), "p6": ((80 - 30) + 80 * 5, 10 + 80, 80, 80),
                           "p7": ((80 - 30) + 80 * 6, 10 + 80, 80, 80), "p8": ((80 - 30) + 80 * 7, 10 + 80, 80, 80),
                           "b1": ((80 - 30) + 80 * 2, 10, 80, 80), "b2": ((80 - 30) + 80 * 5, 10, 80, 80),
                           "n1": ((80 - 30) + 80, 10, 80, 80), "n2": ((80 - 30) + 80 * 6, 10, 80, 80),
                           "r1": ((80 - 30), 10, 80, 80), "r2": ((80 - 30) + 80 * 7, 10, 80, 80),
                           "q": ((80 - 30) + 80 * 3, 10, 80, 80), "k": ((80 - 30) + 80 * 4, 10, 80, 80)
                           }

INITIAL_POSITIONS_BLACK = {"p1": ((80 - 30), 640 - 150, 80, 80), "p2": ((80 - 30) + 80, 640 - 150, 80, 80),
                           "p3": ((80 - 30) + 80 * 2, 640 - 150, 80, 80), "p4": ((80 - 30) + 80 * 3, 640 - 150, 80, 80),
                           "p5": ((80 - 30) + 80 * 4, 640 - 150, 80, 80), "p6": ((80 - 30) + 80 * 5, 640 - 150, 80, 80),
                           "p7": ((80 - 30) + 80 * 6, 640 - 150, 80, 80), "p8": ((80 - 30) + 80 * 7, 640 - 150, 80, 80),
                           "b1": ((80 - 30) + 80 * 2, 640 - 70, 80, 80), "b2": ((80 - 30) + 80 * 5, 640 - 70, 80, 80),
                           "n1": ((80 - 30) + 80, 640 - 70, 80, 80), "n2": ((80 - 30) + 80 * 6, 640 - 70, 80, 80),
                           "r1": ((80 - 30), 640 - 70, 80, 80), "r2": ((80 - 30) + 80 * 7, 640 - 70, 80, 80),
                           "k": ((80 - 30) + 80 * 4, 640 - 70, 80, 80), "q": ((80 - 30) + 80 * 3, 640 - 70, 80, 80)
                          }


def get_png():
    W_PIECES = []
    W_PIECES.extend(
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/plt60.png").convert_alpha()] * 8 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/blt60.png").convert_alpha()] * 2 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/nlt60.png").convert_alpha()] * 2 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/rlt60.png").convert_alpha()] * 2 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/qlt60.png").convert_alpha()] +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/klt60.png").convert_alpha()]
    )

    B_PIECES = []
    B_PIECES.extend(
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/pdt60.png").convert_alpha()] * 8 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/bdt60.png").convert_alpha()] * 2 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/ndt60.png").convert_alpha()] * 2 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/rdt60.png").convert_alpha()] * 2 +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/qdt60.png").convert_alpha()] +
        [pygame.image.load("C:/Users/seNNNz0rel/Documents/ChessProject/Chess_Pieces/kdt60.png").convert_alpha()]
    )
    print(W_PIECES[0])

    return zip(W_PIECES, INITIAL_POSITIONS_WHITE.values()), zip(B_PIECES, INITIAL_POSITIONS_BLACK.values())
