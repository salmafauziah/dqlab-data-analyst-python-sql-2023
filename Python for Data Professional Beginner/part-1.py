# Program pertama: "Hello World"
print("Hello World!")

# Program Pertamaku
# Sekarang aku diberikan tugas dari Senja untuk menampilkan kalimat “Halo Dunia” dan “Riset Bahasa Python” menggunakan fungsi print()#
print("Halo Dunia")
print("Riset Bahasa Python")

# Struktur Program Python - Part 1
# Statement
print("Belajar Python Menyenangkan") 
print("Halo Dunia")
print("Hello World!")

# Variables & Literals
bilangan1 = 5
bilangan2 = 10
kalimat1 = "Belajar Bahasa Python"

# Operators
print(bilangan1 + bilangan2)

# Tugas Praktek
# Deklarasi variable bilangan1 dengan 20, dan bilangan2 dengan 10 dan tampilkan hasil pengurangan bilangan1 & bilangan 2.
bilangan1 = 20
bilangan2 = 10
print(bilangan1 - bilangan2)

# Tugas Praktek
# Tugas:
# Aku diminta menghitung harga_setelah_potongan dan harga_final. harga_final diperoleh dengan mengalikan harga_setelah_potongan dengan angka 1.1 karena PPN sebesar 10% (100% + 10% = 110% atau 1.1)
# Aku menggunakan variabel harga_asli dengan nilai 20000 dan variabel potongan dengan nilai 2000
harga_asli = 20000
potongan = 2000
harga_setelah_potongan = harga_asli - potongan
harga_final = harga_setelah_potongan * 1.1
print(harga_final)

# Sequence Type – Part 1
# Aku diberikan tugas untuk menerapkan variasi tipe data list dengan mengikuti petunjuk yang diberikan Senja. Berikut petunjuknya:

# Petunjuk 1: Input data 1, 'dua', 3, 4.0, 5 ke dalam contoh_list
# Petunjuk 2: Ambil Elemen pertama dari contoh_list untuk menampilkan output 1 menggunakan print statement
# Petunjuk 3: Ambil Elemen ke empat dari contoh_list untuk menampilkan output 4.0 menggunakan print statement
# Petunjuk 4: Input data 1, 'dua', 3, 4.0, 5 ke dalam contoh_list
# Petunjuk 5: Rubah Elemen keempat dalam contoh_list menjadi 'empat'
# Petunjuk 6: Tampilkan output elemen keempat yang telah dirubah tersebut menggunakan print statement
contoh_list = [1, 'dua', 3, 4.0, 5]
print(contoh_list[0])
print(contoh_list[3])
contoh_list = [1, 'dua', 3, 4.0, 5]
contoh_list[3] = 'empat'
print(contoh_list[3])

# Sequence Type – Part 2
# Petunjuk 1: Input data Januari sampai dengan April ke dalam contoh_tuple
# Petunjuk 2: Ambil Elemen pertama dari contoh_tuple untuk menampilkan output 1 menggunakan print statement
# Petunjuk 3: Input kembali data Januari sampai dengan April ke dalam contoh_tuple
# Petunjuk 4: Rubah Elemen pertama dalam contoh_tuple menjadi 'Desember'
contoh_tuple = ('Januari', 'Februari', 'Maret','April')
print(contoh_tuple[0])
contoh_tuple = ('Januari', 'Februari', 'Maret','April')
contoh_tuple[0] = 'Desember'

# Set Type
# Tugas 1:Input data Dewi, Budi, Cici, Linda, Cici kedalam tipe data list dan tampilkan hasilnya
# Tugas 2: Input data Dewi, Budi, Cici, Linda, Cici kedalam tipe data set dan tampilkan hasilnya
# Tugas 3: Input data Dewi, Budi, Cici, Linda, Cici kedalam tipe data frozenset dan tampilkan hasilnya
contoh_list = ['Dewi', 'Budi','Cici','Linda','Cici'] 
print(contoh_list)
contoh_set = {'Dewi', 'Budi','Cici','Linda','Cici'}
print(contoh_set)
contoh_frozen_set = ({'Dewi', 'Budi','Cici','Linda','Cici'})
print(contoh_frozen_set)

# Mapping Type
# Menggunakan tipe data mapping, aku diminta Senja untuk menampilkan nama & pekerjaan John Doe, seorang Programmer
person = {'nama':'John Doe', 'pekerjaan':'Programmer'}
print(person['nama'])
print(person['pekerjaan'])

# Tugas Praktek 1
sepatu = {"nama": 'Sepatu Niko', 'Harga': 150000, "diskon": 30000 }
baju = {"nama": 'Baju Unikloh', 'Harga': 80000, "diskon": 8000 }
celana = {"nama": 'Celana Lepis', 'Harga': 200000, "diskon": 60000 }

# Tugas Praktek 2
# Setelah berhasil merepresentasikan setiap barang ke dalam tipe data dictionary dengan variabel nama, harga, dan diskon, langkahku selanjutnya adalah: mendeklarasikan list dengan nama daftar_belanja yang berisi data sepatu, baju, dan celana.
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000} 
daftar_belanja = [sepatu, baju, celana]

# Tugas Praktek 3
# Dengan data yang aku miliki, aku bisa menghitung total harga jual dengan potongan harga beserta pajak sebesar 10% dari nilai jual.
# Untungnya Senja memberikan beberapa tips untuk menyelesaikan tugas ini:
# Tips 1. # Data yang dinyatakan ke dalam dictionary
# Tips 2. # Hitung harga masing-masing data setelah dikurangi diskon
# Tips 3. # Hitung harga total
# Tips 4. # Hitung harga kena pajak
# Tips 5. # Cetak total_harga + total_pajak
# Data yang dinyatakan ke dalam dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}

# Hitunglah harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"] 
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]

# Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana

# Hitung harga kena pajak
total_pajak = total_harga * 0.1

# Cetak total_harga + total_pajak
print(total_harga + total_pajak)

















































