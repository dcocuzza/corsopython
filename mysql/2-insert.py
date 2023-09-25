import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pysql"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clienti(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), cognome VARCHAR(255));")

cursor.execute("show tables;")
for x in cursor:
    print(x)

sql = "INSERT INTO clienti(nome, cognome) VALUES (%s, %s)"
values = ("Luca", "Rossi")
cursor.execute(sql, values)
db.commit()
print("id ultima riga inserita: ", cursor.lastrowid)

values = [
    ("Marco", "Verdi"),
    ("Paolo", "Marrone"),
    ("Giovanni", "Viola")
]
cursor.executemany(sql, values)
db.commit()
