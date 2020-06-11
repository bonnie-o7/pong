import pygame
import pygame.freetype
import sys
import socket
from enum import Enum

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
paddle1 = pygame.Rect(640, 150, 10, 50)
paddle2 = pygame.Rect(50, 150, 10, 50)
ball = pygame.Rect(346, 196, 10, 10)
ball_vector = pygame.math.Vector2(5, 5)
top_border = pygame.Rect(0, -99, 700, 100)
bottom_border = pygame.Rect(0, 399, 700, 100)
right_paddle_turn = True
player1_goal = pygame.Rect(-100, 0, 80, 400)
player2_goal = pygame.Rect(720, 0, 100, 400)
player1_score = 0
player2_score = 0
font = pygame.freetype.Font(None, 20)
Screen = Enum('Screen', 'title game')
current_screen = Screen.title

def draw(p1, p2, b):
    screen.fill(black)

    pygame.draw.line(screen, yellow, (349.5, 0), (349.5, 400))
    
    pygame.draw.rect(screen, white, p1, 0)
    pygame.draw.rect(screen, white, p2, 0)
    
    pygame.draw.rect(screen, white, b, 0)

    font.render_to(screen, (270, 50), str(player1_score), white)
    font.render_to(screen, (415, 50), str(player2_score), white)

    pygame.display.update()

def move_paddles(paddle1, paddle2):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        if paddle1.top - 10 >= 0:
            paddle1 = paddle1.move(0, -10)
    if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        if paddle1.bottom + 10 <= 400:
            paddle1 = paddle1.move(0, 10)
    if keys[pygame.K_w] and not keys[pygame.K_s]:
        if paddle2.top - 10 >= 0:
            paddle2 = paddle2.move(0, -10)
    if keys[pygame.K_s] and not keys[pygame.K_w]:
        if paddle2.bottom + 10 <= 400:
            paddle2 = paddle2.move(0, 10)
    return paddle1, paddle2

def move_ball(ball, ball_vector, right_paddle_turn):
    if ball.colliderect(top_border) or ball.colliderect(bottom_border):
        ball_vector = pygame.math.Vector2(ball_vector[0], ball_vector[1] * -1)
    if (ball.colliderect(paddle2) and not right_paddle_turn) or (ball.colliderect(paddle1) and right_paddle_turn):
        ball_vector = pygame.math.Vector2(ball_vector[0] * -1, ball_vector[1])
        right_paddle_turn = not right_paddle_turn
    return ball.move(ball_vector), ball_vector, right_paddle_turn

def restart():
    global paddle1, paddle2, ball    
    
    paddle1 = pygame.Rect(640, 150, 10, 50)
    paddle2 = pygame.Rect(50, 150, 10, 50)
    ball = pygame.Rect(346, 196, 10, 10)

    draw(paddle1, paddle2, ball)
    pygame.time.delay(2000)

def scored():
    global player1_score, player2_score
    
    if ball.colliderect(player1_goal):
        player2_score += 1
        restart()

    if ball.colliderect(player2_goal):
        player1_score += 1
        restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    
    if current_screen == Screen.title:
        screen.fill(black)
        font.render_to(screen, (320, 30), 'Pong', white)
        pygame.draw.rect(screen, white, (310, 75, 150, 30), 0)
        font.render_to(screen, (320, 80), 'Single player', black)
        pygame.draw.rect(screen, white, (310, 200, 150, 30), 0)
        font.render_to(screen, (320, 210), 'Create Room', black)
        pygame.draw.rect()

        pygame.display.update()
        
    elif current_screen == Screen.game:
        paddle1, paddle2 = move_paddles(paddle1, paddle2)
        ball, ball_vector, right_paddle_turn = move_ball(ball, ball_vector, right_paddle_turn)
        scored()
        draw(paddle1, paddle2, ball)

    pygame.time.delay(int(1000/30))

