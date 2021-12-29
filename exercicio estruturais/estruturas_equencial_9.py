#Lista de exercícios - Estrutura Sequencial exercício 9. link:https://wiki.python.org.br/EstruturaSequencial
#Questão: "Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em
#graus Celsius
#C = 5 * ((F-32) / 9).

print("Bem-vindo")
print("Por favor insira {} a temperatura".format('apenas'.upper()))
while(True):
	temp_frah = input("Temperatura em Fahrenheit: ")
	if(temp_frah.isdigit()):
		temp_frah = float(temp_frah)
		temp_cel = round((5 * (temp_frah - 32)) / 9,2)
		print("A temperatura {}°F graus Fahrenheit equivale a {}°C graus Celsius".format(temp_frah,temp_cel))
		break

	else:
		print(" ", end = '\n')
		print("Por favor, digite apenas o valor numérico da temperatura em Fahrenheit")
		input("Aperte {} para continuar".format('enter'.upper()))
		print(" ", end='\n')

print("Obrigado por utilizar o conversor de temperatura")

print(" ", end='\n')
input("Aperte {} para encerrar".format(""'enter'"".upper()))