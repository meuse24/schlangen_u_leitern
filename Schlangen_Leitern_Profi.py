#########################################################################################################################
# Spiel Schlangen und Leitern  -  01.05.2023 (c) GMeu                                                                   #
# 2 Spieler würfeln abwechselnd. Dann fahren sie ihre Spielfiguren die entsprechende Anzahl von Feldern vorwärts.       #
# Wenn im Zielfeld eine Umleitung (Schlange oder Leiter) besteht, fahren sie dorthin, sonst bleiben sie im Zielfeld.    #
# Der Spieler, der als erstes über die Ziellinie (100) kommt, hat gewonnen.                                             #
#########################################################################################################################

def printBoard(p):      # Spielfeld ausgeben, rows sind die range-Werte der 10 Zeilen, abwechselnd vorwärts und rückwärts
    rows = [ (1,11,1),(20,10,-1),(21,31,1),(40,30,-1),(41,51,1),(60,50,-1),(61,71,1),(80,70,-1),(81,91,1),(100,90,-1) ]
    vLINE  = Style.DIM + Fore.BLACK + Back.WHITE + " " + RESET      # Vertikal-Balken 
    hLINE = {-1:vLINE*83+" "*7+vLINE , 1:vLINE+" "*7+vLINE*83}      # Horizontal-Balken rechts offen und links offen
    p=[min(pos,100) for pos in p]                                   # Spielerpositionen korrigieren, wenn Spieler über Endposition
    os.system('cls' if os.name == 'nt' else 'clear')                # Bildschirm löschen
    print(f"{Fore.BLACK+Back.WHITE}               S  C  H  L  A  N  G  E  N     U  N  D     L  E  I  T  E  R  N               {RESET}")
    for row in reversed(rows):                                      # Schleife für Zeilen (row beinhaltet die range-Werte der einzelnen Zeilen)
        for col in range(row[0] , row[1] , row[2]):                 # Schleife für die Felder in einer einzelne Zeile
            if col==p[0]==p[1]: f = f"{vLINE}{plCOLOR[0]}{Style.BRIGHT}{col:3} SP1{plCOLOR[1]}2{RESET}" # Spieler 1 und 2 auf gleicher Pos
            elif col==p[0]    : f = f"{vLINE}{plCOLOR[0]}{Style.BRIGHT}{col:3} SP1 {RESET}"             # Feld Spieler 1
            elif col==p[1]    : f = f"{vLINE}{plCOLOR[1]}{Style.BRIGHT}{col:3} SP2 {RESET}"             # Feld Spieler 2 
            elif col==100     : f = f"{vLINE}{Style.BRIGHT}END     "                                    # Feld 100 = END
            else              : f = f"{vLINE}{Style.BRIGHT}{col:3}{Style.DIM}{diversions.get(col,'    '):4} {RESET}" # Feld mit Umleitung
            print (f,end="")                                        # ein Feld zeichnen
        print(vLINE)                                                # abschließender vertikaler Balken der Zeile und Zeilenvorschub
        print(f"{hLINE[row[2]]}")                                   # abhängig von vorwärts oder rückwärts den links oder rechts offenen Balken zeichnen

###  Beginn des Hauptprogramms   ####
import os,random
try: from colorama import init, Back, Fore, Style
except ModuleNotFoundError as e: print(f"Bitte zuerst das fehlende Modul mit 'pip install colorama' in der Konsole installieren ({e}).")
else:
    diversions = {5:26,18:39,24:82,25:3,28:51,35:9,47:85,48:12,68:89,77:97,78:42,87:46,94:57} # Umleitungen
    init()                                                              # Colorama initialisieren
    plCOLOR,RESET = (Back.RED+Fore.BLACK, Back.GREEN+Fore.BLACK),Style.RESET_ALL # Colorama-Konstanten für Spielerfarben u Reset
    pos,player = [1,1], 0                                               # Start-Pos der Spieler 1 und 2 auf den Spielfeld, Sp1 ist dran (0=Sp1, 1=Sp2)
    printBoard(pos)                                                     # Spielfeld ausgeben
    while all(p < 100 for p in pos):                                    # Spielschleife solange nicht ein Spieler im Ziel also unter 100 ist
        input(f"\n{Style.BRIGHT}{plCOLOR[player]}Spieler {player+1}{RESET}: Zum Würfeln Eingabetaste drücken!  ")
        rnd,oldPos  = random.randint(1,6) , pos[player]                 # würfeln u alte Position merken (für die Ausgabe der Spielzugbeschreibung)
        pos[player] = diversions.get(pos[player]+rnd , pos[player]+rnd) # neue Position, prüfen, ob Umleitung und dem aktuellen Spieler zuweisen
        printBoard(pos)                                                 # Spielfeld ausgeben und Spielzugbeschreibung
        print(f"\nDer {Style.BRIGHT}{plCOLOR[player]}Spieler {player+1}{RESET} hat an der Position {plCOLOR[player]}{oldPos}{RESET} die Zahl {plCOLOR[player]}{rnd}{RESET} gewürfelt und ist jetzt an der Position {plCOLOR[player]}{pos[player]}{RESET}.")
        player = 1 if player == 0 else 0                                # Anderer Spieler ist dran, aus 0 wird 1 und umgekehrt
    printBoard(pos)                                                     # Spiel ist fertig - Spielfeld ausgeben und Siegesmeldung
    print(f"\nDer {Style.BRIGHT}{plCOLOR[int(not player)]}Spieler {int(not player)+1}{RESET} ist im Ziel und hat gewonnen !!!\n")  # Siegesmeldung