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
        ["plt60.png"] * 8 +
        ["blt60.png"] * 2 +
        ["nlt60.png"] * 2 +
        ["rlt60.png"] * 2 +
        ["qlt60.png"] +
        ["klt60.png"]
    )

    B_PIECES = []
    B_PIECES.extend(
        ["pdt60.png"] * 8 +
        ["bdt60.png"] * 2 +
        ["ndt60.png"] * 2 +
        ["rdt60.png"] * 2 +
        ["qdt60.png"] +
        ["kdt60.png"]
    )

    return zip(W_PIECES, INITIAL_POSITIONS_WHITE.values()), zip(B_PIECES, INITIAL_POSITIONS_BLACK.values())
