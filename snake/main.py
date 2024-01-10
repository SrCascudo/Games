import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Plano Cartesiano
COORDENADA_X = 640
COORDENADA_Y = 480

# CONSTANTES
TELA = pygame.display.set_mode((COORDENADA_X, COORDENADA_Y))
RELOGIO = pygame.time.Clock()
FONTE = pygame.font.SysFont('arial', 20, True, False)

# CORES
RED = (255, 0, 0)
GREEN = (52, 115, 10)
BLUE = (0, 0, 255)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)

def verificar_fechar(event):
    if event.type == QUIT:
        pygame.quit()
        exit()

# PROPRIEDADES INICIAIS DA SNAKE
snake_x = 10
snake_y = 10

snake_body_size = 30
snake_body_width = 20
snake_head_size = 10
snake_head_width = 20

# PROPRIEDADES DE MOVIMENTO
add_x = 0
add_y = 0
direction = 0
previous_direction = 0
unit_move = 10
while True:
    RELOGIO.tick(10)
    TELA.fill(GREEN)

    for event in pygame.event.get():
        verificar_fechar(event)
    
    if pygame.key.get_pressed()[K_UP]:
        direction = 1      

    if pygame.key.get_pressed()[K_RIGHT]:
        direction = 2      

    if pygame.key.get_pressed()[K_DOWN]:
        direction = 3       

    if pygame.key.get_pressed()[K_LEFT]:
        direction = 4

    # ENIBIR MOVIMENTO DE RÉ
    if (previous_direction == direction+2) or (previous_direction == direction-2):
        direction = previous_direction

    # MOVIMENTO PERPETUO
    if direction == 1: 
        '''UP'''
        if snake_y != (0-snake_body_size):
            snake_y -= unit_move
        else:
            snake_y = COORDENADA_Y+unit_move

    elif direction == 2:
        '''RIGHT'''
        if snake_x != (snake_body_width+COORDENADA_X):
            snake_x += unit_move
        else:
            snake_x = 0-unit_move

    elif direction == 3:
        '''DOWN'''
        if snake_y != (COORDENADA_Y+snake_body_size):
            snake_y += unit_move
        else:
            snake_y = 0-unit_move

    elif direction == 4:
        '''LEFT'''
        if snake_x != (0-snake_body_width):
            snake_x -= unit_move
        else:
            snake_x = COORDENADA_X+unit_move


    previous_direction = direction

    # ELEMENTOS DINÂMICOS
    SNAKE_BODY = pygame.draw.rect(TELA, WHITE, (snake_x, snake_y, snake_body_width, snake_body_size))
    SNAKE_HEAD = pygame.draw.rect(TELA, BLACK, ((add_x + snake_x), (snake_y + add_y), snake_head_width, snake_head_size))

    pygame.display.update()
