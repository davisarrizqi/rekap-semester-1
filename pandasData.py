import pandas
import numpy

def latihanPertama():
    # membuat dataFrame
    data = [['Raehan', 85], ['Bobby', 90], ['Johana', 80]]
    data_frame = pandas.DataFrame(data, columns=["Nama", "Nilai1"])
    print(data_frame)

    # menambahkan kolom (series)
    my_column = [70, 85, 70]
    data_frame["Nilai2"] = pandas.Series(data=my_column)
    print(data_frame)

    # tambahkan kolom rata rata dan isi rata ratanya
    data_frame["Rata Rata"] = (data_frame["Nilai1"] + data_frame["Nilai2"])/2
    print(data_frame)

    # ubah Nilai2 milih johana menjadi 90
    data_frame["Nilai2"][2] = 90
    # data_frame["Nilai2"] = data_frame["Nilai2"].replace(90, 70)
    print(data_frame)

# data inserting
dataPenilaian = pandas.read_excel("Important Data/rekap_penilaian.xlsx")
# print(dataPenilaian) --> debug our result



#                              PERSOALAN


# 1. Tambahkan kolom full name hasil gabungan dari first name dan last name

# 2. Berapa nilai rata rata UAS dari data tersebut?

# 3. Tambahkan kolom nilai akhir dengan ketentuan:
    # Tugas 1 20%, Tugas 2 20%, UTS 25%, UAS 35%

# 4. Tambahkan kolom Nilai Huruf dengan ketentuan nilai akhir:
    # Lebih dari sama dengan 81, A
    # Lebih dari sama dengan 61, B
    # Lebih dari sama dengan 41, C
    # Lebih dari sama dengan 21, D
    # Lainnya E

# 5. Tunjukkan nilai akhir dari mahasiswa ke 11 sampai dengan 20

# 6. Tunjukkan nilai akhir dari mahasiswa yang memiliki First Name "Ryan"

# 7. Hitung berapa jumlah mahasiswa Male dan Female

# 8. Tampilkan hanya mahasiswa yang memiliki nilai huruf = A




#                           PENYELESAIAN


# 1. tambahkan kolom fullname hasil gabungan dari firstname dan last name
dataPenilaian["Full Name"] = dataPenilaian["First Name"] + " " + dataPenilaian["Last Name"]
print(dataPenilaian)

# 2. Menghitung Nilai Rata Rata UAS
