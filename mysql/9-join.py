import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pysql"
)
cursor = db.cursor()

sql = "SELECT \
    clienti.nome, cognome, citta.nome \
    FROM clienti \
    INNER JOIN citta ON clienti.id_citta = citta.id"

cursor.execute(sql)
result = cursor.fetchall()
for riga in result:
    print(riga)