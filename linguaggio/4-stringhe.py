name = "Jack"
name = "Ciao " + name
print(name)

messaggio = "Fate il vostro gioco"
print(messaggio.startswith("Fate"))
print(messaggio.startswith("F"))
print(messaggio.startswith("x"))

print(messaggio.endswith("gioco"))
print(messaggio.endswith("gioca"))

spam = "asD123"
eggs = "999"
bacon = "    "
monty = "PokEr "
print(spam.isalpha()) #torna falso perché ci sono anche numeri
print(spam.isalnum())
print(eggs.isdecimal())
print(monty.isspace()) #torna false perché sepput presente uno spazio non ha soltanto spazi
print(bacon.isspace())

print(monty.lower())
print(spam.upper())

to_do = ["portare il cane a passeggio", "finire di studiare", "fare la spesa"]
ris = ", ".join(to_do)
print(ris)
ris = "\n".join(to_do)

print()

print(ris)

citazione = "Nel mezzo del cammin di nostra vita..."
lista = citazione.split(" ")
print(lista)

mystr = "spam, eggs, bacon spam"
mylist = ["spam", "spam", "spam"]
print(len(mystr))
print(len(mylist))

print()

print("bacon" in mylist)
print("s" in mystr)
print("sp" in mystr)
print("s" in mylist)
print("eggs" not in mylist)

print()

alfa = "abcdefghikjklm..."
dots = alfa[-3:]
print(dots)
alfa = alfa[:-3]
print(alfa)

alnum = "djoi3u4nuqnrou01u3m3mdasd"
m = "d"
count = 0

print()

for char in alnum: #è come un foreach char assume ad ogni ciclo un carattere della stringa dall'inizio alla fine
    print("for: ", char)
    if char == m:
        count += 1

print()
print("count: ", count)




