import pygame
pygame.font.init()
BROWN = 125, 92, 52
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 70, 235, 52
FONT = pygame.font.Font('freesansbold.ttf', 16)


def convert_letter(letter):
    return FONT.render(str(letter), True, BLACK)


LETTERS = [convert_letter("a"), convert_letter("b"), convert_letter("c"), convert_letter("d"), convert_letter("e"),
           convert_letter("f"), convert_letter("g"), convert_letter("h")]
NUMBERS = [convert_letter("1"),  convert_letter("2"), convert_letter("3"), convert_letter("4"), convert_letter("5"),
           convert_letter("6"), convert_letter("7"), convert_letter("8")]


"""
Function to draw the chess table
"""


def draw_table(size, screen):
    square_size = 80
    counter = 1

    for width, letter in zip(range(80, size[0], 80), LETTERS):
        screen.blit(letter, (width, 660))

    for height, number in zip(range(40, size[1] - 40, 80), NUMBERS):
        screen.blit(number, (10, height))

    for x in range(40, size[0], square_size):
        for y in range(0, size[1] - 40, square_size):
            rect = pygame.Rect(x, y, square_size, square_size)
            if counter % 2 != 0:
                pygame.draw.rect(screen, WHITE, rect, 0)
            else:
                pygame.draw.rect(screen, BROWN, rect, 0)
            counter += 1
        counter += 1


"""
Function to find coordinates of the square in which the user clicked in or a piece is
"""


def find_square(click_pos):
    x_limit = 40
    y_limit = 640
    start_x = 40
    start_y = 0
    if click_pos[0] < x_limit or click_pos[1] > y_limit:
        return False
    while start_x <= click_pos[0]:
        start_x += 80

    square_x = start_x - 80

    while start_y <= click_pos[1]:
        start_y += 80

    square_y = start_y - 80

    return square_x, square_y


"""
Function to highlight the square in which the player clicked
"""


def highlight_square(screen, square_size, pos):
    square_pos = find_square(pos)
    if square_pos:
        rect = pygame.Rect(square_pos[0], square_pos[1], square_size, square_size)
        pygame.draw.rect(screen, GREEN, rect, 3)



def check_collision(pos, all_sprites):
    for p in all_sprites.sprites():
        if pos[0] == p.rect.left and pos[1] == p.rect.top:
            return True
    return False


"""
Function to draw all possible movements for a piece
"""


def draw_all_possible(piece, all_sprites, screen):
    current_x, current_y = piece.rect.left, piece.rect.top
    if piece.get_type() == "blt60.png":
        while current_x < 680 and not check_collision((current_x, current_y), all_sprites) and current_y < 680:
            current_x += 80
            current_y += 80
            highlight_square(screen, 80, (current_x, current_y))

        while current_x > 80 and not check_collision((current_x, current_y), all_sprites) and current_y < 680:
            current_x -= 80
            current_y += 80
            highlight_square(screen, 80, (current_x, current_y))

    if piece.get_type() == "bdt60.png":
        while current_x < 680 and not check_collision((current_x, current_y), all_sprites) and current_y > 0:
            current_x += 80
            current_y -= 80
            highlight_square(screen, 80, (current_x, current_y))

        while current_x > 80 and not check_collision((current_x, current_y), all_sprites) and current_y > 0:
            current_x -= 80
            current_y -= 80
            highlight_square(screen, 80, (current_x, current_y))

    if piece.get_type() == "plt60.png":
        if not check_collision((current_x, current_y + 80), all_sprites):
            highlight_square(screen, 80, (current_x, current_y + 80))