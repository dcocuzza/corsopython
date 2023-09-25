import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pysql"
)

cursor = db.cursor()

sql = "SELECT * FROM clienti"
cursor.execute(sql)
result = cursor.fetchall() #ritorna tutte le righe

for riga in result:
    print(riga)

print()

cursor.execute(sql)
result = cursor.fetchone() #ritorna solo la prima riga

for riga in result:
    print(riga)

print(result)
print()

cursor.reset() #se non lo metto mi dice che ci sono dati non letti

sql = "SELECT nome, cognome FROM clienti"
cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga)

print()

sql = "SELECT nome, cognome FROM clienti WHERE nome = 'Marco'"
cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga)