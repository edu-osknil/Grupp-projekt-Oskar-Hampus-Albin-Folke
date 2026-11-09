import random 
ordlista = ["apelsiner","datorerna","fotbollen","solsystem","bibliotek","historien","människor","utbildning","skolbänke","blommorna","sommarlov","vintertid","färgglada","stranden","kärleksfull","flygplanen","glassbåtar","hästkrafter","vattenfall","brandmännen"]
word=random.choice(ordlista)
incorrectHash = set([])


print("Du ska gissa ett ord, bokstav för bokstav, på 9 bokstäver")

def Takeguess():
    while True:
        letter = input("Ange en gissning -> ").upper()
        if letter.isalpha() and len(letter) == 1:
            return letter
        else:
            print("Ogiltig gissning")

def Compareword(letter):
    for i in range(len(word)):
        if word[i] == letter:
            return i
    incorrectHash.add(letter)
    return -1

incorrectGuesses = 10
while incorrectGuesses > 0:
    guess = Takeguess()
    guessState = Compareword(guess)
    if guessState == -1:
        incorrectGuesses -= 1
    print(f"Du har nu {incorrectGuesses} st. felgissningar kvar.")
    print(f"Felgissningar: {incorrectHash}")

