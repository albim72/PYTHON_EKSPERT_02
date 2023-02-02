import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306, database="dbtestowa")

cursorObject = db.cursor()
print("wstawienie danych do tabeli")
sql = "INSERT INTO student(name,lastname,idstudent) VALUES(%s,%s,%s);"
val1 = ("Anna","Kot",43435)

vallist = [
    ("Olga","Nowak",74566456),
    ("Olaf","Nowik",123424),
    ("Nadia","Kowal",785665),
    ("Tomasz","Kot",43543),
    ("Maria","Kos",7857656),
]

cursorObject.execute(sql,val1)
#db.commit()
print(f'dodano do tabeli -> {cursorObject.rowcount} wierszy')
cursorObject.executemany(sql,vallist)
#db.commit()
print(f'dodano do tabeli -> {cursorObject.rowcount} wierszy')

db.close()
