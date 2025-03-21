import pygame
from paddle import Paddle
from ball import Ball
from funzioni import disegna_punteggio
import os

pygame.init()
LARGHEZZA,ALTEZZA = 1280, 720
SCHERMO = pygame.display.set_mode((LARGHEZZA,ALTEZZA))

pygame.display.set_caption("Pong")

running = True
clock = pygame.time.Clock()

percorso_asset_mappa = os.path.join("assets","Background_Grid.png")
mappa  = pygame.image.load(percorso_asset_mappa).convert()
mappa = pygame.transform.scale(mappa, (LARGHEZZA, ALTEZZA))
mappa_immagine = mappa

rect_smappa = pygame.Rect(90, 85, LARGHEZZA - 182, ALTEZZA - 172) 


player1 = Paddle(1,90,100,SCHERMO)
player2 = Paddle(2,1155,100,SCHERMO)
palla =  Ball(SCHERMO)

percorso_font = os.path.join("assets","font","pong-score.otf")
font = pygame.font.Font(percorso_font, 40) 


#sezione suoni
percorso_musica = os.path.join("assets","sounds","music.mp3")
musica_gioco = pygame.mixer.Sound(percorso_musica)
musica_gioco.set_volume(0.4)
canale_musica = pygame.mixer.Channel(0) 

if not canale_musica.get_busy():
    canale_musica.play(musica_gioco, loops=-1)


while running:
    clock.tick(60)
    SCHERMO.blit(mappa,(0,0))
    player1.disegna()
    player2.disegna()
    
    
    #pygame.draw.rect(SCHERMO,(255,0,0),rect_smappa,2)
    
   
   
    
    
    tasti = pygame.key.get_pressed()
    player1.movimento(tasti,rect_smappa)
    player2.movimento(tasti,rect_smappa)
    palla.aggiorna()
    palla.disegna()
   
    
    
    if palla.check_collision(player1) or palla.check_collision(player2):
        pass #nella funzione e' presente la modifica di direzione
    
    
    #controllo punto
    if palla.x <= 80:
        player2.punteggio += 1
        #print("punto player 1:",player1.punteggio)
        palla = None
        palla = Ball(SCHERMO)
    elif palla.x >= 1165:
        player1.punteggio += 1
        #print("punto player 2:",player2.punteggio)
        palla = None
        palla = Ball(SCHERMO)
        
        
    
    #controllo eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    disegna_punteggio(SCHERMO,LARGHEZZA,player1.punteggio,player2.punteggio,font)
    pygame.display.update()
    
pygame.quit()