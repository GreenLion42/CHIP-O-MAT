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

filepath = None

def openFile():
    global filepath
    filepath = fd.askopenfilename(title = "Wähle Playlist", filetypes=(("text files", "*.txt"),("all Files","*.*")))
    print(filepath) 
    label11 = Message(window, text=filepath, aspect= 640, justify=CENTER).place(x=30, y=160)
#  width=600, height=80

def CheckShuffle():
    cb1_l1 = Label(window, text=var1.get()).place(x=250, y=350)



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

        window.destroy

    elif var1.get() == "Deaktiviert" :

        window.destroy


window = Tk() 

window.iconbitmap('kenny.ico')

# Logo- einbetten
Logo =  PhotoImage(file="chip.png")
#label0  = Label(window, image=Logo).pack(x=20, y=5, width=200, height=30)

# Titel des Tkinter Fensters
window.title('Willkommen bei CH!P-O-MAT')
window.geometry('650x500')    # Größe der Tkinter Fensters

# Playlist Auswahl
label1 = Label(window, text="Wähle die Playlist die du einfügen willst:", fg="orange", bg="black")
label1.place(x=110, y=45)
button = Button(text="Playlist auswählen", command=openFile)
button.place(x=220, y=100)


# Zusätzliche Optionen
label5 = Label(window, text="Möchtest du den Shuffle-mode aktivieren ?", fg="orange", bg="black")
label5.place(x=80, y=250)

var1 =  StringVar()
cb1 = Checkbutton(text="Shuffle-Mode", variable=var1, onvalue="  Aktiviert  ", offvalue="Deaktiviert", command=CheckShuffle )
cb1.deselect()
cb1.place(x=220, y=300)

# bestätigt die Auswahl und startet den Countdown
button1 = Button(text="Bestätigen", command=runCode,)
button1.place(x=100, y=400)

# Beendet das Programm vorzeitig
button2 = Button( text="Abbrechen", command=window.destroy, width=10)
button2.place(x=400, y=400)



window.mainloop()