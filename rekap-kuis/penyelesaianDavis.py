
import matplotlib.pyplot as plt
import pandas

# ----------------------------------------------------------------- - #
# deklarasikan pusat datanya terlebih dahulu
dataFrame = pandas.read_excel("berkas-penyelesaian/produksi_perikanan.xlsx")
# ------------------------------------------------------------------- #


# ------------------------------------------------------------------- #
# 1. Tampilkan provinsi dan produksi perikanan hanya di tahun 2017
print(dataFrame[["Provinsi", 2017]])
# ------------------------------------------------------------------- #


print(" ") #--> blank space


# ------------------------------------------------------------------------------------------- #
# 2. Tambahkan kolom yang akan menghitung nilai rata-rata semua produksi dari setiap provinsi

# deklarasikan terlebih dahulu
jumlahProvinsi = len(dataFrame["Provinsi"])
listTahun = []; listIndexTahun = []; listColumnHeader = []
listRataRata = []; pivotList = []; counter = 0; nestedCount = 0

# memasukkan setiap column header terhadap listColumnHeader
for data in dataFrame:
    listColumnHeader.append(data)

# mendeteksi variabel integer yang merupakan variabel tahun
for data in listColumnHeader:
    try: data = int(data); listTahun.append(data)
    except: pass

# mendeteksi index masing masing tahun, lalu menginput pada list
for data in listTahun:
    listIndexTahun.append(listColumnHeader.index(data))

# memasukkkan data dari masing masing provinsi
for columnHeader in listColumnHeader:
    for data in dataFrame.iloc[[nestedCount][0]]:
        if(counter in listIndexTahun): pivotList.append(data)
        counter += 1
    listRataRata.append(pivotList); pivotList = []
    counter = 0; nestedCount += 1

# membuat fungsi untuk konversi masing masing data menjadi rata rata
def listMean(listNumber):
    # deklarasi terlebih dahulu
    totalNumber = 0; mean = 0
    counter = 0; listMean = []
    
    # membuat for-loop untuk memasukkan masing masing rata rata
    for number in listNumber:
        for nestedNumber in number:
            totalNumber += nestedNumber
        mean = totalNumber/len(number)
        
        # append lalu reset
        listMean.append(mean)
        mean = 0

    return listMean
listRataRata = listMean(listRataRata)

# setelah diolah data tersebut, lalu masukkan ke dalam kolom baru
dataFrame["Rata Rata"] = listRataRata

# tampilkan hasilnya
print(dataFrame)
# ------------------------------------------------------------------------------------------- #


print(" ") #--> blank space


# ----------------------------------------------------------------------------------- #
# 3. Tampilkan data produksi perikanan di Provinsi DI Yogyakarta dari tahun ke tahun

# deklarasikan terlebih dahulu
listProvinsi = [province for province in dataFrame["Provinsi"] if(province != None)] 
indexYogyakarta = listProvinsi.index("DI Yogyakarta")

# tampilkan hasilnya
print(dataFrame.iloc[[indexYogyakarta]])
# ----------------------------------------------------------------------------------- #


print(" ") #--> blank space


# ------------------------------------------------------------------------------------------- #
# 4. Buatlah grafik sebagaimana dalam Figure 1

# deklarasikan terlebih dahulu
jatengPos = listProvinsi.index("Jawa Tengah")
jatimPos = listProvinsi.index("Jawa Timur")

# memasukkan masing masing data ke dalam list
jatengData = [data for data in dataFrame.iloc[[jatengPos][0]] if data not in listProvinsi and data not in listRataRata]
jatimData = [data for data in dataFrame.iloc[[jatimPos][0]] if data not in listProvinsi and data not in listRataRata]

# labelling
plt.title("Perbandingan Produksi Perikanan")
plt.xlabel("Tahun ke-")
plt.ylabel("Nilai Produksi")

# dotting
plt.scatter(listTahun, jatengData)
plt.scatter(listTahun, jatimData)

# plotting dan memberikan legend
plt.plot(listTahun, jatengData, linestyle="dotted", label="Jawa Tengah")
plt.plot(listTahun, jatimData, linestyle="dashed", label="Jawa Timur")
plt.legend()

# mengatur koordinat x agar menjadi bulat
plt.xticks(listTahun)

# show the result
plt.show()
# ------------------------------------------------------------------------------------------- #

