persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

operazioni = ("aggiungere", "modificare", "eliminare")

def start():
    operazione = input("Cosa vuoi fare?")
    if operazione == operazioni[0]:
        x = input("aggiungi chiave valore separati da una virgola")
        aggiungi(x.split(","))
    elif operazioni == operazioni[1]:
        pass
    elif operazioni == operazioni[2]:
        pass

def aggiungi(param):
    chave = param[0]
    valore = param[1]
    persona[chave] = valore
    print(persona)

while True:
    start()