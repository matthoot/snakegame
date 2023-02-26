import pygame
import copy

# 1 = light green, 2 = dark green, 3 = light green with apple, 4 = dark green with apple

board = [
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
]

WIDTH = 950
HEIGHT = 950
score_padding = HEIGHT - WIDTH

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = copy.deepcopy(board)

def drawboard():
    pygame.draw.rect(screen, (72, 118, 47), pygame.Rect(0, 0, 950, 100)) # top bar with score and stuff
    
    # pygame.draw.rect(screen, (165, 218, 87), pygame.Rect(50, 150, 50, 50))
    for column in range (len(board)):
        for row in range(len(board[column])):
            if board[column][row] == 1:
                pygame.draw.rect(screen, (165, 218, 87), pygame.Rect(50 + (50 * row), 150 + (50 * column), 50, 50))    
            elif board[column][row] == 2:
                pygame.draw.rect(screen, (150, 202, 76), pygame.Rect(50 + (50 * row), 150 + (50 * column), 50, 50))
run = True
while run:
    timer.tick(fps)
    screen.fill((84, 140, 56))
    # pygame.draw.rect(screen, 'white', pygame.Rect(30, 30, 30, 30))
    drawboard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
