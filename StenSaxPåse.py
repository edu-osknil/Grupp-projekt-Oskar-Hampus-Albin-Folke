import random as rand
from enum import Enum
from dataclasses import dataclass

class Moves(Enum):
    Rock = 0
    Scissor = 1
    Paper = 2

@dataclass (frozen=True)
class Scissor():
    win = Moves.Paper
    loss = Moves.Rock

@dataclass (frozen=True)
class Paper():
    win = Moves.Rock
    loss = Moves.Scissor

@dataclass (frozen=True)
class Rock():
    win = Moves.Scissor
    loss = Moves.Paper

val = {"Scissor" : Scissor, "Paper" : Paper, "Rock" : Rock}
playerName=input("Ange ditt spelarnamn -> ")

def GetRounds():
    '''Take a number from the user'''
    while True:
        try:
            return(int(input("Ange antal omgångar som ska spelas: ")))
        except:
            print("Felaktig inmatning, skriv ett tal")

def GetAction():
    '''Take action from user'''
    while True:
        action = input("Välj handling (Rock/Scissor/Paper)").lower()
        if action in val:
            return val[action]
        else:
            print("Ogilltig handling")

def PrintState(winning):
    '''Print the current scoreboard'''
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
    computerAction = rand.choice(list(Moves))
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