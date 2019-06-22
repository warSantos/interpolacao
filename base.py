import pandas as pd
import numpy as np

# Colunas a serem remvoidas da base.
colunas = ['Evaporation', 'Sunshine', 'WindGustDir', 'WindDir9am',
           'WindDir3pm', 'Cloud9am', 'Cloud3pm', 'RainToday', 'RainTomorrow']


def carregar_base(caminho, colunas):
    data_frame = pd.read_csv(caminho)
    return data_frame.drop(colunas, axis=1)

def carregar_base_individual(caminho, data_inf='2012-01-01', \
        data_sup='2013-01-01'):
    data_frame = pd.read_csv(caminho)
    data_inf = data_frame[data_frame['Date'] >= data_inf]
    data_sup = data_inf[data_inf['Date'] <= data_sup]
    return data_sup