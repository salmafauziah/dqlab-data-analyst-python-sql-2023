##############################
# Chapter 1 : Pengenalan Library dalam Python
# Memanggil library di Python
##############################

import numpy as np
import pandas as pd

##############################
# Chapter 1 : Pengenalan Library dalam Python
# Cobalah untuk mengimport dataset marketplace ABC dari order.csv dan disimpan ke dalam dataframe bernama order_df.
##############################

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

##############################
# Chapter 1 : Pengenalan Library dalam Python
# Cobalah untuk order dataframe dengan menuliskan syntax Python untuk melihat struktur dari order_df dengan menggunakan fungsi shape!
##############################

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.shape

##############################
# Chapter 1 : Pengenalan Library dalam Python
# Cobalah untuk check bagaimana contoh data dari dataframe tersebut dengan fungsi head dengan limit 10 baris!
##############################

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.head(10))

##############################
# Chapter 1 : Pengenalan Library dalam Python
# Tugas Praktek
##############################

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())
# Median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())

##############################
# Chapter 1 : Pengenalan Library dalam Python
# Tugas Praktek : Aku pun kembali merebahkan diri di bangku dan mengutak-atik dataset order_df dengan jumlah bins=10: & Bikin saja dalam bentuk histogram price
##############################
      
import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# plot histogram kolom: price
order_df[["price"]].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)

plt.show()  # Untuk menampilkan histogram plot
