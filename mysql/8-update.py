import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pysql"
)
cursor = db.cursor()

sql = "UPDATE clienti SET nome = 'Geronimo' WHERE id = 12"
cursor.execute(sql)
db.commit()
print("Righe modificare: ", cursor.rowcount)

sql = "UPDATE clienti SET nome = %s WHERE id = %s"
valori = ("Gigio", 12)
cursor.execute(sql, valori)
db.commit()
print("Righe modificare: ", cursor.rowcount)