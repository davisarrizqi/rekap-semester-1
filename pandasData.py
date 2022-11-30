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

# 1. tambahkan kolom fullname hasil gabungan dari firstname dan last name
dataPenilaian["Full Name"] = dataPenilaian["First Name"] + " " + dataPenilaian["Last Name"]
print(dataPenilaian)
