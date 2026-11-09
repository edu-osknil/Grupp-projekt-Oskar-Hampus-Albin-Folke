import random as rand

def intro():
    print("""Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.
Du ska försöka gissa denna kods siffror på max 12 drag.
Efter respektive gissning så kommer du att få en respons:
För varje gissad korrekt siffra på korrekt plats i koden: ✔
För varje gissad siffra på fel plats i koden: ▢
För de siffror som inte finns med i koden ges ingen markering.

Exempel: om den slumpade koden är 2315
och du gissar 3165
så blir responsen ✔▢▢

Du får välja mellan två svårighetsnivåer:
Lättare nivå: Alla siffror är garanterat olika
Svårare nivå: Det kan finnas upprepningar av en eller flera siffror""")
    
    ans=input("Ange önskad nivå: lättare (1), svårare (2) -> ")
    return ans

def codeGen():
    num=list(range(1,7))
    code=[]
    for i in range(4):
        if ans==1:
            code.append(str(num[rand.randint(0,5-i)]))
        elif ans==2:
            code.append(rand.randint(1,6))
    return "".join(code)



