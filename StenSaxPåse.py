import random as rand
from enum import Enum

class Drag(Enum):
    sten = 0
    sax = 1
    påse = 2

class Sax():
    win = Drag.påse
    loss = Drag.sten
    tie = Drag.sax

class Påse():
    win = Drag.sten
    loss = Drag.sax
    tie = Drag.påse

class Sten():
    win = Drag.sax
    loss = Drag.påse
    tie = Drag.sten

val = {"sax" : Sax, "påse" : Påse, "sten" : Sten}

playerName=input("Ange ditt spelarnamn -> ")

def GetRounds():
    while True:
        try:
            return(int(input("Ange antal omgångar som ska spelas: ")))
        except:
            print("Felaktig inmatning, skriv ett tal")

def GetAction():
    while True:
        action = input("Välj handling (sten/sax/påse)").lower()
        if action in val:
            return val[action]
        else:
            print("Ogilltig handling")
win = 0
loss = 0
logicScore = 0
rounds = GetRounds()
for i in range(rounds):
    action = GetAction()
    computerAction = rand.choice(list(Drag))
    if action.win == computerAction:
        print(f"Python valde {computerAction.name}, du vann!")
        win += 1
        logicScore += 1
    elif action.loss == computerAction:
        print(f"Python valde {computerAction.name}, du förlorade!")
        loss += 1
        logicScore -= 1
    else:
        print(f"Python valde {computerAction.name}, Oavgjort!") 
    print(f"ställningen är {win}, {loss} ", end="")
    if logicScore == 0:
        print("oavgjort")
    elif logicScore >= 0:
        print(f"till {playerName}")
    else:
        print("till Python")
    print("\n")

if logicScore == 0:
    print("oavgjort")
elif logicScore >= 0:
    print(f"{playerName} vann")
else:
    print("Python vann")