#este arquivo e responsavel por conter a funcao de preprocessamento de dados financeiros
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

path = './data/german_credit_data.csv'

def preprocessing(data, NA = 'drop',
                  to_date = 'none', date_format = 'none',
                  normalization = False, norm_type = 'norm',
                  dummies = 'none'):

    data_num = data.select_dtypes(include=np.number) #only numerical columns
    data_cat = data.drop(data_num.columns, axis = 1) #only categorical columns

    if to_date != 'none':
        data_cat = data_cat.drop(to_date, axis = 1)
    

    #null values management 
    if NA == 'drop':

        data = data.dropna()
        data_num = data.select_dtypes(include=np.number)
        data_cat = data.drop(data_num.columns, axis = 1) 

        if to_date != 'none':
            data_cat = data_cat.drop(to_date, axis = 1)

    if NA == 'mean_mode':
        #replace with the mean in numerical columns and with mode in categorical
        data_num = data_num.fillna('mean')

        for c in data_cat.columns:
            data_cat[c] = data_cat[c].fillna(data_cat[c].mode()[0])

    #datetimes

    if to_date != 'none':

        if date_format == 'none':
            data[to_date] = pd.to_datetime(to_date)
        else:
            data[to_date] = pd.to_datetime(to_date, format = date_format)

    #normalizacao 

    if normalization:

        if norm_type == 'norm':
            data_num = (data_num - data_num.mean()) / data_num.std()

        if norm_type == 'min_max':
            data_num = (data_num - data_num.min())/(data_num.max() - data_num.min())
            

    #tratamento de categoricas
    if dummies != 'none':

        if dummies == 'all':
            dummies = data_cat.columns

        data_cat = pd.concat([data_cat, pd.get_dummies(data[dummies])], axis = 1)
        data_cat = data_cat.drop(dummies, axis = 1)


    if to_date != 'none':

        data = pd.concat([data[to_date], data_cat], axis = 1)
        data = pd.concat([data, data_num], axis = 1)

    else:
        data = pd.concat([data_cat, data_num], axis = 1)

    return data