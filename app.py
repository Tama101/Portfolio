print('''
Selamat Datang di Aplikasi Input Data

Data yang bisa anda inputkan adalah nama dan jenis kelamin.
''')

x = int(input("Masukkan jumlah data yang ingin diinput: "))
nama = []
gender = []
for i in range(x):
    nama.append(input("Masukkan nama: "))
    gender.append(input("Masukkan jenis kelamin (L/P): "))

print('''Terima kasih sudah menginputkan datanya!

Berikut data yang telah anda inputkan:''')

data = pd.DataFrame({'Nama':nama,'Jenis Kelamin':gender})
print(data)