
import os

def pedacos():
	dir = os.path.dirname(os.getcwd())

	base_file = open(f"{dir}/data/sourcefile.txt", "r")

	lines = base_file.readlines()

	lines = [line.replace('\n', '') for line in lines]


	var = {
	}

	for line in lines:

		chars = list(line[0:].replace(" ", ""))
		print(chars)

		for i in range(1, len(chars)):
			if chars[i] in var.keys():
				chars[i] = var[chars[i]]

		for ch in chars:
			print("\n", ch)
			if ch.isupper():
				print("Palavra Reservada")
			elif ch.islower():
				print("Variável")
			elif ch.isalnum():
				print('numero')
			elif '{' in ch or '}' in ch:
				print("delimitador")
			else:
				print('operador')
