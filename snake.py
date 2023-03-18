
import pygame
import copy
import random

pygame.init()
# 1 = light green, 2 = dark green, 3 = wall, 4 = light green with apple, 5 = dark green with apple
#18 x 16 board, 850x750

snakeHead_image = pygame.image.load('assets/snake.png')
snakeTail_image = pygame.image.load('assets/tail.png')
orange_image = pygame.image.load('assets/orange.png')

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
        self.image = orange_image
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def randomize(self):
        self.row_index = random.randint(0, rows-1)
        self.col_index = random.randint(0, cols-1)
        self.rect.x = 58 + (50 * self.col_index)
        self.rect.y = 158 + (50 * self.row_index)

class Segment:
    def __init__(self, x, y, image):
        self.next_segment = None
        self.last_segment = None
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center_x = x + 20
        self.center_y = y + 20
        self.direction = "none"
        self.index = 0
        self.move_delay = 0
        
    def moveLeft(self, speed):
        self.rect.x -= speed
        self.center_x -= speed
    
    def moveRight(self, speed):
        self.rect.x += speed
        self.center_x += speed
    
    def moveUp(self, speed):
        self.rect.y -= speed
        self.center_y -= speed
    
    def moveDown(self, speed):
        self.rect.y += speed
        self.center_y += speed
            
class Snake:
    def __init__(self, x, y):
        self.head = Segment(x, y, snakeHead_image)
        self.length = 1
        self.tail = self.head
        self.direction = "none"
        self.last_direction = "none"
        self.canGoLeft = False
        self.canGoRight = False
        self.canGoUp = False
        self.canGoDown = False
        self.speed = 5
        self.offset = 50
        self.totalSegments = 0
        
    def move(self):

        if self.direction == "left" and self.canGoLeft:
            self.head.moveLeft(self.speed)
        elif self.direction == "right" and self.canGoRight:
            self.head.moveRight(self.speed)
        elif self.direction == "up" and self.canGoUp:
            self.head.moveUp(self.speed)
        elif self.direction == "down" and self.canGoDown:
            self.head.moveDown(self.speed)
        else:
            self.direction = self.last_direction
            
            
    def check_direction(self):
        centerAdjust = 30
        currentSquare_x = self.head.center_x - ((self.head.center_x // 50) * 50)
        currentSquare_y = self.head.center_y - ((self.head.center_y // 50) * 50)
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
        
        if (self.head.center_x - centerAdjust) < 50:
            self.canGoLeft = False
        if (self.head.center_x + centerAdjust) > 900:
            self.canGoRight = False
        if (self.head.center_y + centerAdjust) < 210:
            self.canGoUp = False
        if (self.head.center_y - centerAdjust) > 840:
            self.canGoDown = False
    
    def addSegment(self):
        last_segment = self.tail
        if self.direction == "left":
            new_segment = Segment(last_segment.rect.x + self.offset, last_segment.rect.y, snakeTail_image)
        elif self.direction == "right":
            new_segment = Segment(last_segment.rect.x - self.offset, last_segment.rect.y, snakeTail_image)
        elif self.direction == "up":
            new_segment = Segment(last_segment.rect.x, last_segment.rect.y + self.offset, snakeTail_image)
        elif self.direction == "down":
            new_segment = Segment(last_segment.rect.x, last_segment.rect.y - self.offset, snakeTail_image)
        last_segment.next_segment = new_segment
        new_segment.last_segment = last_segment
        self.tail = new_segment
        self.totalSegments += 1
        new_segment.index = self.totalSegments
        new_segment.move_delay = new_segment.index * 10
        new_segment.direction = self.direction

    def updateSegmentDirection(self):
        current = self.head.next_segment
        prev = self.head
        if prev == self.head:
            prev.direction = self.direction    
        while current:
            if current.direction == "right" and prev.direction == "up":
                if current.center_x == prev.center_x:
                    current.direction = "up"
            elif current.direction == "right" and prev.direction == "down":
                if current.center_x == prev.center_x:
                    current.direction = "down"
            elif current.direction == "left" and prev.direction == "up":
                if current.center_x == prev.center_x:    
                    current.direction = "up"
            elif current.direction == "left" and prev.direction == "down":
                if current.center_x == prev.center_x:    
                    current.direction = "down"
            elif current.direction == "up" and prev.direction == "left":
                if current.center_y == prev.center_y:
                    current.direction = "left"
            elif current.direction == "up" and prev.direction == "right":
                if current.center_y == prev.center_y:
                        current.direction = "right"    
            elif current.direction == "down" and prev.direction == "left":
                if current.center_y == prev.center_y:
                            current.direction = "left"
            elif current.direction == "down" and prev.direction == "right":
                if current.center_y == prev.center_y:
                            current.direction = "right"              
            prev = current
            current = current.next_segment
    
    
    def moveSegments(self):
        current = self.head.next_segment
        prev = self.head
        if prev == self.head:
            prev.direction = self.direction
        while current:
            if current.direction == "left":
                current.moveLeft(self.speed)
            elif current.direction == "right":
                current.moveRight(self.speed)
            elif current.direction == "up":
                current.moveUp(self.speed)
            elif current.direction == "down":
                current.moveDown(self.speed)
            prev = current
            current = current.next_segment
        #for each segment in the list of segments, each segment should wait 10 * indexOfSegments before moving
                        
    def draw(self, screen):
        segment = self.head
        while segment is not None:
            screen.blit(segment.image, segment.rect)
            segment = segment.next_segment
                  
WIDTH = 950
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',20)
fps = 60
level = copy.deepcopy(board)
rows = 15
cols = 17
orange = Orange()
snake = Snake(255, 505)
score = 0
direction_command = "none"
move_delay = 0


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
        snake.addSegment()
        score += 1
    snake.check_direction()
    snake.move()
    snake.updateSegmentDirection()
    snake.moveSegments()
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
    
    snake.last_direction = snake.direction
    if direction_command == "right" and snake.canGoRight:
        snake.direction = "right"
    if direction_command == "left" and snake.canGoLeft:
        snake.direction = "left"
    if direction_command == "up" and snake.canGoUp:
        snake.direction = "up"
    if direction_command == "down" and snake.canGoDown:
        snake.direction = "down"
    
    pygame.display.flip()
    
pygame.quit()