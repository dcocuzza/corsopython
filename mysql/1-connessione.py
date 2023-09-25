import mysql.connector

'''
per la connssione al database

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "nome_db"
)
cursor = db.cursor()
cursor.execute("Show tables;")
print(cursor.fetchAll())
'''

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)
print(db)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS pysql;")

cursor.execute("SHOW DATABASES;")
for x in cursor:
    print(x)


