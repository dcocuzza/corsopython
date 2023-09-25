#from random import * (importa tutte le funzioni di random)
from math import sqrt
from random import randint

age = 26
license = True

if age >= 18 and license == True:
    print("Puoi noleggiare una Ferrari")
elif age >= 19 and license == False:
    print("Sei senza patente")
else:
    print("Sei minorenne")

counter = 0
while counter <= 10:
    print(counter)
    counter += 1

print()

counter = 0
while license == True:
    counter += 1

    if counter % 2 == 0:
        print("Salto i numeri pari")
        continue

    if counter >= 10:
        print("Sto uscendo")
        break
    print(counter)

print("\nfor\n")

for numero in range(11): #la funzione range() inizia a contare da 0 e non include l'ultimo numero passato come parametro
    print(numero)

#range(start, stop, step)
#start = punto iniziale dell'intervallo
#stop = punto finale dell'intervallo
#step = passo di avanzamento

print("\nfor con 3 paramtri\n")

for numero in range(3, 11, 2): #il primo elemento è incluso, l'ultimo no, salta di 2
    print(numero)

print("\nfor con 3 paramtri\n")  

for numero in range(10, -1, -1): 
    print(numero)

print("\nGenerazione di numeri casuali\n")

for numero in range(10):
    val = randint(1, 50) #valori interi random compresi gli estremi 1 e 50
    print(val)

x = sqrt(25)
print("\nradice quadrata: \n", x)