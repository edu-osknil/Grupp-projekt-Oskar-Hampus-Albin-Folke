import random 
ordlista = ["apelsiner","datorerna","fotbollen","solsystem","bibliotek","historien","människor","utbildning","skolbänke","blommorna","sommarlov","vintertid","färgglada","stranden","kärleksfull","flygplanen","glassbåtar","hästkrafter","vattenfall","brandmännen"]
word=random.choice(ordlista)
incorrectHash = {}


print("Du ska gissa ett ord, bokstav för bokstav, på 9 bokstäver")

def Takeguess():
    while True:
        letter = input("Ange en gissning -> ").upper()
        if letter.isalpha() and len(letter) == 1:
            return letter
        else:
            print("Ogiltig gissning")

def Compareword(letter):
    for i in range(word):
        if word[i] == letter:
            return i
    incorrectHash.append(letter)
    return -1



