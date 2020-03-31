import pygame, sys
from pygame.locals import *
import random
import threading, time, nave
import logicajogo
largura = 445
altura = 400
ponto = 0
pause = False




class Disparo(pygame.sprite.Sprite):
    def __init__(self,jogador):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load('imagens/tiro.jpeg')
        self.rect = self.ImagemBala.get_rect()
        self.rect.x = jogador.rect.x + jogador.rect.width/2 - self.rect.width/2
        self.rect.y = jogador.rect.y - self.rect.height


def printfps(tela,relogio,score,vidas):
    font = pygame.font.SysFont('comicsansms', 30)
    text = font.render('FPS: '+str(int(relogio.get_fps())), True, (255, 0, 0))
    score = font.render('score: '+str(score),True,(255,0,0))
    vida = font.render('Vidas: '+str(vidas),True,(255,0,0))
    tela.blit(text,(0,10))
    tela.blit(score,(100,10))
    tela.blit(vida,(300,10))


def tirojogador(jogador,vidas):
    laser = pygame.mixer.Sound('sons/laser.ogg')
    global pause
    while vidas > 0:
        jogador.disparar(Disparo(jogador))
        laser.set_volume(.1)
        laser.play()
        while pause == True:
            pass
        time.sleep(.2)
    sys.exit()


def IniciaJogo():
    global vidas, ponto
    logica = logicajogo.Logica(largura,altura,ponto,pause)
    jogador = nave.NaveEspacial(largura,altura)
    t = threading.Thread(target=tirojogador, args=(jogador,logica.vidas))
    pygame.init()
    pygame.mixer.music.load('sons/musica_fundo.ogg')
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1)
    imagemfundo = pygame.image.load('imagens/cenario2.jpg')
    tela = pygame.display.set_mode((largura,altura))
    relogio = pygame.time.Clock()
    pygame.display.set_caption('teste')
    t.start()

    while True:
        relogio.tick(70)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                logica.vidas=0
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogador.rect.left -= jogador.velocidade
                    jogador.movimento()
                if evento.key == pygame.K_RIGHT:
                    jogador.rect.right += jogador.velocidade
                    jogador.movimento()
                if evento.key == pygame.K_KP_ENTER:
                    logica.adicionaInimigo()
                if evento.key == pygame.K_ESCAPE:
                    logica.listaAsteroides.clear()
            jogador.rect.centerx = pygame.mouse.get_pos()[0]
            #jogador.movimento()
        if(pygame.time.get_ticks() % 15) == 0:
            logica.adicionaInimigo()

        tela.blit(imagemfundo,(0,0))
        jogador.colocar(tela)
        jogador.mostrarDisparo(tela)
        logica.logicaInimigos(tela,jogador.listaDisparo)
        printfps(tela,relogio,logica.score,logica.vidas)
        pygame.display.update()


IniciaJogo()

