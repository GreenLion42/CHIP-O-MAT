#    ▄████▄   ██░ ██  ▐██▌  ██▓███   ▒█████   ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓
#   ▒██▀ ▀█  ▓██░ ██▒ ▐██▌ ▓██░  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒
#   ▒▓█    ▄ ▒██▀▀██░ ▐██▌ ▓██░ ██▓▒▒██░  ██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░
#   ▒▓▓▄ ▄██▒░▓█ ░██  ▓██▒ ▒██▄█▓▒ ▒▒██   ██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ 
#   ▒ ▓███▀ ░░▓█▒░██▓ ▒▄▄  ▒██▒ ░  ░░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ 
#   ░ ░▒ ▒  ░ ▒ ░░▒░▒ ░▀▀▒ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   
#     ░  ▒    ▒ ░▒░ ░ ░  ░ ░▒ ░       ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░   ░    
#   ░         ░  ░░ ░    ░ ░░       ░ ░ ░ ▒  ░      ░     ░   ▒    ░      
#   ░ ░       ░  ░  ░ ░                 ░ ░         ░         ░  ░  v0.1       by GreenLion42  
#
#   CH!P-O-MAT ist ein Programm zum automatisierten einfügen von selbsterstellten Playlists aufs einer ".txt" Datei
#   v0.1

import pyautogui as pg
import time


time.sleep(10)      # Wartet 10 Sekunden bevor er startet die Playlist ins Eingabefeld zu schreiben

txt = open("playlist.txt", "r")     # wählt die .txt Datei aus und 
pre = "ch!p"                        # definiert das Prefix das vor den Songtitel gesetzt wird 


for i in txt:                       
    pg.write(pre+' '+i)             # Schreibt das Prefix + den Songtitel in das ausgewählte Feld
    pg.press('Enter')               # Bestätigt die Eingabe mit drücken von 'Enter'
    time.sleep(0.5)                 # Wartet 0.3 Sekunden bevor er den nächsten Song einfügt um Problemen vorzubeugen 