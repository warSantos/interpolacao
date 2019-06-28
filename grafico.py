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
	plt.xticks(np.arange(1, len_y, step=gap), fontsize=26)
	plt.yticks(fontsize=26)
	plt.xlabel('Período em dias', fontsize=26)
	plt.ylabel('Temperatura em C°', fontsize=26)
	plt.scatter(x_range, y_range, s=10000/len_y, label="Distrib.")
	plt.legend(loc='best',  fontsize=26)
	plt.text(5, pos_y, datas[0]+' á '+datas[1], fontsize=26)
	plt.show()
	plt.close()

def distribuicao_aprox(x_valores, y_valores, aproximacao, gap=30,\
	grafico='grafico.pdf'):
	
	plt.style.use('ggplot')
	plt.xlabel('Período em dias', fontsize=18)
	plt.ylabel('Temperatura em C°', fontsize=18)
	plt.xticks(np.arange(1, len(x_valores), step=gap), fontsize=12)
	plt.yticks(fontsize=12)
	plt.scatter(x_valores, y_valores, s=3.8, label="Distrib.")
	plt.plot(aproximacao, 'blue', label="Aprox.")
	plt.legend(loc='best', fontsize=18)
	#plt.show()
	plt.savefig(grafico, format='pdf')
	plt.close()

def varios_plots(aprox_anos, gap=30, grafico='4grafico.pdf'):
	
	fig, axs = plt.subplots(2,2)
	i = 0
	j = 0
	cont = 0
	while i < 2:
		j = 0
		while j < 2:
			plt.sca(axs[i, j])
			plt.xticks(np.arange(1, len(aprox_anos[cont][0]), step=gap), \
				fontsize=12)
			plt.xlabel('Período em dias', fontsize=18)
			plt.ylabel('Temperatura em C°', fontsize=18)
			plt.yticks(fontsize=12)
			# Plotando distribuição
			axs[i, j].scatter(aprox_anos[cont][0], aprox_anos[cont][2], \
				s=3.8, label="Distrib.")
			# Plotando aproximação
			axs[i, j].plot(aprox_anos[cont][1], 'blue', label="Aprox.")
			plt.legend(loc='best', fontsize=18)
			j += 1
			cont += 1
		i += 1
	#plt.show()
	#plt.savefig(grafico, format='pdf')

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