#!/usr/bin/env python
# coding: utf-8

# In[35]:


#Imports
import math 
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import category_encoders as ce


# In[36]:


# Carga de datos.
train =  pd.read_csv('./ComercioExteriorSetDeDatos.csv', encoding='latin-1',dtype={
             "Channel":'category'
            ,"Día":'category'
            ,"Hora":str 
            ,"Periodo del Dia": 'category'
            })

a = train


# In[37]:


features = [ 'Hora',
              'Balenos',
              'Serendia',
              'Calpheon ',
              'Mediah',
              'Valencia',
              'Margoria',
              'Kamasilvia',
              'Drieghan',
             'Día_1_oh',
             'Día_2_oh',
             'Día_3_oh',
             'Periodo del Dia_1_oh',
             'Periodo del Dia_2_oh',
             'Periodo del Dia_3_oh',
             'Periodo del Dia_4_oh',
             'Periodo del Dia_5_oh',
             'Periodo del Dia_6_oh'
               ]  # 18
    
features2 = [ 'Hora',
              'Margoria',
             'Día_1_oh',
             'Día_2_oh',
             'Día_3_oh',
             'Periodo del Dia_1_oh',
             'Periodo del Dia_2_oh',
             'Periodo del Dia_3_oh',
             'Periodo del Dia_4_oh',
             'Periodo del Dia_5_oh',
             'Periodo del Dia_6_oh'
               ]  # 11
        
features3 = [ 'Hora',
              'Mediah',
             'Día_1_oh',
             'Día_2_oh',
             'Día_3_oh',
             'Periodo del Dia_1_oh',
             'Periodo del Dia_2_oh',
             'Periodo del Dia_3_oh',
             'Periodo del Dia_4_oh',
             'Periodo del Dia_5_oh',
             'Periodo del Dia_6_oh'
               ] # 11

features4 = [ 'Hora',
              'Mediah',
             'Periodo del Dia_1_oh',
             'Periodo del Dia_2_oh',
             'Periodo del Dia_3_oh',
             'Periodo del Dia_4_oh',
             'Periodo del Dia_5_oh',
             'Periodo del Dia_6_oh'
               ] # 8

features5 = [ 'Hora',
              'Margoria',
             'Periodo del Dia_1_oh',
             'Periodo del Dia_2_oh',
             'Periodo del Dia_3_oh',
             'Periodo del Dia_4_oh',
             'Periodo del Dia_5_oh',
             'Periodo del Dia_6_oh'
               ] # 8

features6 = [ 'Hora',
              'Margoria'
               ] # 2


# In[38]:


#One hot encoding
one_hot_enc = ce.OneHotEncoder()
one_hot_encoded = one_hot_enc.fit_transform(a[['Día','Periodo del Dia']])
a= a.join(one_hot_encoded.add_suffix("_oh"))


# In[39]:


#transformaciones
a['Fecha'] = pd.to_datetime(a['Fecha'])
a['Hora'] = pd.to_datetime(a['Hora'])
a['Hora'] = a.Hora.dt.hour


# In[42]:


#pregunta el channel del prodtucto que busco

while True:
    pos = input("Elije el channel 1-Balenos 2-Serendia 3-Calpheon 4-Mediah 5-Valencia 6-Margoria 7-Kamasilvia 8-Drieghan\n") 
    if int(pos) > 0 and int(pos) < 9:
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


#Separo el set 
X = a[ [ 'Hora', canales[ int(pos) -1] ] ]
y = a['Channel']

# No separo el set para luego ver el resultado por aun tengo muy pocos datos
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1,random_state=1)


# In[43]:


#Modelo
clf = RandomForestClassifier( random_state=0,bootstrap =False,min_samples_leaf=2 ,n_jobs=-1,
                             max_depth = 100,max_features =2,min_samples_split = 2 ,
                             n_estimators = 200 )
#Entrenamiento
model = clf.fit(X, y)


# In[44]:


#Prediccion
hora = input("Escribe la hora \n")
codigoProd = input("Escribe el codigo del producto \n")

print('El canal donde se podria encontrar el producto es :')
print(clf.predict([[ hora,codigoProd]]))


# In[ ]:




