#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[6]:


#Abro el csv
df = pd.read_csv('./ComercioExteriorSetDeDatos.csv', encoding='latin-1',dtype={
             "Channel":'category'
            ,"Día":'category'
            ,"Hora":str 
            ,"Periodo del Dia": 'category'
            })


# In[7]:


#df


# In[8]:


#Cambio la fecha a Datatime
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Hora'] = pd.to_datetime(df['Hora'])
df['Hora'] = df.Hora.dt.strftime('%H:%M')


# # Margoria

# In[9]:

while True:
    pos = input("\n\nElije el periodo 1:(0-4) 2:(4-8) 3:(8-12) 4:(12-16) 5:(16-20) 6:(20-24) \n") 
    if int(pos) > 0 and int(pos) < 7:
        break;

if int(pos) == 1 :
    a = df.loc[df['Periodo del Dia']=='(0-4 )']
    print('Lista de channels en ese periodo (0-4) \n')
if int(pos) == 2 :
    a = df.loc[df['Periodo del Dia']=='(4-8 )']
    print('Lista de channels en ese periodo (4-8) \n')
if int(pos) == 3 : 
    a = df.loc[df['Periodo del Dia']=='(8-12)']
    print('Lista de channels en ese periodo (8-12) \n')
if int(pos) == 4 :
    a = df.loc[df['Periodo del Dia']=='(12-16)']
    print('Lista de channels en ese periodo (12-16) \n')
if int(pos) == 5 :
    a = df.loc[df['Periodo del Dia']=='(16-20)']
    print('Lista de channels en ese periodo (16-20) \n')
if int(pos) == 6 :
    a = df.loc[df['Periodo del Dia']=='(20-24)']
    print('Lista de channels en ese periodo (20-24) \n')
    
    
print(a[['Channel','Hora','Balenos',
              'Serendia',
              'Calpheon ',
              'Mediah',
              'Valencia',
              'Margoria',
              'Kamasilvia',
              'Drieghan',]])


# In[10]:

while True:
    pos2 = input("\n\nElije la Region donde buscas el producto \n 1-Balenos 2-Serendia 3-Calpheon 4-Mediah 5-Valencia 6-Margoria 7-Kamasilvia 8-Drieghan\n") 
    if int(pos2) > 0 and int(pos2) < 9:
        break;

canales = [   'Balenos',
              'Serendia',
              'Calpheon ',
              'Mediah',
              'Valencia',
              'Margoria',
              'Kamasilvia',
              'Drieghan'
          ]

while True:
    codProd = input("Codigo del producto que buscas\n")
    if int(codProd) > 0 and int(codProd) < 6:
        break;
    

b = a.loc[ a[  canales[ int(pos2) -1]  ] == int(codProd)]
    
print('\n\nLista de Los channels con ese producto en esa region y ese periodo: \n')
print(b[['Channel','Hora','Fecha',canales[ int(pos2) -1]]])


# In[11]:


#b


# In[12]:

c = b.groupby('Channel').count().sort_values(by= canales[ int(pos2) -1],ascending=False).reset_index()


# In[14]:

d = c.nlargest(columns={canales[ int(pos2) -1]},n=5)
print('\n\nLista de Los channels con mayor frecuencia con ese producto en esa region : \n')
print(d[['Channel',canales[ int(pos2) -1]]])
print('\n\n\n')

# In[ ]:




