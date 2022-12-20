import tkinter
import os
import random
import mysql.connector


class _Admin:
    def __init__(self):
        # set our connection
        self.koneksiDatabase = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='application_database'
        ); self.cursor = self.koneksiDatabase.cursor()

class DatabaseControl(_Admin):
    def __init__(self):
        super().__init__()

    def createTable(self, tableName, columnTotal):
        # declare and input it first
        eachColumn = [input(f"Column {data+1}'s Name : ") for data in range(columnTotal)]; print('')
        eachRules = [input(f"Column {data+1}'s Rules : ") for data in range(columnTotal)]; print('')
        myCommand = f'CREATE TABLE IF NOT EXISTS {tableName}('

        # start our proccess
        for data in range(columnTotal): myCommand += (eachColumn[data]+ " " +  eachRules[data] + ', ')
        myCommand = [myCommand[char] for char in range(len(myCommand)) if char != len(myCommand) - 2]
        myCommand.pop(); pivot=myCommand[::]; myCommand = '' 
        for data in pivot: myCommand += data; myCommand += ')'
        self.cursor.execute(myCommand); self.koneksiDatabase.commit()
        print("Tabel Berhasil Dibuat!")  # debug the result

    def readTable(self, tableName):
        self.cursor.execute(f"SELECT * FROM {tableName}")
        dataResult = self.cursor.fetchall(); 
        return dataResult

    def updateTable(self, tableName):
        myCommand = f'UPDATE {tableName} SET'


    def DataInsert(self, tableName):
        # declare it first
        myCommand = f"INSERT INTO {tableName} VALUES("
        self.cursor.execute(f'DESC {tableName}'); columnList = self.cursor.fetchall();
        
        # input our data
        columnList = [data[0] for data in columnList]; dataLength = len(columnList)
        dataList = [input(f"Input for {column.capitalize()} column : ") for column in columnList]
        dataList = [('"' + data + '"')  for data in dataList] 

        # proccess our data
        for data in dataList: myCommand += data + ', ' if data != columnList[-1] else data + ''
        if myCommand[-2] == ',': myCommand = myCommand[0:len(myCommand)-2]
        myCommand += ')'; self.cursor.execute(myCommand); self.koneksiDatabase.commit() 
        print("Berhasil Memasukkan Data!")




databaseControl = TryingPass()
databaseControl.tryPass()

# databaseControl.DataInsert("SAMPLE")

"""

window = tkinter.Tk()
window.configure(bg='gray')
window.geometry('500x500')

usernameText = tkinter.Text(window, font="Sans-Serif, 13")
usernameText.insert(tkinter.INSERT, "Username")
usernameText.pack()

window.mainloop()
"""
