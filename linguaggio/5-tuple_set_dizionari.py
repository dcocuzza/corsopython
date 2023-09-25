print()
#Tuple
my_tuple = (2, 5, 9, 13, 25)
my_tuple2 = 2, 3, 7

#accediamo agli elementi come nelle liste
#la differenza con la lista è che le tuple sono immutabili, non possiamo usare il metodo append() per aggiungere dei nuovi elementi
#non possiamo usare l'istruzione del, ... .

print(type(my_tuple))
print(type(my_tuple2))

print()
#Set
#i set sono un tipo di dato di Python che permette di creare collezioni di elementi e vengono definiti usand una coppia di {}
my_set = {"spam", "eggs", "bacon"}
my_set2 = {"spam", "eggs", "bacon", "spam"}

print(my_set)
print(my_set2)
my_set.add("poker")
print(my_set)


print()
#Dizionari
miodict = {"mia_chiave": "mio_valore", "age": 29, 3.14: "pi_greco", "primi": [2, 3, 5, 7]}
#coppia chiave-valore

print(miodict["mia_chiave"])
print(miodict[3.14])

miodict["mia_chiave"] = "miovalore"
print(miodict["mia_chiave"])

miodict["nuova chiave"] = "nuovo valore"
print(miodict["nuova chiave"])
print(miodict)

print()

#per verificare se una chiave è presente o meno all'interno di un dizionario possiamo usare gli operatori in e not in
a = "spam" in miodict
print(a)
a = "age" in miodict
print(a)
a = "mio_valore" in miodict
print(a) #ritorna false perché mio_valore è un valore e non una chiave

print()
#rimuovere un elementi da un dizionario, rimuove la coppia chiave-valore
del miodict["mia_chiave"]
print(miodict)

print()
#metodi del dizionario
ita_eng = {"ciao" : "hello", "arrivederci" : "goodbye", "uova" : "eggs", "gatto" : "cat", "arancia" : "orange"}
print(ita_eng.keys()) #ritorna tutte le chiavi del dizionario
print(ita_eng.values()) #ritorna tutti i valori presenti
print(ita_eng.items()) #ritorna le coppie chiave-valore rappresentare come tuple

#questi metodi non restituiscono semplici liste ma oggetti di tipo dict_key, dict_values e dict_items. Possiamo ottenere una lista
#da questi elementi

lista = list(ita_eng.items())
print(lista)

for chaive in ita_eng.keys():
    print(chaive)

print()
#get
a = ita_eng.get("spam", "chiave non presente") #valore ritornato se la chiave non è presente nel dizionario
print(a)
a = ita_eng.get("ciao", "chiave non presente")
print(a)
print(ita_eng)

print()
#setdefault
a = ita_eng.setdefault("birra", "bear") #se la chiave non è presente nel dizionario aggiunge la coppia chiave-valore nel dizionario
print(a)
print(ita_eng)
a = ita_eng.setdefault("ciao", "hi") #non viene aggiunto perché la chiave ciao è presente nel dizionario
print(a)
print(ita_eng)
