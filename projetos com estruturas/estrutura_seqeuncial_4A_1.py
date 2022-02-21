#Evolução do exercício da Lista de exercícios - Estrutura Sequencial exercício 4. link:https://wiki.python.org.br/EstruturaSequencial

print("Bem-vindo")
total_de_numeros = 0
numeros = []
numeros_soma = 0
verifica_inteiro = 0

while(verifica_inteiro == 0):
    mensagem_inicio = float(input("Digite o total de valores: "))
    if(mensagem_inicio - round(mensagem_inicio) == 0):
        total_de_numeros = int(mensagem_inicio)
        for num in range(1,total_de_numeros+1):
            print("Digite {}° número:".format(num))
            add_numeros = float(input("-> "))
            numeros.append(add_numeros)
            numeros_soma = sum(numeros)
        print("A soma dos {} valores é {}".format(total_de_numeros,numeros_soma))
        media = numeros_soma/total_de_numeros
        print("A média desses valores é igual a {}".format(media))
        verifica_inteiro = 1

    else:
        print("Por favor digite um número inteiro")
        print(" ", end="\n")

print(" ", end='\n')
input("Obrigado por usar o programa! Aperte {} para encerrar".format(""'enter'"".upper()))