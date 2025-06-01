n=int(input("Masukkan jumlah kategori: "))

data_aplikasi={}
for i in range (n):
    nama_kategori=input("Masukkan nama katgori: ")
    print("Masukkan 5 nama aplikasi di kategori", nama_kategori)
    aplikasi=[]
    for j in range(5):
        nama_aplikasi=input("Nama aplikasi: ")
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori]=aplikasi

daftar_aplikasi_list =[]
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
hasil = daftar_aplikasi_list[0]
    
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print("Aplikasi yang muncul di semua kategori: ", hasil)
    
semua_aplikasi = []
for kategori in data_aplikasi:
    for aplikasi in data_aplikasi[kategori]:
        semua_aplikasi.append(aplikasi)

hitung_aplikasi = {}
for apk in semua_aplikasi:
    if apk in hitung_aplikasi:
        hitung_aplikasi[apk] += 1
    else:
        hitung_aplikasi[apk] = 1

satu_kategori = []
for apk in hitung_aplikasi:
    if hitung_aplikasi[apk] == 1:
        satu_kategori.append(apk)
print("\nAplikasi yang hanya muncul di satu kategori:", satu_kategori)
if n > 2:
        dua_kategori = []
        for apk in hitung_aplikasi:
            if hitung_aplikasi[apk] == 2:
                dua_kategori.append(apk)
print("\nAplikasi yang muncul tepat di dua kategori:", dua_kategori)