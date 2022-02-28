import sys, pygame, os
from Utils import draw, extract_png, check_movements
from Domain import piece

pygame.init()

"""
CONSTANTS
"""

SIZE = (WIDTH, HEIGHT) = (680, 680)
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRAY = 255 // 2, 255 // 2, 255 // 2
PIECES_PNG = WHITE_PIECES_PNG, BLACK_PIECES_PNG = extract_png.get_png()

"""
SPRITES AND SCREEN INITIALIZATION
"""

white_pieces = []
black_pieces = []
piece_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode(SIZE)


for whites in WHITE_PIECES_PNG:
    new_piece = piece.Pieces(piece_sprites, whites[1], whites[0])
    white_pieces.append(new_piece)
    piece_sprites.add(new_piece)

for blacks in BLACK_PIECES_PNG:
    new_piece = piece.Pieces(piece_sprites, blacks[1], blacks[0])
    black_pieces.append(new_piece)
    piece_sprites.add(new_piece)

all_pieces = white_pieces + black_pieces

"""
MAIN LOOP
"""
running = True

while running:

    screen.fill(GRAY)
    draw.draw_table(SIZE, screen)
    piece_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece_sprite, piece in zip(piece_sprites.sprites(), all_pieces):
                if piece_sprite.rect.collidepoint(event.pos):
                    x, y = draw.find_square(event.pos)
                    possible_movements = check_movements.check_possible_movements(piece.type_of_piece,
                                                                                  (x, y), piece_sprites)
                    print(possible_movements)

        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
