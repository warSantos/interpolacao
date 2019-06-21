import base
import grafico
import pandas as pd
import numpy as np
from sys import argv, exit

def quad(valor):
	return valor*valor

def funcao_reta(valor):
	return valor

def funcao_reta_final(coef_a, coef_b, x_valores, y_valores):

	# Calculando a regressão com suporte da função ajustada.
	regressao = [ (coef_a * x + coef_b) for x in x_valores ]
	grafico.distribuicao_aprox(x_valores, y_valores, regressao)

def minimos_quadrados_temporal(data_frame, y_label, \
	faplicada=funcao_reta, ffinal=funcao_reta_final):
	# Criando array com contabilização dos dias.
	numero_valores = len(data_frame['Date'])
	# Somatorio dos valores de x.
	x_valores = np.array(range(1, numero_valores+1))
	soma_x = np.sum(x_valores)
	# Somatorio dos valores de y.
	y_valores = [ faplicada(i) for i in data_frame[y_label] ]
	soma_y = np.sum(y_valores)
	# Somatorio dos valores de x*y
	soma_xy = 0
	for x, y in zip(x_valores, y_valores):
		soma_xy += x * y
	# Aplicando o quadrado em cada valor de x.
	soma_xquad = np.sum([ x*x for x in x_valores ])
	# Coeficiente a da função ax + b.
	coef_a = numero_valores * soma_xy - soma_x * soma_y
	coef_a /= numero_valores * soma_xquad - quad(soma_x)

	# Coeficiente b.
	coef_b = (soma_y - soma_x * coef_a)/numero_valores

	ffinal(coef_a, coef_b, x_valores, y_valores)

if __name__=='__main__':
	data_frame = base.carregar_base_individual(argv[1], \
		argv[3], argv[4])
	minimos_quadrados_temporal(data_frame, argv[2])