import base
import grafico as gfc
import math as mt
import pandas as pd
import numpy as np
import statistics as sttc
from sys import argv, exit

# Funções para calcular a regressão linear.
# Função associada ao alfa1.
def funcao_reta_a1(valor):
	return valor
# Função associada ao alfa1.
def funcao_reta_a2(valor):
	return 1
# Função reta arpoximada com coeficientes.
def reta_aprox(valores_x, valores_y, solucao, gap, grafico):

	# Calculando a regressão com suporte da função ajustada.
	regressao = [ (solucao[0][0] * x + solucao[1][0]) for x in valores_x ]
	gfc.distribuicao_aprox(valores_x, valores_y, regressao, gap, grafico)
	return regressao

# Funções para calcular a aproximação parabólica.
# Função associada ao alfa1.
def parabola_a1(valor):
	return mt.pow(valor - 182, 2)
# Função associada ao alfa1.
def parabola_a2(valor):
	return 1
# Função parabólica aproximada com coeficientes.
def parab_aprox(valores_x, valores_y, solucao, gap, grafico):
	
	res = list()
	for x in valores_x:
		v = (solucao[0][0] * mt.pow((x - 180),2) + solucao[1][0])
		res.append(v)
	gfc.distribuicao_aprox(valores_x, valores_y, res, gap, grafico)
	return res

# Funções para calcular polinômios de grau 2: ax2 + bx + c, a,b,c == alfas(1,2,3).
def coeficiente_a(valor):
	return mt.pow(valor, 2)

def coeficiente_b(valor):
	return valor

def coeficiente_c(valor):
	return 1

# ax2 + bx + c
def polinomio_g2(valores_x, valores_y, solucao, gap, grafico):
	res = list()
	for x in valores_x:
		v = solucao[0][0] * mt.pow(x, 2) + \
			solucao[1][0] * x + \
			solucao[2][0]
		res.append(v)
	gfc.distribuicao_aprox(valores_x, valores_y, res, gap, grafico)
	return res

# Funções para calcular polinômios de grau 2: ax3 + bx2 + cx + d, a,b,c,d == alfas(1,2,3,4).
def coeficiente_d(valor):
	return mt.pow(valor, 3)

# ax3 + bx2 + cx + d
def polinomio_g3(valores_x, valores_y, solucao, gap, grafico):
	res = list()
	for x in valores_x:
		v = solucao[0][0] * mt.pow(x, 3) + \
			solucao[1][0] * mt.pow(x, 2) + \
			solucao[2][0] * x + \
			solucao[3][0]
		res.append(v)
	gfc.distribuicao_aprox(valores_x, valores_y, res, gap, grafico)
	return res

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
	[parabola_a1, parabola_a2],
	[coeficiente_a, coeficiente_b, coeficiente_c],
	[coeficiente_d, coeficiente_a, coeficiente_b, coeficiente_c]]

## Indexe aqui sua funcão aproximada com os coeficientes já 
## calculados. Siga o exemplo das funções já indexadas que
## foram implementadas logo acima.

funcoes_aprox = [reta_aprox,\
	parab_aprox,
	polinomio_g2,
	polinomio_g3]

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
	print(ma)
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
	print(vb)
	return vb

def residuo(valores_y, aprox):
	num = 0
	den = 0
	media_y = sttc.median(valores_y)
	for y, a in zip(valores_y, aprox):
		num += mt.pow((a - media_y), 2)
		den += mt.pow((y - media_y), 2)
	return mt.sqrt(num/den)

def preproc(data_frame, y_label, x_label='Date'):
	valores_y = data_frame[y_label]
	numero_valores = len(valores_y)
	valores_x = np.array(range(1, numero_valores+1), dtype=float)
	return valores_x, valores_y

def min_quad(data_frame, y_label, aprox_id, gap, grafico):

	valores_x, valores_y = preproc(data_frame, y_label)
	ma = matriz_a(valores_x, funcoes[aprox_id])
	vb = vetor_b(valores_x, valores_y, funcoes[aprox_id])
	# Resolvendo o sistema.
	solucao = np.linalg.solve(ma, vb)
	print("SOLUÇÃO: ", solucao)
	ffinal = funcoes_aprox[aprox_id]
	aprox = ffinal(valores_x, valores_y, solucao, gap, grafico)
	res = residuo(valores_y, aprox)
	pt_write = open(grafico.replace('pdf', 'res'), 'w')
	pt_write.write(str(res)+'\n')
	pt_write.close()

if __name__=='__main__':
	data_frame = base.carregar_base_individual(argv[1], argv[4], argv[5])
	grafico = 'resultados/'+argv[1].split('/')[-1].replace('.csv','')+\
		'_'+argv[2]+'_'+argv[4]+'_'+argv[5]+'_'+argv[3]+'.pdf'
	min_quad(data_frame, argv[2], int(argv[3]), int(argv[6]), grafico)