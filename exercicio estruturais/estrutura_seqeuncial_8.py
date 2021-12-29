#Lista de exercícios - Estrutura Sequencial exercício 8. link:https://wiki.python.org.br/EstruturaSequencial
#Questão: "Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
# mostre o total do seu salário no referido mês.

print("Bem-vindo")

while(True):
    salario = input("Digite o valor do seu salário R$ ")
    if(salario.isdigit()):
        salario = float(salario)
        while(True):
            total_horas = input("Agora digite, o total de horas que você trabalhou no mês: ")
            if (total_horas.isdigit()):
                total_horas = int(total_horas)
                salario_hora = salario/total_horas
                print("Você ganha {} por hora".format(salario_hora))
                break

            else:
                print("", end="\n")
                print(("Digite apenas o valor numérico do total de horas"))
                print("Por exemplo: {}".format('Se você trabalha das 8h às 18h, deve digitar apenas "240", pois é o valor de 8h x 30 dias.'))
                input("Aperte {} para continuar".format('"enter"'.upper()))
                print("", end="\n")
        break

    else:
        print(("Digite apenas o valor numérico do seu salário"))
        input("Aperte {} para continuar".format('"enter"'.upper()))
        print("",end="\n")

print("Obrigado por usar a calculadora")
print(" ", end='\n')
input("Aperte {} para encerrar".format(""'enter'"".upper()))