import pygame
import copy
import random

pygame.init()
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
last_direction = directions["none"]
snakeHead_image = pygame.image.load('assets/snake.png')
orange_image = pygame.image.load('assets/orange.png')
snake_speed = 5
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',20)
fps = 60
level = copy.deepcopy(board)
rows = 15
cols = 17
row_index = random.randint(0, rows-1)
col_index = random.randint(0, cols-1)
orange_x = 58 + (50 * col_index)
orange_y = 158 + (50 * row_index)
center_snake_x = snakeHead_x + 20
center_snake_y = snakeHead_y + 20
center_orange_x = orange_x + 16
center_orange_y = orange_y + 16
screen.blit(snakeHead_image, (snakeHead_x, snakeHead_y))
snake_collision_box = pygame.draw.circle(screen, 'red', (center_snake_x, center_snake_y), 20, 2)
orange_collision_box = pygame.draw.circle(screen, 'red', (center_orange_x, center_orange_y), 16, 2)
score = 0

orange_collision = False

class Segment:
    def __init__(self, x, y):
        self.x_position = x
        self.y_position = y
        self.next_segment = None
        
    def move(self, dx, dy):
        self.x_position += dx
        self.y_position += dy
            
class Snake:
    def __init__(self, x, y):
        self.head = Segment(x, y)
        self.length = 1
        self.tail = self.head
        self.direction = None
    
    def moveSegments(self, dx, dy):
        current_segment = self.tail
        while current_segment != self.head:
            current_segment.x = current_segment.next_segment.x
            current_segment.y = current_segment.next_segment.y
            current_segment = current_segment.next_segment
        self.head.move(dx, dy)
    
    def draw(self, screen):
        segment = self.head
        while segment is not None:
            screen.blit(segment.surface, segment.rect)
            segment = segment.next_segment
            
    def set_direction(self, direction):
        self.direction = direction
        
    def move(self):
        if self.direction is None:
            return

class Orange:
    def __init__(self, x, y):    
        self.x = x
        self.y = y

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

def move_snake(direction, snakeHead_x, snakeHead_y):
    if not valid_turns[direction]:
        direction = last_direction
    if direction == directions["left"] and valid_turns[directions["left"]]:
        snakeHead_x -= snake_speed
    elif direction == directions["right"] and valid_turns[directions["right"]]:
        snakeHead_x += snake_speed
    elif direction == directions["up"] and valid_turns[directions["up"]]:
        snakeHead_y -= snake_speed
    elif direction == directions["down"] and valid_turns[directions["down"]]:
        snakeHead_y += snake_speed
    return direction, snakeHead_x, snakeHead_y    

def check_position(center_x, center_y):
    valid_turns = [False, False, False, False, False]  
    centerAdjust = 30
    currentSquare_x = center_x - ((center_x // 50) * 50)
    currentSquare_y = center_y - ((center_y // 50) * 50)
    if direction == directions["none"] and direction_command == directions["none"]:
        return [True, True, True, True, False]
    
    if 20 <= currentSquare_x <= 30:
        valid_turns[directions["up"]] = True
        valid_turns[directions["down"]] = True
    else:
        valid_turns[directions["up"]] = False
        valid_turns[directions["down"]] = False
            
    if 20 <= currentSquare_y <= 30:
        valid_turns[directions["right"]] = True
        valid_turns[directions["left"]] = True
    else:
        valid_turns[directions["right"]] = False
        valid_turns[directions["left"]] = False
    
    if (center_x - centerAdjust) < 50:
        valid_turns[directions["left"]] = False
    if (center_x + centerAdjust) > 900:
        valid_turns[directions["right"]] = False
    if (center_y + centerAdjust) < 210:
        valid_turns[directions["up"]] = False
    if (center_y - centerAdjust) > 840:
        valid_turns[directions["down"]] = False
        
    return valid_turns   

def draw_misc():
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (10, 10))

run = True
while run:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    drawboard()
    draw_misc()
    if snake_collision_box.colliderect(orange_collision_box):
        row_index = random.randint(0, rows-1)
        col_index = random.randint(0, cols-1)
        orange_x = 58 + (50 * col_index)
        orange_y = 158 + (50 * row_index)
        score += 1
    center_snake_x = snakeHead_x + 20
    center_snake_y = snakeHead_y + 20
    center_orange_x = orange_x + 16
    center_orange_y = orange_y + 16
    snake_collision_box = pygame.draw.circle(screen, 'black', (center_snake_x, center_snake_y), 20, 2)
    orange_collision_box = pygame.draw.circle(screen, 'black', (center_orange_x, center_orange_y), 15, 2)
    screen.blit(orange_image, (orange_x, orange_y))
    screen.blit(snakeHead_image, (snakeHead_x, snakeHead_y))
    valid_turns = check_position(center_snake_x, center_snake_y)
    direction, snakeHead_x, snakeHead_y = move_snake(direction, snakeHead_x, snakeHead_y)
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
    
    last_direction = direction
    if direction_command == directions["right"] and valid_turns[directions["right"]]:
        direction = directions["right"]
    if direction_command == directions["left"] and valid_turns[directions["left"]]:
        direction = directions["left"]
    if direction_command == directions["up"] and valid_turns[directions["up"]]:
        direction = directions["up"]
    if direction_command == directions["down"] and valid_turns[directions["down"]]:
        direction = directions["down"]  
        
    pygame.display.flip()
    
pygame.quit()