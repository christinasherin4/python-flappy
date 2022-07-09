# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:42:12 2021

@author: ASUS
"""

import pygame
import random
import pygame.font

pygame.init()
SCREEN = pygame.display.set_mode((500,750))
BACKGROUND_IMAGE = pygame.image.load('bb.jpg')


BIRD_IMAGE = pygame.image.load('hh.gif')
bird_x = 50
bird_y = 300
bird_y_change = 0
running = True

def display_bird(x,y):
    SCREEN.blit(BIRD_IMAGE,(x,y))
    
#OBSTACLES
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(100,300)
OBSTACLE_COLOR = "pink"
OBSTACLE_X_CHANGE = -4
obstacle_x = 10

def display_obstacle(height):
    pygame.draw.rect(SCREEN,OBSTACLE_COLOR,(obstacle_x,0,OBSTACLE_WIDTH,height))
    bottom_obstacle_height = 650 - height - 150
    pygame.draw.rect(SCREEN,OBSTACLE_COLOR,(obstacle_x,350,OBSTACLE_WIDTH, -bottom_obstacle_height))
def collision_detection(obstacle_x,obstacle_height,bird_y,bottom_obstacle_height):
                   if obstacle_x >= 50 and obstacle_x <= (50+64):
                         if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
                             return True
                   return False
score = 0 
SCORE_FONT = "sans-serif"
def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}",True,(255,255,255))
    SCREEN.blit(display,(100,200))
running = True
while running:
     SCREEN.fill((0,0,0))
     SCREEN.blit(BACKGROUND_IMAGE,(0,0))
     
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 bird_y_change = -6
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_SPACE:
                 bird_y_change = 3
                 
     bird_y += bird_y_change
     if bird_y <= 0:
         bird_y = 0
     if bird_y >= 571:
         bird_y = 571
     obstacle_x += OBSTACLE_X_CHANGE
     if obstacle_x <= -10:
         obstacle_x = 500
         OBSTACLE_HEIGHT = random.randint(100,300)
         score += 1
     display_obstacle(OBSTACLE_HEIGHT)
     collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y ,OBSTACLE_HEIGHT + 150)
     if collision:
         pygame.quit()
     display_bird(bird_x,bird_y)

     
     pygame.display.update()
pygame.quit()