import base
import grafico
import math
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

def parabola_a1(valor):
	return math.pow(valor - 172, 2)
	
def parabola_a2(valor):
	return valor

def parab_aprox(valores_x, valores_y, coef_a1, coef_a2):
	
	res = list()
	for x in valores_x:
		v = (coef_a1 * math.pow((x - 180),2) - coef_a2)
		res.append(v)
	
	grafico.distribuicao_aprox(valores_x, valores_y, res)

def preproc(data_frame, x_label, y_label):
	y_valores = data_frame[y_label]
	numero_valores = len(y_valores)
	x_valores = np.array(range(1, numero_valores+1))
	return x_valores, y_valores

def min_quad(data_frame, y_label, x_label='Date', len_matriz=2, \
	g1=parabola_a1, g2=parabola_a2, ffinal=parab_aprox):

	# Carregando dados do problema.
	valores_x, valores_y = preproc(data_frame, x_label, y_label)

	# Construindo vetores.
	matriz_a = np.zeros((len_matriz, len_matriz))
	vetor_b = np.zeros(len_matriz)

	# Construindo matriz do sistema (Ax).
	for i in valores_x:
		matriz_a[0][0] += g1(i) * g1(i)
	
	for i in valores_x:
		matriz_a[0][1] += g1(i) * g2(i)
	matriz_a[1][0] = matriz_a[0][1]
	
	for i in valores_x:
		matriz_a[1][1] += g2(i) * g2(i)
	
	# Construindo vetor de igualdade (vetor B).
	for i, j in zip(valores_x, valores_y):	
		vetor_b[0] += j * g1(i)
		vetor_b[1] += j * g2(i)
	
	# Resolvendo o sistema.
	solucao = np.linalg.solve(matriz_a, vetor_b)
	print(solucao)
	ffinal(valores_x, valores_y, solucao[0], solucao[1])

if __name__=='__main__':
	data_frame = base.carregar_base_individual(argv[1])
	min_quad(data_frame, argv[2])