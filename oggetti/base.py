class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("Ciao sono: ", self.nome)

persona1 = Persona("Luca", "Rossi")
persona2 = Persona("Marco", "Verdi")
print(persona2.nome)

persona2.nome = "Maria"
persona2.saluta()

del persona2.nome #cancella il nome della persona2

persona2.nome = "Maria"
persona2.saluta()

del persona2 #cancella l'oggetto