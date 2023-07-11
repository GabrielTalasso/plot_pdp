#este arquivo e responsavel por conter a funcao de preprocessamento de dados financeiros
import pandas as pd
import numpy as np

def preprocessing(data, NA = 'drop',
                  to_date = 'none', date_format = 'none',
                  normalization = False, norm_type = 'norm',
                  dummies = 'none'):
    
    """
    Perform preprocessing on a dataset.

    Args:
        data (object): The dataset to be preprocessed.
        NA (str, optional): Determines how to handle missing values (NA). Defaults to 'drop'.
            - 'drop': Remove rows containing missing values.
            - 'mean_mode': Replace missing values in numeric columns with the mean, and in categorical columns with the mode.
        to_date (str, optional): The name of the column containing date data. Defaults to 'none'.
            If different from 'none', the column will be converted to a date format.
        date_format (str, optional): The format of the date in the 'to_date' column. Defaults to 'none'.
            If 'none', the default format will be used. Otherwise, a valid date format must be specified.
        normalization (bool, optional): Determines whether to perform normalization on numeric data. Defaults to False.
            If True, numeric data will be normalized; otherwise, no processing will be done.
        norm_type (str, optional): The type of normalization to apply. Defaults to 'norm'.
            - 'norm': Standard normalization using mean and standard deviation.
            - 'min_max': Min-max scaling using the minimum and maximum values of the data.
        dummies (str or list, optional): Determines how to handle categorical columns. Defaults to 'none'.
            - 'none': No transformation will be applied to categorical columns.
            - 'all': All categorical columns will be converted to dummy variables.
            - List of specific categorical column names to be converted to dummy variables.

    Returns:
        object: The preprocessed dataset.
    """

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
            data[to_date] = pd.to_datetime(data[to_date])
        else:
            data[to_date] = pd.to_datetime(data[to_date], format = date_format)

    #normalizacao 

    if normalization:

        if norm_type == 'norm':
            data_num = (data_num - data_num.mean()) / data_num.std()

        if norm_type == 'min_max':
            data_num = (data_num - data_num.min())/(data_num.max() - data_num.min())
            

    #categorical columns
    if dummies != 'none':

        if dummies == 'all':
            dummies = data_cat.columns

        data_cat = pd.concat([data_cat, pd.get_dummies(data[dummies])*1], axis = 1)
        data_cat = data_cat.drop(dummies, axis = 1)


    if to_date != 'none':

        data = pd.concat([data[to_date], data_cat], axis = 1)
        data = pd.concat([data, data_num], axis = 1)

    else:
        data = pd.concat([data_cat, data_num], axis = 1)

    return data