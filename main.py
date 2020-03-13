import pygame
import sys
import sudoku as su
import numpy as np


pygame.init()
size = width, height = 900, 900
white = 255, 255, 255
screen = pygame.display.set_mode(size)
screen.fill(white)
sudoku = su.Sudoku(width)


def sudoku_intro():
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Sudoku', False, (0, 0, 0))
    textsurface = myfont.render('Start', False, (0, 0, 0))
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(textsurface,(int((width/2) - width/16),int(height/8)))
        screen.blit(textsurface)
        pygame.display.update()

def draw_lines():
    line_width = 0
    line_height = 0
    aux = width/9
    for item in range(9):
        if line_height % 3 == 0:
            pygame.draw.line(screen,(0,0,0),(int(line_width), int(line_height)),(int(width), int(line_height)),3)
        else:
            pygame.draw.line(screen,(0,0,0),(int(line_width), int(line_height)),(int(width), int(line_height)))
        line_height += aux
    line_height = 0
    for item in range(9):
        if line_width % 3 == 0:
            pygame.draw.line(screen,(0,0,0),(int(line_width), int(line_height)),(int(line_width), int(height)),3)
        else:
            pygame.draw.line(screen,(0,0,0),(int(line_width),int(line_height)),(int(line_width), int(height)))
        line_width += aux


def draw_lines_temp():
    for item in sudoku.square_list:
        item.rect = pygame.draw.rect(screen,(255,0,0), (int(item.s_width),int(item.s_height), int(item.size), int(item.size)))
        #pygame.draw.line(screen,(0,0,0),(item.s_width,item.s_height),(item.f_width,item.f_height),3)


draw_lines()
draw_lines_temp()

while True:
    draw_lines()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for item in sudoku.square_list:
                if item.rect.collidepoint(pos):
                    pygame.draw.rect(screen,(0, 0, 255), (int(item.s_width),int(item.s_height), int(item.size), int(item.size)))

    
    
    
    
    