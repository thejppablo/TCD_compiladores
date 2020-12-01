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

# visualização da variavel lines = ['G n', 'G p', '= i 3', '+ i i 1']

"""
for c in lines:
	print(c)
"""

# tabelas de simbolos para o analisador:
def remover_esp(lista):
    for x in lista:
        lista[lista.index(x)] = x[2:]

def chaves_while(linhas):
    lista_idx = []
    for x in linhas:
        if "{" in x:
            #print("tem", x, "index: ",linhas.index(x))
            lista_idx.append(linhas.index(x))
        elif "}" in x:
            #print("tem",x, "index: ",linhas.index(x))
            lista_idx.append(linhas.index(x))
    lista3 = linhas[lista_idx[0]+1:lista_idx[1]]
    remover_esp(lista3)
    print("LISTA3: ",lista3)
    return lista3


# VARIAVEIS:
var = {
}

# FUNÇÕES:
#obs: todos os parametros variavel são strings que se tornaram keys de um dicionario de "variaveis"

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

def printar(variavel):
	print(var[variavel])

def menor(variavel, valor):
	return int(var[variavel]) < int(valor)

def diferente(variavel,valor):
	return int(var[variavel]) != int(valor)

def repeticao(variavel, chave, valor,parentesis): #parms: ('i', '#', 'n')
	listaWhile = chaves_while(lines)
	while pal_res[chave](variavel,valor):
		for x in listaWhile:
			charss = list(x[1:].replace(" ", ""))
			for i in range(1, len(charss)):
				if charss[i] in var.keys():
					charss[i] = var[charss[i]]
			pal_res[x[0]](*charss)

# PALAVRAS RESERVADAS:
pal_res = {
	'G': get_input,
	'=': atribuicao,
	'+': soma,
	'-': subtra,
	'*': mult,
	'/': div,
	'%': mod,
	'<': menor,
	'#': diferente,
	'P': printar,
	'W': repeticao,
	'I': 'if'
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

	#print(f'Char Base: {chars}')
	for i in range(1, len(chars)):
		if chars[i] in var.keys():
			chars[i] = var[chars[i]]


	"""
		o código a seguir pega o primeiro caracter da linha e o usa como key 
		no dicionário de pal_res inserindo os demais cacteres como parametros 
		para a função que o pal_res retorna. 
	"""
	#print("linha zero: ",line[0])
#			line[0] é o primeiro char da linha atual
	#print("VARIAVEIS:",var)
	try:
		pal_res[line[0]](*chars)
	except KeyError:
		continue

	# visualização:
	#print(f'Os chars são: {chars}')
	print(f'As variaveis atualmente são: {var}')