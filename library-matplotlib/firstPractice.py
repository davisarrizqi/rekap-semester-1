import matplotlib.pyplot as plt
import numpy
import random

def myWay():
    # part 1, declare it first
    semester = [1, 2, 3, 4, 5, 6]
    ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]

    # part 2, labelling
    plt.xlabel("Semester ke-")
    plt.ylabel("Nilai Indeks Prestasi")
    plt.title("Grafik Batang Indeks Prestasi")

    # part 3, styling
    listWarna = ["maroon", "dimgray", "slategrey", "midnightblue", "navy", "darkred", "darkorchid"]
    listWarnaDigunakan = []

    # now insert the color
    for color in range(len(semester)):
        listWarnaDigunakan.append(listWarna[random.randint(0, (len(listWarna) - 1))])

    # the last part, made it up
    plt.bar(semester, ip, color=listWarnaDigunakan)


def lecturerWay():
    semester = [1, 2, 3, 4, 5, 6]
    ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]
    warna = ["#FF0000", "cyan", "blue", "magenta", "yellow", "#00FF00"]

    fig, ax = plt.subplots()
    ax.set_title("Index Prestasi Persemester")
    ax.set_ylabel("Semester")
    ax.set_xlabel("Nilai Index Prestasi")
    plt.bar(semester, ip, color=warna)

def nextTrial():
    semester = [1, 2, 3, 4, 5, 6]
    ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]
    warna = ["#FF0000", "cyan", "blue", "magenta", "yellow", "#00FF00"]

    # add my own
    fig, myGraph = plt.subplots()
    myGraph.set_title("Data Selanjutnya")
    myGraph.set_ylabel("Garis Y")
    myGraph.set_xlabel("Garis X")
    plt.bar(semester, ip, color=warna)

def pieWay():
    prodi = ["Sistem Informasi", "Informatika", "Psikologi"]
    jumlahMahasiswa = [145, 438, 186]

    plt.pie(jumlahMahasiswa, labels=prodi, autopct="%i Mahasiswa")
