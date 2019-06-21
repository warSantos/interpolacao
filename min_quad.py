import base
import grafico
import math
import pandas as pd
import numpy as np
from sys import argv, exit

# Funções para calcular a regressão linear.
# Função associada ao alfa1.
def funcao_reta_a1(valor):
	return valor
# Função associada ao alfa1.
def funcao_reta_a2(valor):
	return 1
# Função reta arpoximada com coeficientes.
def reta_aprox(valores_x, valores_y, coef_a1, coef_a2):

	# Calculando a regressão com suporte da função ajustada.
	regressao = [ (coef_a1 * x + coef_a2) for x in valores_x ]
	grafico.distribuicao_aprox(valores_x, valores_y, regressao)

# Funções para calcular a aproximação parabólica.
# Função associada ao alfa1.
def parabola_a1(valor):
	return math.pow(valor - 182, 2)
# Função associada ao alfa1.
def parabola_a2(valor):
	return valor
# Função parabólica aproximada com coeficientes.
def parab_aprox(valores_x, valores_y, coef_a1, coef_a2):
	
	res = list()
	for x in valores_x:
		v = (coef_a1 * math.pow((x - 180),2) - coef_a2)
		res.append(v)
	grafico.distribuicao_aprox(valores_x, valores_y, res)

## Implemente aqui suas funções de aproximação.
## Mantenha a ordem dos parâmetros para que o
## a função min_quad possa acha-las e aplica-las
## automaticamente. Siga o formato das funções acima
## mantenha a ordem e os parâmetros iguais. Chame também a 
## função de plotar o gráfico como nas funções de aproximação
## já implementadas para poder ver os resultados.

# Vetores com funções indexadas.

## Indexe aqui suas funções. Elas seram chamadas na funcao
## min_quad. Adicione também um comentário em frente ao indice
## igual nas funções abaixo.

# [0]: funções para cálculo com reta.
# [1]: funções de calculo com parábola.
funcoes = [[funcao_reta_a1, funcao_reta_a2], \
	[parabola_a1, parabola_a2]]

## Indexe aqui sua funcão aproximada com os coeficientes já 
## calculados. Siga o exemplo das funções já indexadas que
## foram implementadas logo acima.

funcoes_aprox = [reta_aprox,\
	parab_aprox]

# Matriz de calculo do sistema.
def matriz_a(valores, funcoes):

	# Pegando o número de coeficientes.
	n_coefs = len(funcoes)
	ma = np.zeros((n_coefs, n_coefs), dtype=float)

	# Calculando matriz.
	id_f = 0
	while id_f < len(funcoes):
		id_f2 = id_f
		g1 = funcoes[id_f]
		while id_f2 < len(funcoes):
			g2 = funcoes[id_f2]
			for v in valores:
				r = g1(v) * g2(v)
				ma[id_f][id_f2] += r
			# Atualizando diagonal secundária e posições abaixo da matriz.
			ma[id_f2][id_f] = ma[id_f][id_f2]
			id_f2 += 1
		id_f += 1

	return ma

# Vetor B de cálculo do sistema.
def vetor_b(valores_x, valores_y, funcoes):

	# Pegando o número de coeficientes.
	n_coefs = len(funcoes)
	vb = np.zeros((n_coefs, 1), dtype=float)
	id_f = 0
	while id_f < len(funcoes):
		g = funcoes[id_f]
		for v, y in zip(valores_x, valores_y):
			vb[id_f] += y * g(v)
		id_f += 1

	return vb

def preproc(data_frame, y_label, x_label='Date'):
	valores_y = data_frame[y_label]
	numero_valores = len(valores_y)
	valores_x = np.array(range(1, numero_valores+1), dtype=float)
	return valores_x, valores_y

def min_quad(data_frame, y_label, aprox_id):

	valores_x, valores_y = preproc(data_frame, y_label)
	ma = matriz_a(valores_x, funcoes[aprox_id])
	vb = vetor_b(valores_x, valores_y, funcoes[aprox_id])
	# Resolvendo o sistema.
	solucao = np.linalg.solve(ma, vb)
	print("SOLUÇÃO: ", solucao)
	ffinal = funcoes_aprox[aprox_id]
	ffinal(valores_x, valores_y, solucao[0], solucao[1])

if __name__=='__main__':
	data_frame = base.carregar_base_individual(argv[1])
	min_quad(data_frame, argv[2], int(argv[3]))