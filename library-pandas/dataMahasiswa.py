import pandas
import random

# input data
dataPenilaian = pandas.read_excel("Important Data/rekap_penilaian.xlsx")


# 1. Menambahkan kolom Full Name [First Name + Last Name]
dataPenilaian["Full Name"] = dataPenilaian["First Name"] + " " + dataPenilaian["Last Name"]



# 2. Mencari nilai rata rata UAS
meanValue = dataPenilaian["UAS"].mean()



# 3. Menambahkan kolom nilai akhir [T1 20%, T2 20%, UTS 25%, UAS 35%]

# siapkan pemrosesan
nilaiTugas = dataPenilaian["Tugas 1"]*20/100 + dataPenilaian["Tugas 2"]*20/100
nilaiUjian = dataPenilaian["UTS"]*25/100 + dataPenilaian["UAS"]*35/100
nilaiAkhir = nilaiTugas + nilaiUjian

# masukkan hasil tersebut ke dalam kolom baru, serta buat judul kolom
dataPenilaian["Nilai Akhir"] = nilaiAkhir

# print(nilaiAkhir) --> debug hasil
print(dataPenilaian)



# 4. Menambahkan kolom Nilai Huruf, dengan ketentuan:
    # >=81 --> A    # >=41 --> C
    # >=61 --> B    # >= 21 --> D
                    # other --> E

# membuat fungsi sebagai logika
def hasilkanNilaiHuruf(value):
    if(value >= 81):
        return 'A'

    elif(value >= 61):
        return 'B'

    elif(value >= 41):
        return 'C'

    elif(value >= 21):
        return 'D'

    else:
        return 'D'

# membuat list untuk menampung hasil nilai hurufnya
listNilaiHuruf = []

# memasukkan masing masing nilai akhir menjadi nilai huruf
for element in dataPenilaian["Nilai Akhir"]:
    listNilaiHuruf.append(hasilkanNilaiHuruf(element))

# memasukkan masing masing nilai huruf ke dalam kolom baru
dataPenilaian["Nilai Huruf"] = listNilaiHuruf

# debug hasilnya
print(dataPenilaian)



# 5. Menunjukkan Nilai Akhir dari mahasiswa ke 11 sampai dengan 20

# menentukan awal index
startingIndex = 11; endIndex = 20

# menampilkan dengan cara menggunakan for
for element in range((endIndex-startingIndex) + 1):
    print(f"{element + 1}). Nilai Mahasiswa ke {element + startingIndex} adalah", end=' ')
    print(dataPenilaian["Nilai Akhir"][element + startingIndex])


print(' ') # --> blank space


# 6. Menunjukkan Nilai Akhir dari mahasiswa yang memiliki First Name "Ryan"

# mendeklarasikan variabel sebagai penampung
targetName = 'Ryan'; listName = list(dataPenilaian["First Name"])
indexPosition = listName.index(targetName) # --> index 12

# menampilkan nilai akhir dari mahasiswa index 12
print(f"Nilai Akhir dari {targetName} adalah", end=' ')
print(dataPenilaian["Nilai Akhir"][indexPosition])


print(' ') # --> blank space


# 7. Menghitung jumlah mahasiswa Male dan Female

# membuat variabel sebagai penampung data
totalMale = 0; totalFemale = 0
takTerDefinisi = 0

# melakukan pengecekan
for element in dataPenilaian["Sex"]:
    if(element == "Male"): totalMale += 1
    elif(element == "Female"): totalFemale +=1
    else: takTerDefinisi += 1

# menampilkan hasilnya
print("Pada data tersebut, didapati bahwa terdapat ", end='')
print(f"sejumlah {totalMale} Male dan {totalFemale} Female")


print(' ') # --> blank space


# 8. Menampilkan hanya mahasiswa yang memiliki Nilai Huruf = A

# melakukan perhitungan dan deklarasi daftar nama beserta index
counter = 0; listName = []; listIndex = []

# melakukan for-loop untuk mengecek dan menampilkan
for char in dataPenilaian["Nilai Huruf"]:
    if(char == 'A'): 
        listIndex.append(counter)
        listName.append(dataPenilaian["Full Name"][counter])
    counter += 1    # --> Menambah perhitungan
counter = 0 # --> Melakukan reset

# Menampilkan hasilnya
print("Mahasiswa Dengan Perolehan Nilai Huruf A: ")
for name in listName:
    print(f"{counter + 1}). {name} dengan nomor index ", end='')
    print(listIndex[counter]); counter += 1
    

print(' ') # --> blank space
