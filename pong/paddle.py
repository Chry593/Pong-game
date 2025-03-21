import pygame
import os

class Paddle():
    def __init__(self,player: int, x: int, y: int,schermo: pygame.SurfaceType):
        self.velocita = 6
        self.player = player
        self.x = x
        self.y = y
        self.schermo = schermo
        self.punteggio = 0
        
        if self.player == 1:
            
            self.asset = os.path.join("assets","Paddle_1.png") 
        else:
            self.asset = os.path.join("assets","Paddle_2.png") 
        
        self.PADDLE_IMG = pygame.image.load(self.asset)  
        self.PADDLE_IMG = pygame.transform.scale(self.PADDLE_IMG, (35, 124))
        self.immagine_corrente = self.PADDLE_IMG 
        self.rect_paddle = self.immagine_corrente.get_rect().inflate(1,1)
        #self.rect.inflate_ip(-0.5,-0.5)
        
    
    def movimento(self, tasto, limiti):
        if self.player == 1:
            if tasto[pygame.K_w]:
                self.y = max(limiti.top, self.y - self.velocita)  
            elif tasto[pygame.K_s]:
                self.y = min(limiti.bottom - self.rect_paddle.height, self.y + self.velocita)  
        else:
            if tasto[pygame.K_UP]:
                self.y = max(limiti.top, self.y - self.velocita)
            elif tasto[pygame.K_DOWN]:
                self.y = min(limiti.bottom - self.rect_paddle.height, self.y + self.velocita)
    
    def disegna(self):
        self.rect_paddle.topleft = (self.x,self.y)
        self.schermo.blit(self.immagine_corrente, self.rect_paddle)
        #pygame.draw.rect(self.schermo,(255,0,0),self.rect_paddle,2)
        