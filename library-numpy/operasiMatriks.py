import numpy

# deklarasi bagian 1
A = [1, 2, 3]; B = [4, 5, 6]

# deklarasi bagian 2
mA = [[1, 2, 3], [4, 2, -2]]
mB = [[-5, 1, 3], [4, -3, -1]]

# deklarasi bagian 3
mA1 = numpy.array(mA)
mB1 = numpy.array(mB)
mC = mA1 - mB1

# blank space
print("\n")


# Operasi Matriks
"""
1. Tunjukkan hasil pengurangan A dengan B
2. Tunjukkan hasil perkalian mA dengan mB
3. Balik matriks mB menjadi ordo 3x2 (transpose matriks)
4. Tunjukkan ordo matrik mB
5. Kerjakan soal nomor 2
6. Buatlah vektor baris "vc" yang merupakan gabungan
   dari mA dan mB
7. Hitunglah nilai terendah, tertinggi, rata-rata, dan
   standar deviasi dari vc
8. Ubah bentuk vektor  vc menjadi matriks dengan ukuran 4x3
"""

#                    Penyelesaian 

# 1. Menunjukkan hasil pengurangan A dengan B
print(numpy.array(A) - numpy.array(B))

print("\n") # --> Membuat blank space


# 2. Menunjukkan hasil perkalian mA dengan mB
try: result = mA1.dot(mB); print("\n") # --> Membuat blank space
except: pass
# untuk menghindari pemberhentian runned-script


# 3. Melakukan transpose matriks mB menjadi ordo 3x2
mB = numpy.transpose(mB); print(mB)

print("\n") # --> Membuat blank space


# 4. Menunjukkan ordo di matriks mB
print(numpy.shape(mB))

print("\n") # --> Membuat blank space


# 5. Mengerjakan soal nomor 2
# note --> banyak yang melakukan kesalahan di nomor 2
# sehingga, diadakan penugasan kembali di nomor 5
mAmB = mA1.dot(mB); print(mAmB)

print("\n") # --> Membuat blank space


# 6. Membuat vektor baris vc yang merupakan gabungan dari mA dan mB
mA = mA1.flatten(); mB = mB1.flatten()
vc = numpy.concatenate((mA, mB))
print(vc)

print("\n") # --> Membuat blank space


# 7. Menghitung nilai terendah, tertinggi, rata rata, dan std

# deklarasi terlebih dahulu
minValue = numpy.min(vc); maxValue = numpy.max(vc)
meanValue = numpy.mean(vc); stdValue = numpy.std(vc)

# lakukan print secara terpisah, tujuannya agar mudah dipahami
print("Nilai Terendah:", minValue)
print("Nilai Tertinggi:", maxValue)

print("Nilai Rata Rata:", meanValue)
print("Nilai Standar Deviasi:", stdValue)

print("\n") # --> Membuat blank space


# Mengubah bentuk vektor vc menjadi matriks ordo 4x3
vc = vc.reshape(4,3)
print(vc)
