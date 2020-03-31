import nave,pygame,random, sys
from pygame.locals import *

#Classe responsável pela lógica do jogo
class Logica(nave.NaveEspacial):

    def __init__(self,largura,altura,score,pause):

        self.pause = pause
        self.vidas = 3
        self.score = score
        self.largura = largura
        self.altura = altura
        self.listaAsteroides = []
        self.listaDisparo=[]
 #adiciona na estrutura de dados       
    def adicionaInimigo(self):
        self.listaAsteroides.append(nave.NaveEspacial(self.largura,self.altura))
        self.listaAsteroides[-1].ImagemNave = pygame.image.load('imagens/asteroide.png')
        self.listaAsteroides[-1].rect.centerx = random.randint(0, self.largura)
        self.listaAsteroides[-1].rect.centery=-30
#blita asteroid, verifica se o tiro colidiu e remove, coloca texto na tela, verifica vida, pausa
#futura refatoraçao completa do código
    def logicaInimigos(self,tela,listadisparo):
        for i in self.listaAsteroides:
            tela.blit(i.ImagemNave, i.rect)
        for i in self.listaAsteroides:
            for j in listadisparo:
                if i.rect.colliderect(j):
                    self.score = self.score + 10
                    try:
                        self.listaAsteroides.remove(i)
                    except ValueError:
                        pass
                    listadisparo.remove(j)
        for i in self.listaAsteroides:
            i.rect.y += 1
            if i.rect.y == self.altura-i.rect.height:
                self.pause = True
                self.vidas -= 1
                font = pygame.font.SysFont('comicsansms', 30)
                font2 = pygame.font.SysFont('comicsansms', 20)
                pressioneEnter= font2.render('(ENTER)', True, (255, 0, 0))
                if self.vidas == 0:
                    string = 'GAME OVER'
                    text = font.render(string, True, (255, 0, 0))
                    tela.blit(text, (150, 160))
                    tela.blit(pressioneEnter, (195, 190))
                if self.vidas == 1:
                    string = '1 vida'
                    text = font.render(string, True, (255, 0, 0))
                    tela.blit(text, (195, 160))
                    tela.blit(pressioneEnter, (195, 190))
                if self.vidas == 2:
                    string = '2 vidas'
                    text = font.render(string, True, (255, 0, 0))
                    tela.blit(text, (185, 160))
                    tela.blit(pressioneEnter, (195, 190))

                pygame.display.update()
                while self.pause == True:
                    for evento in pygame.event.get():
                        if evento.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_RETURN:
                                self.pause = False
                self.listaAsteroides.clear()
                self.listaDisparo.clear()
                if self.vidas == 0:           
                    pygame.quit()
                    sys.exit()
