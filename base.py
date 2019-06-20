import pandas as pd
import numpy as np

# Colunas a serem remvoidas da base.
colunas = ['Evaporation', 'Sunshine', 'WindGustDir', 'WindDir9am',
           'WindDir3pm', 'Cloud9am', 'Cloud3pm', 'RainToday', 'RainTomorrow']


def carregar_base(caminho, colunas):
    data_frame = pd.read_csv(caminho)
    return data_frame.drop(colunas, axis=1)
