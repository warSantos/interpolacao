import base
import grafico
import math
import pandas as pd
import numpy as np
from sys import argv, exit

def quad(valor):
	return valor*valor

# Funções para calcular a regressão linear.

def funcao_reta(valor):
	return valor

def funcao_reta_final(coef_a, coef_b, x_valores, y_valores):

	# Calculando a regressão com suporte da função ajustada.
	regressao = [ (coef_a * x + coef_b) for x in x_valores ]
	grafico.distribuicao_aprox(x_valores, y_valores, regressao)

# Funções para calcular a aproximação parabólica.

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

if __name__=='__main__':
	data_frame = base.carregar_base_individual(argv[1])
	min_quad(data_frame, argv[2])