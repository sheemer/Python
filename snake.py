from asyncore import read
from distutils.file_util import write_file
from importlib.resources import open_text
import time
import random
from turtle import Screen
import pygame
import os 
import requests

file = open("highscore.txt","a+")
clock = pygame.time.Clock()
snake_speed = 15

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


img_data = requests.get('https://i.redd.it/wq6nqm0omzv91.png').content
with open('wq6nqm0omzv91.png', 'wb') as handler:
    handler.write(img_data)

pygame.init()
screen = pygame.display.set_mode()
x, y = screen.get_size()
window_x = x
window_y = y
game_window = pygame.display.set_mode((window_x,window_y), pygame.FULLSCREEN)
bg_img = pygame.image.load('wq6nqm0omzv91.png')
bg_img = pygame.transform.smoothscale(bg_img, game_window.get_size())
#/Users//jonny5//Pictures//wq6nqm0omzv91.png
#https://i.redd.it/wq6nqm0omzv91.png
fps = pygame.time.Clock()

snake_position = [100,50]

snake_body =[ [100,50],
             [90,50],
             [80,50],
             [70,50]
             ]

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10 ]
fruit_spawn = True
Direction = 'RIGHT'
change_to = Direction


score = 0
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : '+ str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

       

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Score is : ' + str(score) )
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2,window_y)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def startscreen():
    
    startscreen = True

    while startscreen:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        bg_img.fill(white)
        largewords = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Snake", largewords)
        TextRect.center = ((window_x),(window_y))
        game_window.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

    
highscorefile = open("highscore.txt", 'r')
highscore = highscorefile.read()
def show_highscore(choice, color, font, size):
    highscore_font = pygame.font.SysFont(font, size)
    highscore_surface = highscore_font.render('High Score : '+ str(highscore), True, color)
    highscore_rect = highscore_surface.get_rect()
    game_window.blit(highscore_surface, (0,20), highscore_rect)
   
highscore1 = ('highscore.txt')
if os.stat(highscore1).st_size == 0:
    highscorewrite =open("highscore.txt","w")
    highscorewrite.write(str(10))
while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                
        if change_to == 'UP' and Direction != 'DOWN':
            Direction = 'UP'
        if change_to == 'DOWN' and Direction != 'UP':
            Direction = 'DOWN'
        if change_to == 'LEFT' and Direction != 'RIGHT':
            Direction = 'LEFT'
        if change_to == 'RIGHT' and Direction != 'LEFT':
            Direction = 'RIGHT'
    
        if Direction == 'UP':
            snake_position[1] -= 10
        if Direction == 'DOWN':
            snake_position[1] += 10
        if Direction == 'LEFT':
            snake_position[0] -= 10
        if Direction == 'RIGHT':
            snake_position[0] += 10
        
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
        fruit_spawn = True
        game_window.blit(bg_img, (0,0))
    
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
            

        if snake_position[0] < 0 or snake_position[0] > window_x-10:
         game_over()
        if snake_position[1] < 0 or snake_position[1] > window_x-10:
         game_over()

#touching the snakebody 
        for block in snake_body[1:]:
            if snake_position [0] == block[0] and snake_position[1] == block[1]:
                 game_over()

#score board live update
        show_score(1, white, 'times new roman', 20)
        show_highscore(1, white, 'times new roman', 20)
       
            
#saving scor
       # 
    
#refesh gmae 
        pygame.display.update()
        highscore_int = int(highscore)
        if score > highscore_int:
            highscore_write = open("highscore.txt", 'w')
            highscore_write.write(str(score))

#frames per second
        fps.tick(snake_speed)
        
        #hisc.close()