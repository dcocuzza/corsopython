peso = 65
altezza = 176
eta = 25

frase = "Ciao sono Luca e sono alto {} cm"
frase2 = "Ciao sono Luca e sono alto {:.2f} cm" #2 cifre decimali
print(frase.format(altezza))
print(frase2.format(altezza))

frase3 = "Ciao sono Luca, ho {} anni, peso {}, e sono alto {}"
print(frase3.format(eta, peso, altezza))

frase4 = "Ciao sono Luca, ho {0} anni, peso {1}, e sono alto {2:.2f}, e faccio {0}" #metto gli indici che corrispondono all'ordine dei parametri
print(frase4.format(eta, peso, altezza))

frase5 = "Ciao sono Luca, ho {eta} anni, peso {peso}, e sono alto {altezza}" #indici nominali, possiamo metterli
print(frase5.format(eta=45, peso=65, altezza=176))
print(frase5.format(eta=eta, peso=peso, altezza=altezza))