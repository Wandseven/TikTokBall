import pygame
import numpy as np
import math
import random

# Everytime the ball hits the circle, 2 more balls are added to the list.

class Ball:
    def __init__(self, position, velocity):
        self.pos = np.array(position, dtype=np.float64)
        self.v = np.array(velocity, dtype=np.float64)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.is_in = True

pygame.init()
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CIRCLE_CENTER = np.array([WIDTH // 2, HEIGHT // 2], dtype=np.float64)
CIRCLE_RADIUS = 200
BALL_RADIUS = 5
ball_pos = np.array([WIDTH // 2, HEIGHT // 2 - 120],dtype=np.float64)
running = True
GRAVITY = 0.2
ball_vel = np.array([1, 0],dtype=np.float64)
balls =[Ball(ball_pos, ball_vel)]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for ball in balls:
        ball.v[1] += GRAVITY
        ball.pos += ball.v
        dist = np.linalg.norm(ball.pos - CIRCLE_CENTER)
        if dist + BALL_RADIUS > CIRCLE_RADIUS:
            d = ball.pos - CIRCLE_CENTER
            d_unit = d/np.linalg.norm(d)
            ball.pos = CIRCLE_CENTER + (CIRCLE_RADIUS - BALL_RADIUS) * d_unit
            t = np.array([-d[1], d[0]], dtype=np.float64)
            proj_v_t = np.dot(ball.v,t)/np.dot(t, t) * t
            ball.v = 2 * proj_v_t - ball.v
            balls.append(Ball(position=[WIDTH//2,HEIGHT//2 - 120], velocity=[random.uniform(-5, 5), random.uniform(-5, 5)]))
#           balls.append(Ball(position=[WIDTH//2,HEIGHT//2 - 120], velocity=[random.uniform(-5, 5), random.uniform(-5, 5)]))

        

    window.fill(BLACK)
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
    for ball in balls:
        pygame.draw.circle(window, ball.color, ball.pos, BALL_RADIUS)


    pygame.display.flip()  
    clock.tick(60)

pygame.quit()
