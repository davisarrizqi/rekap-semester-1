import mysql.connector
from mysql.connector import connect, Error

try:
    db = connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "toko"
    ); print("Berhasil terhubung!"); cursor = db.cursor()
except Error as e: print(e)

class DatabaseCenter():
    def __init__(self, database,  cursorDatabase) -> None:
        self.cursorDatabase = cursorDatabase

    def insertData(self):
        self.cursorDatabase.execute("INSERT INTO BARANG VALUES(10102020, 'CONTOH SAMPLE', 2003)")
        self.database.commit()

    def readData(self):
        self.cursorDatabase.execute("SELECT * FROM BARANG")
        print(self.cursorDatabase.fetchall())

    def deleteData(self):
        self.cursorDatabase.execute("DELETE FROM BARANG WHERE ")

def tryToStart():
    myDatabase = DatabaseCenter(db, cursor)
    myDatabase.insertData()
    myDatabase.readData()


# --------------------------------------------------------------------------------------------------------- #


def koneksi():
    koneksiDatabase = None
    try:
        koneksiDatabase = connect(
            host="localhost",
            user="root",
            passwd="",
            database="toko"
        ); print("Berhasil terkoneksi dengan database!")
    except Error as e: print(e)
    return koneksiDatabase


def tampilData(conn):
    query = "SELECT * FROM BARANG"
    with conn.cursor() as cur:
        cur.execute(query)
        result = cur.fetchall()
        for row in result: print(row)

if __name__ == '__main__':
    # tampilData(koneksi())
    pass
