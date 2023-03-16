
import pygame
import copy
import random

pygame.init()
# 1 = light green, 2 = dark green, 3 = wall, 4 = light green with apple, 5 = dark green with apple
#18 x 16 board, 850x750

direction_command = "none"
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

class Orange:
    def __init__(self):    
        self.image = pygame.image.load('assets/orange.png')
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def randomize(self):
        self.row_index = random.randint(0, rows-1)
        self.col_index = random.randint(0, cols-1)
        self.rect.x = 58 + (50 * self.col_index)
        self.rect.y = 158 + (50 * self.row_index)

class Segment:
    def __init__(self, x, y):
        self.next_segment = None
        self.image = pygame.image.load('assets/snake2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center_x = x + 20
        self.center_y = y + 20
        self.canGoLeft = False
        self.canGoRight = False
        self.canGoUp = False
        self.canGoDown = False
        self.direction = "none"
        self.last_direction = "none"
        
    def move(self):
        if self.direction == "left" and self.canGoLeft:
            self.rect.x -= snake_speed
            self.center_x -= snake_speed
        elif self.direction == "right" and self.canGoRight:
            self.rect.x += snake_speed
            self.center_x += snake_speed
        elif self.direction == "up" and self.canGoUp:
            self.rect.y -= snake_speed
            self.center_y -= snake_speed
        elif self.direction == "down" and self.canGoDown:
            self.rect.y += snake_speed
            self.center_y += snake_speed
        else:
            self.direction = self.last_direction
    
    def check_direction(self):
        centerAdjust = 30
        currentSquare_x = self.center_x - ((self.center_x // 50) * 50)
        currentSquare_y = self.center_y - ((self.center_y // 50) * 50)
        if self.direction == "none" and direction_command == "none":
            self.canGoLeft, self.canGoRight, self.canGoUp, self.canGoDown = True, True, True, True
        
        if 20 <= currentSquare_x <= 30:
            self.canGoUp = True
            self.canGoDown = True
        else:
            self.canGoUp = False
            self.canGoDown = False
                
        if 20 <= currentSquare_y <= 30:
            self.canGoRight = True
            self.canGoLeft = True
        else:
            self.canGoRight = False
            self.canGoLeft = False
        
        if (self.center_x - centerAdjust) < 50:
            self.canGoLeft = False
        if (self.center_x + centerAdjust) > 900:
            self.canGoRight = False
        if (self.center_y + centerAdjust) < 210:
            self.canGoUp = False
        if (self.center_y - centerAdjust) > 840:
            self.canGoDown = False
            
class Snake:
    def __init__(self, x, y):
        self.head = Segment(x, y)
        self.length = 1
        self.tail = self.head
        # self.direction = "none"
        # self.last_direction = "none"
        # self.canGoLeft = False
        # self.canGoRight = False
        # self.canGoUp = False
        # self.canGoDown = False
    
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
            screen.blit(segment.image, segment.rect)
            segment = segment.next_segment
            
    def set_direction(self, direction):
        self.direction = direction
        
    def move(self):
        if self.direction is None:
            return

        

WIDTH = 950
HEIGHT = 950
score_padding = HEIGHT - WIDTH
snakeHead_x = 255
snakeHead_y = 505
snake_speed = 5
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',20)
fps = 60
level = copy.deepcopy(board)
rows = 15
cols = 17
center_snake_x = snakeHead_x + 20
center_snake_y = snakeHead_y + 20
orange = Orange()
snake = Snake(255, 505)
score = 0
orange_collision = False

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

def check_position(center_x, center_y):
    left, right, up, down, none = False, False, False, False, False 
    centerAdjust = 30
    currentSquare_x = center_x - ((center_x // 50) * 50)
    currentSquare_y = center_y - ((center_y // 50) * 50)
    if direction == "none" and direction_command == "none":
        left, right, up, down = True, True, True, True
        none = False
        return left, right, up, down, none
    
    if 20 <= currentSquare_x <= 30:
        up = True
        down = True
    else:
        up = False
        down = False
            
    if 20 <= currentSquare_y <= 30:
        right = True
        left = True
    else:
        right = False
        left = False
    
    if (center_x - centerAdjust) < 50:
        left = False
    if (center_x + centerAdjust) > 900:
        right = False
    if (center_y + centerAdjust) < 210:
        up = False
    if (center_y - centerAdjust) > 840:
        down = False
        
    return left, right, up, down, none

def draw_misc():
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (10, 10))

orange.randomize()
run = True
while run:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    drawboard()
    draw_misc()
    orange.draw(screen)
    snake.draw(screen)
    if snake.head.rect.colliderect(orange.rect):
        orange.randomize()
        score += 1
    snake.head.check_direction()
    snake.head.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = "right"
            if event.key == pygame.K_LEFT:
                direction_command = "left"
            if event.key == pygame.K_UP:
                direction_command = "up"
            if event.key == pygame.K_DOWN:
                direction_command = "down"
    
    snake.head.last_direction = snake.head.direction
    if direction_command == "right" and snake.head.canGoRight:
        snake.head.direction = "right"
    if direction_command == "left" and snake.head.canGoLeft:
        snake.head.direction = "left"
    if direction_command == "up" and snake.head.canGoUp:
        snake.head.direction = "up"
    if direction_command == "down" and snake.head.canGoDown:
        snake.head.direction = "down"
        
    pygame.display.flip()
    
pygame.quit()