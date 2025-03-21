# Pong Game

Questo è un progetto di gioco ispirato a Pong, sviluppato utilizzando Python e la libreria Pygame. Il gioco presenta due giocatori che si sfidano in una partita di Pong, con grafica, suoni e meccaniche di gioco personalizzate.

## Crediti

- **Asset grafici**: gli asset del gioco sono stati presi dal pacchetto [Neon Pong](https://hektorprofe.itch.io/neon-pong) su Itch.io.
- **Suoni**: i suoni sono stati presi dal sito [OpenGameArt.org](https://opengameart.org/content/pong-0).

## Requisiti

- Python 3.x
- Pygame (assicurati di avere installato Pygame nel tuo ambiente di sviluppo)

## Installazione

1. Clona il repository.
2. Installa le dipendenze (Pygame).

## Come Giocare

- Usa le frecce `SU` e `GIU'` per muovere il paddle del Player 1
- Usa `W` e `S` per muovere il paddle del Player 2.
- Il gioco si basa sulle meccaniche classiche di Pong, con il primo giocatore che arriva a un punteggio predeterminato che vince (in questo caso continua finche' non viene chiuso manualmente).

## Struttura del Codice

- **Main**: Il codice principale dove vengono gestiti gli oggetti di gioco, il punteggio e gli eventi di gioco.
- **Paddle**: Gestisce il movimento dei paddle e la loro interazione con la palla.
- **Ball**: Gestisce il movimento e le collisioni della palla.
- **Funzioni**: Contiene le funzioni di supporto come la visualizzazione del punteggio.

## Funzionalità

- Grafica personalizzata per il campo di gioco e i paddle.
- Musica di sottofondo  (i suoni per le azioni verranno aggiunti in seguito).
- Gestione del punteggio e della partita.


## Licenza

Distribuito sotto la Licenza MIT. Vedi il file [LICENSE](LICENSE) per maggiori informazioni.
