import sqlite3
import hashlib

def getData(req):
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

def insertData(email, password):
    hashPassword = hashlib.md5(password.encode()).hexdigest()
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute("""INSERT INTO User(email, hashword) VALUES(?, ?)""", (email, hashPassword))
    con.commit()
    cursor.close()
    con.close()


# insertData("test@gmail.com", "Azerty0!")
print(getData("""SELECT * FROM User"""))
