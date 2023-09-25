import os

'''
r - Read: apre il file per leggere, errore se non esiste
a - Append: apre il file per appendere(scrive alla fine), crea il file se non esiste
w - Write: apre il file pre scrivere(sovrascrive tutto il file), crea il file se non esiste
x - Create: crea il file, errore se esiste
'''

f  = open("text.txt", "r") #apriamo il file in lettura

#per visualizzare le differenze commentare gli altri perché quando si legge il "cursore" va avanti e se leggo tutto non mi legge più nulla
print(f.read())
print(f.read(5)) #numero di caratteri che vogliamo leggere in questo caso 5
print(f.readline())

for riga in f:
    print(riga)


f.close()

f = open("text.txt", "a")
f.write("Dentro scriviamo quello che vogliamo")
f.close()

f  = open("text.txt", "r")
print(f.read())
f.close()

f = open("creafile.txt", "w")
f.close()

os.remove("creafile.txt")

if(os.path.exists("prova.txt")):
    os.remove("prova.txt")
else:
    print("Non esiste un file con questo nome")

#os.rmdir("prova") cancella la cartella