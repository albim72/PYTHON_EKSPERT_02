import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306, database="dbtestowa")

cursorObject = db.cursor()

query = "SELECT idstudent,name,lastname FROM student WHERE idstudent > 100000"
cursorObject.execute(query)

wynik = cursorObject.fetchall()
for x in wynik:
    print(x)

db.close;
