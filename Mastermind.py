import random as rand

def intro(): #printar startmeddelandet
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
Svårare nivå: Det kan finnas upprepningar av en eller flera siffror
""")
    
def dif(): #returnerar 1 eller 2 beroende på svar, säker inmatning
    while True:
        try:
            ans=int(input("Ange önskad nivå: lättare (1), svårare (2) -> "))
            if ans==1:
                return 1
            if ans==2:
                return 2
            else:
                print("Ogiltig svårighet")
        except:
            print("Felaktig inmatning, skriv en siffra")

def codeGen(ans): #genererar en kod beroende på om inmatningen är 1 eller 2
    num=[1,2,3,4,5,6]
    code=[]
    for i in range(4):
        if ans==1:
            code.append(str(num[rand.randint(0,6-i)]))
        elif ans==2:
            code.append(rand.randint(1,6))
    return "".join(code)

def giveFeedback(a): #tar emot en gissning och returnerar feedbacken
    retStr=[]
    global code
    for i in range(4):
        if a[i]==code[i]:
            retStr.append("✓")
    for i in a:
        if i in code:
            retStr.append("▢")
    return "".join(retStr)

def guessPrint(a): #tar in en gissning och printar loggen för alla gissningar
    global guesses
    guesses.append(a)
    
    #printar loggen och utgår ifrån listan guesses
    print("""
Drag #    Drag        Feedback
-------------------------------------------""")
    
    #printar numrerade gissningar
    for i in range(12,0,-1):
        print(f"\n{i:<4}",end="")
        try:
            print(f"{guesses[i-1].split(" "):<10}",end="")
        except:
            pass
        try:
            print(feedbacks[i-1])
        except IndexError:
            pass
        print()

def retry():
    while True:
        om=input("Vill du spela igen (j/n) --> ")
        if input=="j":
            return "j"


def play():
    intro()
    global code
    global guesses
    global feedbacks
    
    while True:
        won=0
        guesses=[]
        feedbacks=[]
        
        code=codeGen(dif())
        
        for i in range(1,13):
            while True:
                guess=input("\nAnge gissning som följd av fyra siffror --> ")
                if len(guess)==4 and guess.isdigit():
                    guesses.append(guess)
                    break
                else:
                    print("Din gissning är felaktig")
            feedbacks.append(giveFeedback(guess))
            guessPrint(guess)
            if guess==code:
                print("Du van!")
                won=1
                break
        
        if won==0:
            print(f"Du förlorade. Rätt kod var: {code}")
        
        
        
    print("Play() avslutades")
