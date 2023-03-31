##################################
# Chapter 1 : Penggabungan Tabel dari Relasi Kolom
# Cobalah ketik query pada code editor untuk melihat keseluruhan isi dari kolom tabel ms_item_kategori dan ms_item_warna.
##################################

select * from ms_item_kategori;

select * from ms_item_warna;

##################################
# Chapter 1 : Penggabungan Tabel dari Relasi Kolom
# Menggabungkan Tabel dengan Key Columns
##################################

SELECT * FROM ms_item_kategori, ms_item_warna
WHERE nama_barang = nama_item;

##################################
# Chapter 1 : Penggabungan Tabel dari Relasi Kolom
# Dimana dua kolom pertama adalah dari tabel ms_item_warna, dan dua kolom berikutnya dari tabel ms_item_kategori. Hal ini sesuai dengan urutan nama tabel yang diketikkan setelah FROM.
##################################

SELECT * FROM ms_item_kategori, ms_item_warna
WHERE nama_barang = nama_item

##################################
# Chapter 1 : Penggabungan Tabel dari Relasi Kolom
# Menggunakan Prefix Nama Tabel
##################################

SELECT ms_item_kategori.*, ms_item_warna.*
FROM ms_item_warna, ms_item_kategori
WHERE nama_barang = nama_item

##################################
# Chapter 1 : Penggabungan Tabel dari Relasi Kolom
# Penggabungan Tanpa Kondisi
##################################

SELECT * FROM ms_item_kategori, ms_item_warna;

##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



##################################
# Chapter 2 : INNERJOIN
# ##################################



