import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Plano Cartesiano
x = 640
y = 480

pygame.mixer.music.set_volume(0.5)
som_fundo = pygame.mixer.music.load('song/background.mp3')
pygame.mixer.music.play(-1)

som_recompensa = pygame.mixer.Sound('song/coin.wav')
som_recompensa.set_volume(1)

tela = pygame.display.set_mode((x, y))
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 20, True, False)
pygame.display.set_caption('Game')


vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
branco = (255,255,255)

cordenada_x = 90
cordenada_y = 240

white_x = randint(0, x-20)
white_y = randint(0, y-20)
pontos = 0
while True:
    relogio.tick(30)
    tela.fill((100,100,100))
    mensagem = f'Pts: {pontos}'

    texto_formatado = fonte.render(mensagem, False, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        '''
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                cordenada_x = cordenada_x + 10

            if event.key == K_LEFT:
                cordenada_x = cordenada_x - 10
            
            if event.key == K_UP:
                cordenada_y = cordenada_y - 10

            if event.key == K_DOWN:
                cordenada_y = cordenada_y + 10
        '''
    
    if pygame.key.get_pressed()[K_RIGHT]:
        cordenada_x = cordenada_x + 10

    if pygame.key.get_pressed()[K_LEFT]:
        cordenada_x = cordenada_x - 10
            
    if pygame.key.get_pressed()[K_UP]:
        cordenada_y = cordenada_y - 10

    if pygame.key.get_pressed()[K_DOWN]:
        cordenada_y = cordenada_y + 10


    # Estático
    pygame.draw.rect(tela, verde, (40, 40 , 560, 400))
    pygame.draw.line(tela, vermelho, (x/2, 40), (x/2, 440), 3)

    # Dinâmico
    circle = pygame.draw.circle(tela, azul if cordenada_x < 320 else vermelho, (cordenada_x, cordenada_y), 20)
    white = pygame.draw.circle(tela, branco, (white_x, white_y), 20)        
    
    if circle.colliderect(white):
        white_x = randint(0, x-20)
        white_y = randint(0, y-20)
        white = pygame.draw.circle(tela, branco, (white_x, white_y), 20)
        pontos = pontos + 1
        som_recompensa.play()
        
    tela.blit(texto_formatado, (10, 10))
    pygame.display.update()
