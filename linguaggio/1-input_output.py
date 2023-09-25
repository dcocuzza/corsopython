testo = "Dante scrisse: \"Nel mezzo del cammin di nostra vita\""
print(testo)

eggs = "Meglio un uovo oggi..."
bacon = "o una gallina domani?"

testo = eggs + bacon
print(testo)

age = 30
stringa = "La mia età è: "
testo = stringa + str(age)
print(testo)

arancie = "13"
testo = int(arancie) * 13 #casting temporaneo dopo l'utilizzo arancie ritorna stringa
print(testo)

print("""prima
seconda
      teza""") #print multiriga

x = input()
print(x)

user_name = input("Tu come ti chiami? ")
print("Ciao " + user_name)

age = int(input("Quanti anni hai? ")) #qualsiasi valore preso in input sarà una stringa se vogliamo un int dobbiamo fare il cast
print(age)