# Grupp-projekt-Oskar-Hampus-Albin-Folke
Grupp övningar

5 november

Oskar 
började skriva om strukturen på hänga gubbe för att använda klasser och enums för att göra det mera lättläst och lättarbetat.

Albin
påbörjade stenSaxPåse samt skapade hänga gubbe

Hampus
Förtydligade några input satser i sten sax påse spelet.

9 november

Albin
gjorde ungefär halva mastermind

Oskar
Skrev färdigt sten sax påse spelet, Det använder enums för att koppla ihop värden logisk med klasser för att hålla de olika
handlingarna lättlästa och organiserade. Har fortfarande små saker som bättre formatering vid utskrifter, bättre variabel namn och möjligvis byta ut klasserna som håller handlingarna till structs/dataclass men ska först kolla mer på hur dem beter sig i python.

Hampus
började med ordgissningsspelet aka hänga gubbe. Skapade en lista med ord på 9 bokstäver. gjorde så att det slumpades fram ett random ord wrån listan, sedan gjorde jag en funktion som kollade om det var en bokstav. Slutligen kollade om det fanns i ordet.
Började på spelloopen

12 november

Oskar
Jag skrev färdigt sten sax påse och hänga gubbe
Sten sax påse var funktionellt innan idag. jag mest lade till några docstrings och bytte ut klasserna till frozen dataclass.
Jag har bara skrivit språk i C familjen så som jag tolkade det var en frozen dataclass det närmaste man kom till en static struct.
Jag skrev färdigt logiken i hänga gubbe så att den är funktionell. Den använder hashsets för att hålla tidskomplexiteten linjär oavsett mängden gissningar. Samt så använder jag mig av regex för att substitionera tecken man inte ville ha i utskrifterna.