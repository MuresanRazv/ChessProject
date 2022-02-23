import sys, pygame, os
from Utils import draw, extract_png

pygame.init()
SIZE = (WIDTH, HEIGHT) = (680, 680)
screen = pygame.display.set_mode(SIZE)
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRAY = 255 // 2, 255 // 2, 255 // 2

PIECES = WHITE_PIECES, BLACK_PIECES = extract_png.get_png()

WHITES = []
for whites in WHITE_PIECES:
    WHITES.append((whites[0], whites[1]))
BLACKS = []
for blacks in BLACK_PIECES:
    BLACKS.append((blacks[0], blacks[1]))

running = True
current_click_pos = [0, 0]

while running:

    screen.fill(GRAY)
    draw.draw_table(SIZE, screen)
    draw.highlight_square(screen, 80, current_click_pos)
    for w_piece, b_piece in zip(WHITES, BLACKS):
        screen.blit(w_piece[0], w_piece[1])
        screen.blit(b_piece[0], b_piece[1])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_click_pos[0], current_click_pos[1] = event.pos
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
