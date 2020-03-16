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
        update_display()

def draw_lines():
    line_width = 0
    line_height = 0
    aux = width/9
    for item in range(9):
        if item % 3 == 0:
            pygame.draw.line(screen,(0,0,0),(int(line_width), int(line_height)),(int(width), int(line_height)),3)
        else:
            pygame.draw.line(screen,(0,0,0),(int(line_width), int(line_height)),(int(width), int(line_height)))
        line_height += aux
    line_height = 0
    for item in range(9):
        if item % 3 == 0:
            pygame.draw.line(screen,(0,0,0),(int(line_width), int(line_height)),(int(line_width), int(height)),3)
        else:
            pygame.draw.line(screen,(0,0,0),(int(line_width),int(line_height)),(int(line_width), int(height)))
        line_width += aux


def draw_rect():
    for item in sudoku.square_list:
        item.rect = pygame.draw.rect(screen,(255, 255, 255), (int(item.s_width),int(item.s_height), int(item.size), int(item.size)))
        #pygame.draw.line(screen,(0,0,0),(item.s_width,item.s_height),(item.f_width,item.f_height),3)


draw_lines()
draw_rect()
#print(pygame.font.get_fonts())
font = pygame.font.SysFont('arial', 16)

def update_display():
    pygame.display.update()

def handle_draw_number(pos,num):
    global screen
    for item in sudoku.square_list:
        try:
            if item.rect.collidepoint(pos):
                if item.num == 0:
                    screen.blit(font.render('{num}'.format(num=num), True, (0,0,0)), (int(item.num_x), int(item.num_y)))
                    item.num = num
                    update_display()
                else:
                    continue
        except Exception as E:
            print(E)

def draw_answer():
    global sudoku
    for item in range(9):
        for item2 in range(9):
            screen.blit(font.render('{num}'.format(num=sudoku.grid[item][item2].num), True, (0,0,0)), (int(sudoku.grid[item][item2].num_x), int(sudoku.grid[item][item2].num_y)))
    update_display()

def check_key_pressed(pos):
    if event.key == pygame.K_1:
         handle_draw_number(pos,1)
    elif event.key == pygame.K_2:
         handle_draw_number(pos,2)
    elif event.key == pygame.K_3:
         handle_draw_number(pos,3)
    elif event.key == pygame.K_4:
         handle_draw_number(pos,4)
    elif event.key == pygame.K_5:
         handle_draw_number(pos,5)
    elif event.key == pygame.K_6:
         handle_draw_number(pos,6)
    elif event.key == pygame.K_7:
         handle_draw_number(pos,7)
    elif event.key == pygame.K_8:
         handle_draw_number(pos,8)
    elif event.key == pygame.K_9:
         handle_draw_number(pos,9)
    elif event.key == pygame.K_l:
        sudoku.solve()
        draw_answer()

        
aux = True
while True:
    draw_lines()
    update_display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pos = pygame.mouse.get_pos()
            check_key_pressed(pos)
        
    
    
    
    
    