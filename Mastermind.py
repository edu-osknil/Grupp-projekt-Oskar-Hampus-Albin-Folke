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
Svårare nivå: Det kan finnas upprepningar av en eller flera siffror""")
    
def dif(): #ändrar "ans" beroende på svar, säker inmatning
    global ans
    while True:
        try:
            ans=int(input("Ange önskad nivå: lättare (1), svårare (2) -> "))
            if ans==1 or ans==2:
                break
            else:
                print("Ogiltig svårighet")
        except:
            print("Felaktig inmatning, skriv en siffra")

def codeGen(): #genererar en kod beroende på om den globala variabeln "ans" är 1 eller 2
    num=list(range(1,7))
    code=[]
    for i in range(4):
        if ans==1:
            code.append(str(num[rand.randint(0,5-i)]))
        elif ans==2:
            code.append(rand.randint(1,6))
    return "".join(code)

def feedback(a): #tar emot en gissning och lägger till feedback i listan "feedback"
    for i in range(4):
        if a[4]==code[4]:
            print("✓")
    
    for i in a:
        if i in codeList:
            print("▢")

def guess(a, b): #tar in en gissning (a) samt en plats (b)
    global guesses
    guesses.insert(b-1, a)
    
    #printar loggen och utgår ifrån listan guesses
    print("""Drag #    Drag        Feedback
-------------------------------------------""")
    
    #printar numrerade gissningar
    for i in range(12,0,-1):
        print(f"\n{i:<4}",end="")
        try:
            print(f"{guesses[i-1].split(" "):<10}",end="")
        except IndexError:
            pass
        try:
            print(feedback[i-1])
        except IndexError:
            pass

def play():
    intro()

    while True:
        guesses=[]
        
        dif()
        codeGen()
        
        for i in range(1,13):
            while True:
                guess=input("Ange gissning som följd av fyra siffror --> ")
                if len(guess)!=4 or not guess.isdigit():
                    print("Din gissning är felaktig")
            feedback(guess)
            guess(guess,i)
            if guess==code:
                print("Snyggt ;-)")
                break
        
        retry=input("Vill du spela igen (j/n) --> ")
        if retry=="j":
            continue
        elif retry=="n":
            break

    print("Programmet avslutade normalt")
