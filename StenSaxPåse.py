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

def PrintState(winning):
    pythonState = f"Python: {loss:>5}"
    playerState = f"{playerName}: {win:>5}"
    upper = playerState if winning else pythonState
    lower = pythonState if winning else playerState
    print(f"\nStällning\n{'-' * 20}")
    print(upper)
    print(f"{lower}\n")

win = 0
loss = 0
rounds = GetRounds()
for i in range(rounds):
    action = GetAction()
    computerAction = rand.choice(list(Drag))
    if action.win == computerAction:
        print(f"Python valde {computerAction.name}, du vann!")
        win += 1
    elif action.loss == computerAction:
        print(f"Python valde {computerAction.name}, du förlorade!")
        loss += 1
    else:
        print(f"Python valde {computerAction.name}, Oavgjort!") 
    PrintState(win > loss)


PrintState(win > loss)
if win > loss:
    print(f"{playerName} vann")
elif loss > win:
    print("Python vann")
else:
    print("oavgjort")