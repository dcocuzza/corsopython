class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("Ciao sono: ", self.nome)

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def saluta(self):
        print("Buongiorno sono: ", self.nome, " ", self.cognome)

    def dai_voto(self):
        print("Bravo, un bel 8")

persona1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Marco", "matematica")

persona1.saluta()
insegnante1.saluta()
print(insegnante1.materia)
insegnante1.dai_voto()
