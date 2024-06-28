import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time
import sys

pygame.init()

largura_tela = 900
altura_tela = 580

x = int(largura_tela/2) #posição
y = int(largura_tela/2) #posição

raio_personagem0 = 20
raio_personagem1 = 30
raio_personagem2 = 40
raio_personagem3 = 8
raio_personagem4 = 36
raio_fruta = 20

x_fruta = randint(30, 870) #valor aleatorio de posição eixo X
y_fruta = randint(20, 550) #valor aleatorio de posição eixo Y

c = 0  # pontos
fghj = "fghj"
#skins
a0 = 0
a1 = 1
a2 = 2
a3 = 3
a4 = 4

pontos = pygame.font.SysFont("arial", 30, True, False)
dica = pygame.font.SysFont("arial", 20, True, False)

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Ajude o Kakyoin! v0.1 / GITHUB: jjoaop")
run = pygame.time.Clock()

# fundo do jogo
imagem_fundo = pygame.image.load("kakyoin/personagem/fundo.png")

# musica de fundo
musica_fundo1 = pygame.mixer.music.load("kakyoin/audios/fase1.mp3")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)
# barulho de pegar item
colisao = pygame.mixer.Sound("kakyoin/audios/item.wav")
colisao.set_volume(0.3)

while c != 85:

    run.tick(30) #frames por segundo
    tela.blit(imagem_fundo, (0, 0))
    #tela.fill((0,0,255)) cor da tela


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #controle de movimento

    m_a = pygame.key.get_pressed()[K_a]

    m_d = pygame.key.get_pressed()[K_d]

    m_w = pygame.key.get_pressed()[K_w]

    m_s = pygame.key.get_pressed()[K_s]


    #carregar e desenhar imagens

    o_personagem0 = pygame.image.load("kakyoin/personagem/a0.png")

    o_personagem1 = pygame.image.load("kakyoin/personagem/a1.png")

    o_personagem2 = pygame.image.load("kakyoin/personagem/a2.png")

    o_personagem3 = pygame.image.load("kakyoin/personagem/a3.png")

    o_personagem4 = pygame.image.load("kakyoin/personagem/a4.png")


    # inicialização do item
    a_fruta = pygame.image.load("kakyoin/personagem/fruta.png")
    tela.blit(a_fruta, (x_fruta, y_fruta))
    fruta = a_fruta.get_rect()

    #pontuação
    pontos_fase1 = f"Pontos: {c}"
    pontos_tela1 = pontos.render(pontos_fase1, False, (0, 0, 0))
    tela.blit(pontos_tela1, (700, 50))

    #condição para verificar se o personagem saiu da tela
    if x < 0 or x > largura_tela or y < 0 or y > altura_tela:
        # O personagem saiu da tela, reinicie as variáveis
        x = int(largura_tela / 2)
        y = int(altura_tela / 2)
        c = 0

    # fase 1 - colheita
    if c < 15:
        tela.blit(o_personagem0, (x, y))
        personagem = o_personagem0.get_rect()
        if m_a:
            x = x - 10
        if m_d:
            x = x + 10
        if m_w:
            y = y - 10
        if m_s:
            y = y + 10

    if c >= 15 and c < 35 :
        tela.blit(o_personagem1, (x, y))
        personagem = o_personagem1.get_rect()
        if m_a:
            x = x - 40
        if m_d:
            x = x + 40
        if m_w:
            y = y - 40
        if m_s:
            y = y + 40

    if c >= 35 and c < 50:
        tela.blit(o_personagem2, (x, y))
        personagem = o_personagem2.get_rect()
        if m_a:
            x = x + 40
        if m_d:
            x = x - 40
        if m_w:
            y = y + 40
        if m_s:
            y = y - 40

    if c >= 50 and c < 72:
        dica1 = f"{fghj}"
        seila = dica.render(dica1, False, (0, 0, 0))
        tela.blit(seila, (100, 50))
        m_a = pygame.key.get_pressed()[K_f]

        m_d = pygame.key.get_pressed()[K_g]

        m_w = pygame.key.get_pressed()[K_h]

        m_s = pygame.key.get_pressed()[K_j]
        tela.blit(o_personagem3, (x, y))
        personagem = o_personagem3.get_rect()
        if m_a:
            x = x + 40
        if m_d:
            x = x - 40
        if m_w:
            y = y + 40
        if m_s:
            y = y - 40

    if c >= 72 and c < 82:
        tela.blit(o_personagem3, (x, y))
        personagem = o_personagem3.get_rect()
        if m_a:
            x = x - 10
        if m_d:
            x = x + 10
        if m_w:
            y = y - 10
        if m_s:
            y = y + 10

    if c >= 82 and c < 85:

        pontos_fase1 = (f"você não está sozinho \n você não está sozinho \n você não está sozinho "
                        f"\n você não está sozinho "
                        f"\n você não está sozinho \n você não está sozinho \nvocê não está sozinho \n")
        pontos_tela1 = pontos.render(pontos_fase1, False, (0, 0, 0))
        tela.blit(pontos_tela1, (700, 50))
        imagem_fundo = pygame.image.load("kakyoin/personagem/fundo2.jpg")
        tela.blit(o_personagem4, (x, y))
        personagem = o_personagem4.get_rect()
        if m_a:
            x = x - 1
        if m_d:
            x = x + 1
        if m_w:
            y = y - 1
        if m_s:
            y = y + 1


    # calcula a distância entre o personagem e a fruta
    distancia = ((x - x_fruta) ** 2 + (y - y_fruta) ** 2) ** 0.5
    # fase 1 - colheita
    if distancia <= raio_personagem0 + raio_fruta:
        c += 1
        print(c)
        x_fruta = randint(30, 870)
        y_fruta = randint(20, 550)
        i = c
        colisao.play()
    if distancia <= raio_personagem1 + raio_fruta:
        c += 1
        print(c)
        x_fruta = randint(30, 870)
        y_fruta = randint(20, 550)
        i = c
        colisao.play()
    if distancia <= raio_personagem2 + raio_fruta:
        c += 1
        print(c)
        x_fruta = randint(30, 870)
        y_fruta = randint(20, 550)
        i = c
        colisao.play()
    if distancia <= raio_personagem3 + raio_fruta:
        c += 1
        print(c)
        x_fruta = randint(30, 870)
        y_fruta = randint(20, 550)
        i = c
        colisao.play()
    if distancia <= raio_personagem4 + raio_fruta:
        c += 1
        print(c)
        x_fruta = randint(30, 870)
        y_fruta = randint(20, 550)
        i = c
        colisao.play()




    pygame.display.update()

time.sleep(6)  #pausa o jogo por 3 segundos
sys.exit() #fecha o jogo