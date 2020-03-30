import pygame
class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self,largura,altura):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load('imagens/nave01.png')
        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura/2+13
        self.rect.centery = altura - self.rect.height/2

        self.listaDisparo=[]
        self.vida=True
        self.velocidade =20

    def disparar(self,disparo):
        self.listaDisparo.append(disparo)

    def mostrarDisparo(self, tela):
        for i in self.listaDisparo:
            i.rect.y -= 10
            if i.rect.y < -30:
                i.rect.y = -30
                self.listaDisparo.remove(i)

        for i in self.listaDisparo:
            tela.blit(i.ImagemBala, i.rect)

            #tela.blit(i.ImagemBala, i.rect)

    def colocar(self,superficie):
        superficie.blit(self.ImagemNave,self.rect)

    def movimento(self):
        if self.rect.left-15<-15:
            self.rect.left= 0-15
        if self.rect.right>largura+15:
            self.rect.right=largura+15
