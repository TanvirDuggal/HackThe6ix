# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:38:13 2021

@author: Tanvy
"""

import pandas as pd

# Reading CSV file
df = pd.read_csv('dataset/HDI.csv',  engine='python')
#Displaying records
print(df)
#Displaying records for some columns
print(df[["Country", "2018"]])
#Displaying first 5 records
print(df.head())
#Filtering records
print(df[df["1990"] > 0.2][["Country", "1990"]])
#Getting dataset information
print(df.columns)
print(len(df))
print(df.iloc[0])
#Creating new column and prefilling it
df["NewColumn"] = 'its new column wow'
print(df.head())

df["OneMoreColumn"] = df['2018'] + df['2019']
print(df)

print(df.iloc[0]["2011"])


for i in range(len(df)):
    df.at[i, '2019'] = df.at[i, '2019'] * 2
    
print(df[['Country', '2019']])


df.to_csv("export.csv")
#for i in range(len(df)):
#    print(df.iloc[i])
    