import random 
ordlista = ["apelsiner","datorerna","fotbollen","solsystem","bibliotek","historien","människor","utbildning","skolbänke","blommorna","sommarlov","vintertid","färgglada","stranden","kärleksfull","flygplanen","glassbåtar","hästkrafter","vattenfall","brandmännen"]
word=random.choice(ordlista)

def Takeguess():
    while True:
        letter = input("Ange en gissning -> ").upper()
        if letter.isalpha() and len(letter) == 1:
            return letter
        else:
            print("Ogiltig gissning")