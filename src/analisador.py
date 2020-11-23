# biblioteca de manipulação do sistema operacional:
import os 

# capturando o diretorio raiz do projeto:
dir = os.path.dirname(os.getcwd())

# lendo os dados presentes no arquivo
base_file = open(f"{dir}/data/sourcefile.txt", "r")

# armazenando uma lista em que cada item é uma linha do arquivo:
lines = base_file.readlines()

# removendo o '\n' de cada item da lista usando list comprehencion:
lines = [line.replace('\n', '') for line in lines]

# visualização da variavel lines:
"""
for c in lines:
	print(c)
"""

# tabelas de simbolos para o analisador:

# VARIAVEIS:
var = {
}

# FUNÇÕES:
def get_input(variavel):
	var[variavel] = input('Insira um valor: ')

def atribuicao(variavel, valor):
	var[variavel] = int(valor) 

def soma(variavel, valor1, valor2):
	var[variavel] = int(valor1) + int(valor2)

def subtra(variavel, valor1, valor2):
	var[variavel] = int(valor1) - int(valor2)

def mult(variavel, valor1, valor2):
	var[variavel] = int(valor1) * int(valor2)

def div(variavel, valor1, valor2):
	var[variavel] = int(valor1) / int(valor2)

def mod(variavel, valor1, valor2):
	var[variavel] = int(valor1) % int(valor2)

# PALAVRAS RESERVADAS:
pal_res = {
	'G': get_input,
	'=': atribuicao,
	'+': soma,
	'-': subtra,
	'*': mult,
	'/': div,
	'%': mod
}

# CÓDIGO EM SI:
"""
	- O código a seguir lê as linhas do arquivo 
	- para cada palavra reservada o código segue algumas ações que são as funções 
	  presentes nos valores da variavel pal_res.
"""

for line in lines:

	# armazenando os caracteres da linha em uma variavel lista sem os espaços em branco
	chars = list(line[1:].replace(" ", ""))

	print(f'Char Base: {chars}')
	for i in range(1, len(chars)):
		if chars[i] in var.keys():
			chars[i] = var[chars[i]]


	"""
		o código a seguir pega o primeiro caracter da linha e o usa como key 
		no dicionário de pal_res inserindo os demais cacteres como parametros 
		para a função que o pal_res retorna. 
	"""
	pal_res[line[0]](*chars)

	# visualização:
	print(f'Os chars são: {chars}')
	print(f'As variaveis atualmente são: {var}')