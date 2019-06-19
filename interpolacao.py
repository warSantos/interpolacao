import pandas as pd
import numpy as np
from sys import argv, exit

def carregar_base(caminho, colunas):
	data_frame = pd.read_csv(caminho)
	return data_frame.drop(colunas, axis=1)

if __name__=='__main__':

	# Colunas a serem remvoidas da base.
	colunas = ['Evaporation', 'Sunshine', 'WindGustDir', 'WindDir9am', \
		'WindDir3pm', 'Cloud9am', 'Cloud3pm', 'RainToday', 'RainTomorrow']
	data_frame = carregar_base(argv[1], colunas)
	print(data_frame.head())