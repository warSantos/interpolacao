import base
import grafico
import pandas as pd
import numpy as np
from sys import argv, exit

if __name__=='__main__':
	data_frame = base.carregar_base(argv[1], base.colunas)
	print(data_frame.head())