#import pygame

def disegna_punteggio(schermo,larghezza_schermo,punteggio_player1,punteggio_player2,font):
    testo = f"{punteggio_player1}  {punteggio_player2}"
   
    superficie_testo = font.render(testo, True, (255, 255, 255))  
  
    larghezza_testo = superficie_testo.get_width()
    schermo.blit(superficie_testo, ((larghezza_schermo - larghezza_testo + 15) // 2, 20))