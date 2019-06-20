# argv[1]: arquivo com dataset.
# argv[2]: cidade a ser analisada.
# argv[3]: eixo x do gráfico (Date, MaxTemp, MinTemp...).
# argv[4]: eixo y do gráfico (Date, MaxTemp, MinTemp...).
# argv[5]: Data inicial (2009-01-01).
# argv[6]: Data final (2011-01-01).

import base
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv, exit

def distribuicao(data_frame, label_x, label_y):
	plt.style.use('ggplot')
	x_range = range(0,len(data_frame[label_y]))
	y_range = data_frame[label_y]
	#data_frame.plot.scatter(x=x_range, y=label_y)
	plt.scatter(x_range, y_range, s=1.2)
	plt.show()
	plt.close()

if __name__=='__main__':
	
	colunas = ['Evaporation', 'Sunshine', 'WindGustDir', 'WindDir9am', \
		'WindDir3pm', 'Cloud9am', 'Cloud3pm', 'RainToday', 'RainTomorrow']
	data_frame = base.carregar_base(argv[1], colunas)

	# Escolhendo de qual cidade se trata a relação.
	data_inf = data_frame[data_frame['Date'] >= argv[5]]
	data_sup = data_inf[data_inf['Date'] <= argv[6]]
	cidade = data_sup[data_sup['Location'] == argv[2]]

	distribuicao(cidade, argv[3], argv[4])