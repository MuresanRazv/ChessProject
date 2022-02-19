import sys, pygame, os
from Utils import draw, extract_png

pygame.init()
SIZE = (WIDTH, HEIGHT) = (680, 680)
screen = pygame.display.set_mode(SIZE)
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRAY = 255 // 2, 255 // 2, 255 // 2
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

PIECES = WHITES, BLACKS = extract_png.get_png()
WHITES_RECT, BLACKS_RECT = [], []
for white, black in zip(WHITES, BLACKS):
    WHITES_RECT.append(white.get_rect())
    BLACKS_RECT.append(black.get_rect())
WHITES_RECT[0] = INITIAL_POSITIONS_WHITE["b1"]

running = True


while running:
    screen.fill(GRAY)
    draw.draw_table(SIZE, screen)
    screen.blit(WHITES[0], WHITES_RECT[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
