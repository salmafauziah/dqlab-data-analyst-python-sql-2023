#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# Pengenalan Dataset
#####

import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
print('Ukuran dataset : %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# Penambahan Kolom Order Month pada Dataset
#####

import pandas as pd
import datetime

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')

dataset['order_month'] = dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())

#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# Penambahan Kolom GMV pada Dataset
#####

import pandas as pd
import datetime

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# Membuat Data Agregat
#####

import pandas as pd
import datetime

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)

#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



#####
# Chapter 1 : Pengenalan Matplotlib dan Persiapan Dataset
# #####



