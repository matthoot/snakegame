import pygame
import copy

# 1 = light green, 2 = dark green, 3 = wall, 4 = light green with apple, 5 = dark green with apple

#18 x 16 board, 850x750

board = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],
    [3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
]

WIDTH = 950
HEIGHT = 950
score_padding = HEIGHT - WIDTH
snakeHead_x = 255
snakeHead_y = 505
directions = { "left": 0, "right": 1, "up": 2, "down": 3, "none": 4}
direction = directions["none"]
direction_command = directions["none"]
next_direction = directions["none"]
snakeHead_image = pygame.image.load('assets/snake.png')
snake_speed = 5

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = copy.deepcopy(board)

def drawboard():
    pygame.draw.rect(screen, (72, 118, 47), pygame.Rect(0, 0, 950, 100)) # top bar with score and stuff
    
    for column in range (len(board)):
        for row in range(len(board[column])):
            if board[column][row] == 1:
                pygame.draw.rect(screen, (165, 218, 87), pygame.Rect(50 * row, 100 + (50 * column), 50, 50))    
            elif board[column][row] == 2:
                pygame.draw.rect(screen, (150, 202, 76), pygame.Rect(50 * row, 100 + (50 * column), 50, 50))
            elif board[column][row] == 3:
                pygame.draw.rect(screen, (84, 140, 56), pygame.Rect(50 * row, 100 + (50 * column), 50, 50))

def move_snake(snakeHead_x, snakeHead_y):
    if direction == directions["left"] and valid_turns[directions["left"]]:
        snakeHead_x -= snake_speed
    elif direction == directions["right"] and valid_turns[directions["right"]]:
        snakeHead_x += snake_speed
    elif direction == directions["up"] and valid_turns[directions["up"]]:
        snakeHead_y -= snake_speed
    elif direction == directions["down"] and valid_turns[directions["down"]]:
        snakeHead_y += snake_speed
    
    return snakeHead_x, snakeHead_y    

def check_position(center_x, center_y, next_direction):
    valid_turns = [False, False, False, False]
    centerAdjust = 30
    currentSquare_x = center_x - ((center_x // 50) * 50)
    currentSquare_y = center_y - ((center_y // 50) * 50)
    print(currentSquare_x, currentSquare_y)
    if (center_x - centerAdjust) < 50:
        valid_turns[directions["left"]] = False
    if (center_x + centerAdjust) > 900:
        valid_turns[directions["right"]] = False
    if (center_y + centerAdjust) < 210:
        valid_turns[directions["up"]] = False
    if (center_y - centerAdjust) > 840:
        valid_turns[directions["down"]] = False

    if direction == directions["right"] or direction == directions["left"]:
        if 16 <= currentSquare_x <= 34:
            if next_direction != directions["none"]:
                next_direction = directions["none"]
            else:
                valid_turns[directions["up"]] = True
                valid_turns[directions["down"]] = True
        else:
            valid_turns[directions["up"]] = False
            valid_turns[directions["down"]] = False
  
    if direction == directions["up"] or direction == directions["down"]:
        if 16 <= currentSquare_y <= 34:
            if next_direction != directions["none"]:
                valid_turns[next_direction] = True
                next_direction = directions["none"]                
            else:
                valid_turns[directions["right"]] = True
                valid_turns[directions["left"]] = True
        else:
            valid_turns[directions["right"]] = False
            valid_turns[directions["left"]] = False
    if direction == directions["none"]:
        valid_turns = [True, True, True, True]
    return valid_turns

run = True
while run:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    drawboard()
    center_x = snakeHead_x + 20
    center_y = snakeHead_y + 20
    screen.blit(snakeHead_image, (snakeHead_x, snakeHead_y))
    pygame.draw.circle(screen, 'pink', (center_x, center_y), 2)
    valid_turns = check_position(center_x, center_y, next_direction)
    print(direction, next_direction)
    snakeHead_x, snakeHead_y = move_snake(snakeHead_x, snakeHead_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = directions["right"]
            if event.key == pygame.K_LEFT:
                direction_command = directions["left"]
            if event.key == pygame.K_UP:
                direction_command = directions["up"]
            if event.key == pygame.K_DOWN:
                direction_command = directions["down"]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == directions["right"]:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == directions["left"]:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == directions["up"]:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == directions["down"]:
                direction_command = direction
    
    if direction_command == directions["right"]:
        if valid_turns[directions["right"]]:
            direction = directions["right"]
            next_direction = directions["none"]
        else:
            next_direction = directions["right"]
    if direction_command == directions["left"]:
        if valid_turns[directions["left"]]:
            direction = directions["left"]
            next_direction = directions["none"]
        else:
            next_direction = directions["left"]
    if direction_command == directions["up"]:
        if valid_turns[directions["up"]]:
            direction = directions["up"]
            next_direction = directions["none"]
        else:
            next_direction = directions["left"]
    if direction_command == directions["down"]:
        if valid_turns[directions["down"]]:
            direction = directions["down"]
            next_direction = directions["none"]
        else: next_direction = directions["down"]
              
    pygame.display.flip()
