import random as rand
import enum

class Drag(enum):
    sten = 0
    sax = 1
    påse = 2

class Sax():
    vinst = Drag.påse
    förlust = Drag.sten
    oavgjort = Drag.sax

class Påse():
    vinst = Drag.sten
    förlust = Drag.sax
    oavgjort = Drag.påse

class Sten():
    vinst = Drag.sax
    förlust = Drag.påse
    oavgjort = Drag.sten

val = {"sax" : Sax, "påse" : Påse, "sten" : Sten}

namn=input("Ange ditt spelarnamn -> ")

def taOmgångar():
    while True:
        try:
            return(int(input("Ange antal omgångar som ska spelas: ")))
        except:
            print("Felaktig inmatning, skriv ett tal")

ggr = taOmgångar()
for i in range(ggr):
    valStr=0
    while not valStr in SSP:
        valStr=input("Välj 'Sten', 'Sax' eller 'Påse': ")
    datorStr=SSP[rand.randint(0,2)]
    if datorStr==valStr:
        print("Oavgjort")
    else:
        print(SSP.index(val))