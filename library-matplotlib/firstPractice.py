import matplotlib.pyplot as plt
import numpy
import random


# algoritma saya sendiri
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


# algoritma pak zaka
def lecturerWay():
    semester = [1, 2, 3, 4, 5, 6]
    ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]
    warna = ["#FF0000", "cyan", "blue", "magenta", "yellow", "#00FF00"]

    fig, ax = plt.subplots()
    ax.set_title("Index Prestasi Persemester")
    ax.set_ylabel("Semester")
    ax.set_xlabel("Nilai Index Prestasi")
    
    plt.bar(semester, ip, color=warna)


# eksperimen saya
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


# algoritma pak zaka, menampilkan pie
def pieWay():
    prodi = ["Sistem Informasi", "Informatika", "Psikologi"]
    jumlahMahasiswa = [145, 438, 186]

    plt.pie(jumlahMahasiswa, labels=prodi, autopct="%i Mahasiswa")


# algoritma saya, menggabungkan bar dan pie
def joinTheGame():
    # bar declaration
    semester = [1, 2, 3, 4, 5, 6]
    ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]
    warna = ["#FF0000", "cyan", "blue", "magenta", "yellow", "#00FF00"]
    plt.subplot(1, 2, 1)
    plt.bar(semester, ip, color=warna)

    # pie declaration
    prodi = ["Sistem Informasi", "Informatika", "Psikologi"]
    jumlahMahasiswa = [145, 438, 186]
    plt.subplot(1, 2, 2)
    plt.pie(jumlahMahasiswa, labels=prodi, autopct="%i Mahasiswa")


# algoritma pak zaka, menggabungkan bar dan pie
def lecturerJoinWay():
    # bar declaration
    semester = [1, 2, 3, 4, 5, 6]
    ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]
    warna = ["#FF0000", "cyan", "blue", "magenta", "yellow", "#00FF00"]

    # pie declaration
    prodi = ["Sistem Informasi", "Informatika", "Psikologi"]
    jumlahMahasiswa = [145, 438, 186]
    
    # start process
    fig, ax = plt.subplots(1, 2)

    # bar label
    ax[0].set_title = "Grafik Batang Indeks Prestasi"
    ax[0].set_xlabel = "Semester ke-"
    ax[0].set_ylabel = "Nilai Indeks Prestasi"

    # pie label
    ax[1].set_title = "Grafik Pie Jumlah Mahasiswa"

    # set it up
    ax[0].bar(semester, ip)
    ax[1].pie(jumlahMahasiswa, labels=prodi, autopct="%i Mahasiswa")


# bar declaration
semester = [1, 2, 3, 4, 5, 6]
ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]
warna = ["#FF0000", "cyan", "blue", "magenta", "yellow", "#00FF00"]

# plot declaration
month = ["Jan", "Feb", "Mar", "Apr", 'May', "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
sellPoint = [10, 30, 60, 75, 40, 30, 10, 20, 100, 120, 90, 70]

# pie declaration
prodi = ["Sistem Informasi", "Informatika", "Psikologi"]
jumlahMahasiswa = [145, 438, 186]

# declare our figure and axes
fig, ax = plt.subplots(3, 3)

# show the result
ax[0, 0].bar(semester, ip)
ax[1, 1].plot(month, sellPoint)
ax[2, 2].pie(jumlahMahasiswa, labels=prodi, autopct="%i Mahasiswa")

# disappear the blank one
ax[0, 1].pie([0]); ax[0, 2].pie([0])
ax[1, 0].pie([0]); ax[1, 2].pie([0])
ax[2, 0].pie([0]); ax[2, 1].pie([0])

# show the result
plt.show()
