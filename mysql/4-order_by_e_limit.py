import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pysql"
)

cursor = db.cursor()
sql = "SELECT * FROM clienti ORDER BY nome"
cursor.execute(sql)
result = cursor.fetchall()
for riga in result:
    print(riga)

print()

sql = "SELECT * FROM clienti ORDER BY nome LIMIT 2"
cursor.execute(sql)
result = cursor.fetchall()
for riga in result:
    print(riga)

print()
