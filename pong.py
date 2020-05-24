import pygame
import sys

pygame.init()

# functions that moves paddles
# function that calculates ball path upon bouncing
# function that determines where ball moves
# function that gives points
# stop game once someone wins
# function that draws

pygame.display.set_caption('  Pong')
screen = pygame.display.set_mode((700, 400))
black = (0, 0, 0)
yellow = (247, 243, 163)
white = (255, 255, 255)
paddle1 = pygame.Rect(50, 150, 10, 50)
paddle2 = pygame.Rect(640, 150, 10, 50)
ball = pygame.Rect(346, 196, 8, 8)

def draw(p1, p2, b):
    pygame.draw.line(screen, yellow, (349.5, 0), (349.5, 400))
    
    pygame.draw.rect(screen, white, p1, 0)
    pygame.draw.rect(screen, white, p2, 0)
    
    pygame.draw.rect(screen, white, b, 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    
    screen.fill(black)
    draw(paddle1, paddle2, ball)
    
    pygame.time.delay(int(1000/30))
    pygame.display.update()