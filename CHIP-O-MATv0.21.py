#    ▄████▄   ██░ ██  ▐██▌  ██▓███   ▒█████   ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓
#   ▒██▀ ▀█  ▓██░ ██▒ ▐██▌ ▓██░  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒
#   ▒▓█    ▄ ▒██▀▀██░ ▐██▌ ▓██░ ██▓▒▒██░  ██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░
#   ▒▓▓▄ ▄██▒░▓█ ░██  ▓██▒ ▒██▄█▓▒ ▒▒██   ██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ 
#   ▒ ▓███▀ ░░▓█▒░██▓ ▒▄▄  ▒██▒ ░  ░░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ 
#   ░ ░▒ ▒  ░ ▒ ░░▒░▒ ░▀▀▒ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   
#     ░  ▒    ▒ ░▒░ ░ ░  ░ ░▒ ░       ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░   ░    
#   ░         ░  ░░ ░    ░ ░░       ░ ░ ░ ▒  ░      ░     ░   ▒    ░      
#   ░ ░       ░  ░  ░ ░                 ░ ░         ░         ░  ░  v0.21   by GreenLion42  
#
#   CH!P-O-MAT ist ein Programm zum automatisierten einfügen von 
#   selbsterstellten Playlists aus einer ".txt" Datei mit GUI.
#   v0.21


from importlib.resources import path
from tkinter import *
from tkinter import filedialog as fd
import pyautogui as pg
import time


def openFile():
    global filepath
    filepath = fd.askopenfilename(title = "Wähle Playlist", filetypes=(("text files", "*.txt"),("all Files","*.*")))
    print(filepath)

def CheckShuffle():
    cb1_l1 = Label(window, text=var1.get()).grid(row=7, column=0)
    print(var1.get())


def runCode():
    time.sleep(10)      # Wartet 10 Sekunden bevor er startet die Playlist ins Eingabefeld zu schreiben

    print(filepath)
    txt = open(filepath, "r")     # öffnet die ausgewählte Playlist
    pre = "ch!p"                        # definiert das Prefix das vor den Songtitel gesetzt wird 

    for i in txt:                       
        pg.write(pre+' '+i)             # Schreibt das Prefix + den Songtitel in das ausgewählte Feld
        pg.press('Enter')               # Bestätigt die Eingabe mit drücken von 'Enter'
        time.sleep(0.5)                 # Wartet 0.3 Sekunden bevor er den nächsten Song einfügt um Problemen vorzubeugen 
        
    if var1.get() == "  Aktiviert  ":
        time.sleep(1.5)
        pg.press('Enter')
        time.sleep(1.5)
        pg.write("ch!shuffle")
        time.sleep(1)
        pg.press('Enter')
        print("Es lebt")
        window.destroy
    elif var1.get() == "Deaktiviert" :
        print("es lebt nicht")
        window.destroy


window = Tk() 

window.iconbitmap('kenny.ico')

# Logo- einbetten
Logo =  PhotoImage(file="chip.png")
label0  = Label(window, image=Logo).grid(row=0, column=0)

# Titel des Tkinter Fensters
window.title('Willkommen bei CH!P-O-MAT')
window.geometry('480x500')    # Größe der Tkinter Fensters

# Playlist Auswahl
label1 = Label(window, text="Wähle die Playlist die du einfügen willst:", fg="orange", bg="black")
label1.grid(row=2, column=0)
button = Button(text="Playlist auswählen", command=openFile)
button.grid(row=3, column=0)

# Zusätzliche Optionen
label5 = Label(window, text="Möchtest du den Shuffle-mode aktivieren ?", fg="orange", bg="black")
label5.grid(row=5, column=0)

var1 =  StringVar()
cb1 = Checkbutton(text="Shuffle-Mode", variable=var1, onvalue="  Aktiviert  ", offvalue="Deaktiviert", command=CheckShuffle )
cb1.deselect()
cb1.grid(row=6, column=0)

# bestätigt die Auswahl und startet den Countdown
button1 = Button(text="Bestätigen", command=runCode,)
button1.grid(row=8, column=0)

# Beendet das Programm vorzeitig
button2 = Button( text="Abbrechen", command=window.destroy, width=10)
button2.grid(row=9, column=0)



window.mainloop()