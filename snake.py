import pygame
import copy

# 1 = light green, 2 = dark green, 3 = light green with apple, 4 = dark green with apple

board = [
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
]

WIDTH = 900
HEIGHT = 950
score_padding = HEIGHT - WIDTH

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = copy.deepcopy(board)
pygame.draw.rect(screen, 'white', pygame.Rect(30, 30, 60, 60))

def drawboard():
    squareHeight = ((HEIGHT - score_padding) // 32)
    squareWidth = WIDTH // 30
    # for column in range (len(board)):
    #     for row in range(column[row]):
    #         if column[row] == 1:
    #

run = True
while run:
    timer.tick(fps)
    screen.fill('green')
    pygame.draw.rect(screen, 'white', pygame.Rect(30, 30, 60, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
