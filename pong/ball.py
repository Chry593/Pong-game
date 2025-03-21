import pygame
import math
import random
import os


class Ball():
    def __init__(self, schermo: pygame.SurfaceType):
        self.x = 640
        self.y = 360
        self.velocita = 4
        self.schermo = schermo
        self.raggio = 15  # La palla è 30x30, quindi raggio = 15
        self.punto_fatto = False

        self.ball_asset = os.path.join("assets","Ball.png") 
        self.BALL_IMG = pygame.image.load(self.ball_asset)  
        self.BALL_IMG = pygame.transform.scale(self.BALL_IMG, (30, 30))
        self.rect_palla = pygame.Rect(self.x, self.y, 26, 26)

        self.reset()  # Imposta la direzione iniziale

    def reset(self):
        angolo = random.uniform(-45, 45)  # Angolo casuale tra -45° e 45°
        direzione_x = random.choice([-1, 1])  # Sceglie se andare a sinistra o destra
        rad = math.radians(angolo)  

        self.velocita_x = self.velocita * math.cos(rad) * direzione_x
        self.velocita_y = self.velocita * math.sin(rad)

        velocita_totale = math.sqrt(self.velocita_x**2 + self.velocita_y**2)
        factor = self.velocita / velocita_totale
        self.velocita_x *= factor
        self.velocita_y *= factor
        
        self.aggiorna()

    def aggiorna(self):
        self.x += self.velocita_x
        self.y += self.velocita_y
        if self.y - 15 <= 85 or self.y + 15 >= 635: 
            self.velocita_y *= -1 
        self.rect_palla.center = (round(self.x), round(self.y))
        


    def disegna(self):
        if self.punto_fatto == False:       
            self.schermo.blit(self.BALL_IMG, (round(self.x) - self.raggio, round(self.y) - self.raggio))
            #pygame.draw.rect(self.schermo, (255, 0, 0), self.rect_palla, 2) 
    
    
    
    
    def check_collision(self, paddle):
        if self.rect_palla.colliderect(paddle.rect_paddle):  # Se collide con il paddle
            offset = (self.y - paddle.rect_paddle.centery) / (paddle.rect_paddle.height / 2)
            max_angolo = 45  
            
            nuovo_angolo = offset * max_angolo  
            rad = math.radians(nuovo_angolo)

         
            self.velocita_x *= -1  
            self.velocita_y = self.velocita * math.sin(rad)  
            
            velocita_totale = math.sqrt(self.velocita_x**2 + self.velocita_y**2)
            factor = self.velocita / velocita_totale
            self.velocita_x *= factor
            self.velocita_y *= factor            
            
            self.velocita += 1
            print(self.velocita)
            return True
        return False


            

    
