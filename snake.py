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

snakeHead_x = 255
snakeHead_y = 505
directions = { "left": 0, "right": 1, "up": 2, "down": 3 }
direction = 0
snakeHead_image = pygame.image.load('assets/snake.png')
snake_speed = 3

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = copy.deepcopy(board)

def drawboard():
    pygame.draw.rect(screen, (72, 118, 47), pygame.Rect(0, 0, 950, 100)) # top bar with score and stuff
    
    for column in range (len(board)):
        for row in range(len(board[column])):
            if board[column][row] == 1:
                pygame.draw.rect(screen, (165, 218, 87), pygame.Rect(50 + (50 * row), 150 + (50 * column), 50, 50))    
            elif board[column][row] == 2:
                pygame.draw.rect(screen, (150, 202, 76), pygame.Rect(50 + (50 * row), 150 + (50 * column), 50, 50))

def move_snake(snakeHead_x, snakeHead_y):
    if direction == directions["left"]:
        snakeHead_x -= snake_speed
    elif direction == directions["right"]:
        snakeHead_x += snake_speed
    elif direction == directions["down"]:
        snakeHead_y += snake_speed
    elif direction == directions["up"]:
        snakeHead_y -= snake_speed
    return snakeHead_x, snakeHead_y    

run = True
while run:
    timer.tick(fps)
    screen.fill((84, 140, 56))
    drawboard()
    screen.blit(snakeHead_image, (snakeHead_x, snakeHead_y))
    snakeHead_x, snakeHead_y = move_snake(snakeHead_x, snakeHead_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = directions["right"]
            if event.key == pygame.K_LEFT:
                direction = directions["left"]
            if event.key == pygame.K_UP:
                direction = directions["up"]
            if event.key == pygame.K_DOWN:
                direction = directions["down"]
    
    pygame.display.flip()
