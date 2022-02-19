import pygame
pygame.font.init()
BLACK = 0, 0, 0
WHITE = 255, 255, 255
FONT = pygame.font.Font('freesansbold.ttf', 16)


def convert_letter(letter):
    return FONT.render(str(letter), True, BLACK)


LETTERS = [convert_letter("a"), convert_letter("b"), convert_letter("c"), convert_letter("d"), convert_letter("e"),
           convert_letter("f"), convert_letter("g"), convert_letter("h")]
NUMBERS = [convert_letter("1"),  convert_letter("2"), convert_letter("3"), convert_letter("4"), convert_letter("5"),
           convert_letter("6"), convert_letter("7"), convert_letter("8")]


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
                pygame.draw.rect(screen, BLACK, rect, 0)
            counter += 1
        counter += 1