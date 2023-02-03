# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

# <h2>Pierwszy skrypt</h2>
# pierwsza próba użycia **Datalore notebook** <strong><cite>użycie pandas<cite></strong>


data = {
    'jabłko':[3,4,0,2],
    'pomarańcza':[2,10,1,2],
    'borówka':[3,2,2,0],
    'winogrono':[1,0.3,0.1,0.8]
}

pur = pd.DataFrame(data)
pur

pur = pd.DataFrame(data,index=['Olek','Dalia','Tadeusz','Ania'])
pur

pur.loc['Olek']

pur.to_csv('owoce.csv')
pur.to_xml('owoce.xml')

df1 = pd.read_csv('owoce.csv')
df1

unsorted_df = pd.DataFrame(np.random.randn(13,3),index=[1,4,6,2,3,5,9,8,0,7,10,11,12],columns=['b','a','c'])
unsorted_df

sorted_df = unsorted_df.sort_index()
sorted_df

sorted_df = unsorted_df.sort_index(ascending=False)
sorted_df

sorted_df = unsorted_df.sort_index(axis=1)
sorted_df

sorted_df = unsorted_df.sort_values(by='a',ascending=False)
sorted_df

def policz(a,b):
    return a*(b-2)

policz(3,6.6)

