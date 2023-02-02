import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306, database="dbtestowa")

cursorObject = db.cursor()
tblstudent = "CREATE TABLE IF NOT EXISTS student(name VARCHAR(60) NOT NULL,lastname VARCHAR(60) NOT NULL,idstudent int NOT NULL);"

cursorObject.execute(tblstudent)
db.close()
