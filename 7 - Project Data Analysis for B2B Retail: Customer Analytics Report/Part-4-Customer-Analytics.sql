# Apakah jumlah customers xyz.com semakin bertambah?
# Penambahan jumlah customers dapat diukur dengan membandingkan total jumlah customers yang registrasi di periode saat ini 
# dengan total jumlah customers yang registrasi diakhir periode sebelumnya.

# Dari tabel customer, pilihlah kolom customerID, createDate dan tambahkan kolom baru dengan menggunakan fungsi QUARTER(…) 
# untuk mengekstrak nilai quarter dari CreateDate dan beri nama “quarter”

# Filter kolom “createDate” sehingga hanya menampilkan baris dengan createDate antara 1 Januari 2004 dan 30Juni 2004
# Gunakan statement Langkah 1 & 2 sebagai subquery dengan alias tabel_b
# Hitunglah jumlah unik customers à tidak ada duplikasi customers dan beri nama “total_customers”
# Kelompokkan total_customer berdasarkan kolom “quarter”, dan jangan lupa menambahkan kolom ini pada bagian select.

SELECT quarter, COUNT(DISTINCT customerID) AS total_customers
FROM (SELECT customerID, createDate, quarter(createDate) AS quarter FROM customer WHERE createDate BETWEEN '2004-01-01' AND '2004-06-30') AS tabel_b
GROUP BY quarter;
