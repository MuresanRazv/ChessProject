import sys, pygame
from Utils import draw
pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRAY = 255 // 2, 255 // 2, 255 // 2
SIZE = (WIDTH, HEIGHT) = (680, 680)
screen = pygame.display.set_mode(SIZE)
running = True


while running:
    screen.fill(GRAY)
    draw.draw_table(SIZE, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
