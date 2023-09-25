import json

x = '{"nome": "Luca", "cognome": "Rossi", "eta": 25}' #è una stringa
y = json.loads(x)
print(type(y))
print(y)
print(y["nome"])

a = { #è un dict
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25,
    "isOnline": False,
    "interessi": ["calcio", "basket"],
    "monetineInTasca": 4.56,
    "fidanzata": None\
}
print(a["cognome"])
b = json.dumps(a, indent=4, separators=(", ", ": "), sort_keys=True) #decidiamo come indentare e separare gli elementi, ordiniamo per ordine alfabetico
print(type(b))
print(b)