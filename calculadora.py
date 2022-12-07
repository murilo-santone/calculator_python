# Imports
import os  # import usado para limpar a tela
import time  # import usado para aguardar 2s antes de finalizar o programa

# Calculadora em Python

# Funções lambda
soma = lambda x, y: x + y 
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y

# Funções def
def limpaConsole():
	'''Limpa tela do console em execução'''
	if os.name in ('nt', 'dt'): # Se maquina estiver rodando Windows, use cls
		c = 'cls'
	os.system(c)

# Variavel Global
bol = True

# Loop de repetição
while bol == True:

	# Menu
	print('--> Calculadora em Python')
	print('--------------------------------')
	print('\n-> 1 Soma')
	print('-> 2 Subtração')
	print('-> 3 Multiplicação')
	print('-> 4 Divisão\n')

	# Variavel local recebe operação a ser realizada
	operacoes = int(input('Qual operação precisa fazer? '))

	# Condicional
	if operacoes == 0 or operacoes >= 5:
		print('\nNúmero inválido informe novamente.\n')
		time.sleep(1)
	else:		
		x = float(input('\n-> Informe o primeiro número: '))
		y = float(input('-> Informe o segundo número: '))
		if operacoes == 1:
			r = soma(x, y)
			print(f'\nResultado entre {x} + {y}: {r}')
		elif operacoes == 2:
			r = subtracao(x, y)
			print(f'\nResultado entre {x} - {y}: {r}')
		elif operacoes == 3:
			r = multiplicacao(x, y)
			print(f'\nResultado entre {x} * {y}: {r}')
		elif operacoes == 4:
			r = 0
			if y == 0:
				try:  # Tratamento de erro
					r = divisao(x, y)
				except ZeroDivisionError:
					print('\nDivisor não pode ser 0 ou menor que 0.')
					print('Recomece sua operação.\n')
			print(f'\nResultado entre {x} / {y}: {r}')
	
		print('''\n\n--> Deseja fazer outra operação?
		\n-> 1 Sim
		\n-> 2 Não \n''') 
		
		outra = int(input('Informe aqui: '))
		
		if outra == 2:
			# Limpando tela antes de finalizar
			limpaConsole()
			print('Finalizando Calculadora...')
			# aguarda 2s 
			time.sleep(2)	
			# Finalizando loop
			bol = False	