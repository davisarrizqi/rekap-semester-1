import os

def pilihanSatu():
    print("    Pilihan Satu")

def pilihanKedua():
    print("    Pilihan Ke Dua")

def pilihanKetiga():
    print("    Pilihan Ke Tiga")

def pilihanKeEmpat():
    print("    Pilihan Ke Empat")

def pilihanKeLima():
    print("    Pilihan Ke Lima")

inputPengguna = 0

while inputPengguna != 6:
    # menampilkan menu
    print(
    """
    Pilih Salah Satu
    1. Pilihan ke satu
    2. Pilihan ke dua
    3. Pilihan ke tiga
    4. Pilihan ke empat
    5. Pilihan ke lima
    """); inputPengguna = int(input("    Pilihan Anda: "))

    # membuat percabangan
    if inputPengguna == 1: pilihanSatu()
    elif inputPengguna == 2: pilihanKedua()
    elif inputPengguna == 3: pilihanKetiga()
    elif inputPengguna == 4: pilihanKeEmpat()
    elif inputPengguna == 5: pilihanKeLima()
    elif inputPengguna == 6: print("    Selesai")
    else: print("    Pilihan tidak tersedia!"); os.system("cls")

    # bagian akhir ketika selesai menjalankan fungsi
    print("    Kembali ke Menu")
    

