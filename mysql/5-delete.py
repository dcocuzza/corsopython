import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pysql"
)
cursor = db.cursor()

sql = "DELETE FROM clienti WHERE nome = 'Marco'"
cursor.execute(sql)
db.commit()

print("Numero di righe cancellate: ", cursor.rowcount)

sql = "DELETE FROM clienti WHERE nome = %s"
valore = ("Paolo", ) #si mette le virgola perché deve essere una tupla
cursor.execute(sql, valore)
db.commit()

print("Numero di righe cancellate: ", cursor.rowcount)

sql = "DELETE FROM clienti WHERE nome = %s AND cognome = %s"
valore = ("Paolo", "Gialli") 
cursor.execute(sql, valore)
db.commit()

print("Numero di righe cancellate: ", cursor.rowcount)
