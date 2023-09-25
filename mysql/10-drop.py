import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pysql"
)
cursor = db.cursor()    

cursor.execute("CREATE TABLE IF NOT EXISTS temporanea(id INT AUTO_INCREMENT PRIMARY KEY, nome_colonna VARCHAR(255), secondo_nome VARCHAR(255));")

sql = "DROP TABLE IF EXISTS temporanea"
cursor.execute(sql)