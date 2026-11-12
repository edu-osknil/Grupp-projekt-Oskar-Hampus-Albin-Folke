import random 
import re

ordlista = ["apelsiner","datorerna","fotbollen","solsystem","bibliotek","historien","människor","utbildning","skolbänke","blommorna","sommarlov","vintertid","färgglada","stranden","kärleksfull","flygplanen","glassbåtar","hästkrafter","vattenfall","brandmännen"]
incorrectHash = set([])
correctHash = set([])

def Takeguess():
    '''Take a letter guess from user'''
    while True:
        letter = input("Ange en gissning -> ").upper()
        if not letter in incorrectHash and not letter in correctHash:
            if letter.isalpha() and len(letter) == 1:
                return letter
            else:
                print("Ogiltig gissning")
        else:
            print("Redan gissat")

def Compareword(letter, word):
    '''Checks if letter is correct'''
    for i in range(len(word)):
        if word[i] == letter:
            return i
    incorrectHash.add(letter)
    return -1

def PrintWord(word):
    '''Prints the currently found parts of the word'''
    currentStr = ""
    state = True
    for i in range(len(word)):
        if word[i] in correctHash:
            currentStr += word[i]
        else:
            currentStr += '*'
            state = False
    print(f"{currentStr}\n")
    return state

def PlayAgain():
    '''Takes a yes or no input'''
    while True:
        action = input("Spela igen (j/n)")
        if (action.lower() == 'j'):
            return True
        elif action.lower() == 'n':
            return False
        print("Ogilltig handling")

def GameLoop():
    '''Runs the game'''
    while True:
        incorrectHash.clear()
        correctHash.clear()
        word = random.choice(ordlista).upper()
        incorrectGuesses = 10
        print(f"Ett ord med {len(word)} bokstäver har valts.\nDu ska gissa det bokstav för bokstav.")
        while incorrectGuesses > 0:
            guess = Takeguess()
            guessState = Compareword(guess, word)
            if guessState == -1:
                incorrectGuesses -= 1
            else:
                correctHash.add(guess)
            print(f"Du har nu {incorrectGuesses} st. felgissningar kvar.")

            #regex pattern to find and replace {'} with nothing.
            print(f"Felgissningar: {re.sub(r"[{'}]", "", f"{incorrectHash}")}")
            correct = PrintWord(word)
            if correct:
                break
            elif incorrectGuesses == 0:
                print(f"ordet var {word}")
        if (not PlayAgain()):
            return

GameLoop()