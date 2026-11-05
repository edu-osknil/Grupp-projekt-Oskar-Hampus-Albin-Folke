import random as rand

SSP=["sten","sax","påse"]
namn=input("Namn: ")
try:
    ggr=int(input("Antal omgångar: "))
except:
    print("Felaktig inmatning, skriv ett tal")
for i in range(ggr):
    valStr=0
    while not valStr in SSP:
        valStr=input("Välj 'Sten', 'Sax' eller 'Påse': ")
    datorStr=SSP[rand.randint(0,2)]
    if datorStr==valStr:
        print("Oavgjort")
    else:
        print(SSP.index(val))