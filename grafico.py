# argv[1]: arquivo com dataset.
# argv[2]: cidade a ser analisada.
# argv[3]: eixo x do gráfico (Date, MaxTemp, MinTemp...).
# argv[4]: eixo y do gráfico (Date, MaxTemp, MinTemp...).
# argv[5]: Data inicial (2009-01-01).
# argv[6]: Data final (2011-01-01).
# argv[7]: Gap para o salto no xlabel (defautl 365).

import base
import math as mt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sys import argv, exit

def distribuicao(data_frame, label_x, label_y, datas, gap=364):
	plt.style.use('ggplot')
	y_range = data_frame[label_y]
	pos_y = max(y_range)
	print(pos_y)
	len_y = len(y_range)
	x_range = ''
	if label_x == 'Date':	
		x_range = range(0,len_y)
	else:
		x_range = data_frame[label_x]
	#data_frame.plot.scatter(x=x_range, y=label_y)
	plt.xticks(np.arange(1, len_y, step=gap))
	plt.xlabel('Período em dias')
	plt.ylabel('Temperatura em C°')
	plt.scatter(x_range, y_range, s=3000/len_y, label="Distrib.")
	plt.legend(loc='best')
	plt.text(5, pos_y, datas[0]+' á '+datas[1])
	plt.show()
	plt.close()

def distribuicao_aprox(x_valores, y_valores, aproximacao, gap=30,\
	grafico='grafico.pdf'):
	
	plt.style.use('ggplot')
	plt.xlabel('Período em dias')
	plt.ylabel('Temperatura em C°')
	plt.xticks(np.arange(1, len(x_valores), step=gap))
	plt.scatter(x_valores, y_valores, s=2.8, label="Distrib.")
	plt.plot(aproximacao, 'blue', label="Aprox.")
	plt.legend(loc='best')
	#plt.show()
	plt.savefig(grafico, format='pdf')
	plt.close()

if __name__=='__main__':
	
	data_frame = base.carregar_base(argv[1], base.colunas)

	# Escolhendo de qual cidade se trata a relação.
	data_inf = data_frame[data_frame['Date'] >= argv[5]]
	data_sup = data_inf[data_inf['Date'] <= argv[6]]
	cidade = data_sup[data_sup['Location'] == argv[2]]

	if len(argv) <= 7:
		distribuicao(cidade, argv[3], argv[4], [argv[5], argv[6]])
	else:
		distribuicao(cidade, argv[3], argv[4], [argv[5], argv[6]], \
			float(argv[7]))