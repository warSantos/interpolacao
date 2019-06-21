# argv[1]: arquivo com dataset.
# argv[2]: cidade a ser analisada.
# argv[3]: eixo x do gráfico (Date, MaxTemp, MinTemp...).
# argv[4]: eixo y do gráfico (Date, MaxTemp, MinTemp...).
# argv[5]: Data inicial (2009-01-01).
# argv[6]: Data final (2011-01-01).
# argv[7]: Gap para o salto no xlabel (defautl 365).

import base
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv, exit

def distribuicao(data_frame, label_x, label_y, gap=365):
	plt.style.use('ggplot')
	y_range = data_frame[label_y]
	len_y = len(y_range)
	x_range = ''
	if label_x == 'Date':	
		x_range = range(0,len_y)
	else:
		x_range = data_frame[label_x]
	#data_frame.plot.scatter(x=x_range, y=label_y)
	plt.xticks(np.arange(1, len_y, step=gap))
	plt.scatter(x_range, y_range, s=2000/len_y)
	plt.show()
	plt.close()

def distribuicao_aprox(x_valores, y_valores, aproximacao):
	
	plt.style.use('ggplot')
	plt.scatter(x_valores, y_valores, s=1.2)
	plt.plot(aproximacao)
	plt.show()
	plt.close()

if __name__=='__main__':
	
	data_frame = base.carregar_base(argv[1], base.colunas)

	# Escolhendo de qual cidade se trata a relação.
	data_inf = data_frame[data_frame['Date'] >= argv[5]]
	data_sup = data_inf[data_inf['Date'] <= argv[6]]
	cidade = data_sup[data_sup['Location'] == argv[2]]

	if len(argv) <= 7:	
		distribuicao(cidade, argv[3], argv[4])
	else:
		distribuicao(cidade, argv[3], argv[4], float(argv[7]))