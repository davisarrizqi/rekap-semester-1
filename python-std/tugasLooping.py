"""
While vs For
> While --> Range yang belum ditentukan
> For --> Range yang lebih pasti

> While --> Menggunakan True or False
> For --> Menggunakan range yang pasti

[ len()--> Menghitung panjang list (berapa banyak item) ]

"""

def materiPertama():
    angka = 1
    print('Hasil Loop\n')
    while angka < 10:
        print(angka)
        angka += 1

    print('Hasil Akhir')
    print(angka)


data = [12, "Zaka", 40, 64, "Yongga"]

# 1. Tampilkan item ke 2
print('Tampilkan item ke 2')
print(data[1])
print('')

# 2. Tampilkan semua item di dalam list data
print('Tampilkan semua item di dalam list data')
for item in data:
    print(item)
print('')

# 3. Tampilkan item terakhir
print('Tampilkan item terakhir')
print(data[-1])
print('')

# 4. Tampilkan item yang string dan integer
print('Tampilkan item yang string dan integer')
print("Ini adalah yang string")
for item in data:
    if isinstance(item, str): print(item)

print("Ini adalah yang integer")
for item in data:
    if isinstance(item, int): print(item)

print('')

# 5. Tampilkan hasil penjumlahan semua angka
print('Tampilkan hasil penjumlahan semua angka')
totalNum = 0
for item in data:
    if isinstance(item, int): totalNum += item
print(f"Hasil penjumlahannya: {totalNum} ")
