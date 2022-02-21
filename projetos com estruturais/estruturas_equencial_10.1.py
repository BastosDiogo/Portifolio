# Faça um Programa que deixe o usuário escolher qual temperatura converter
# em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (9C/5) + 32
# C = 5 * ((F-32) / 9)


print("***Bem-vindo ao conversor de temperatura***")
print("Por favor escolha qual conversão o tipo de conversão")
print("(1) Converter {} para {}".format('Celsius', 'Fahrenheit'))
print("(2) Converter {} para {}".format('Fahrenheit', 'Celsius'))

while (True):
    escolha = input("-> ")
    if (escolha.isdigit()):
        escolha = int(escolha)
        if (escolha == 1):
            print(" ", end='\n')
            print("Você escolheu o conversor de {} para {}".format('Celsius', 'Fahrenheit'))
            while(True):
                temp_cel = input("Por favor, digite {} o valor da temperatura em grau Celsius: ".format('apenas'.upper()))
                if (temp_cel.isdigit()):
                    temp_cel = float(temp_cel)
                    temp_fah = round(((9/5) * (temp_cel)) + 32,2)
                    print("A temperatura de {}°C graus Celsius equivale a {}°F graus Fahrenheit".format(temp_cel,temp_fah))
                    break
                else:
                    print(" ", end='\n')
            break

        elif (escolha == 2):
            print(" ", end='\n')
            print("Você escolheu o conversor de {} para {}".format('Fahrenheit','Celsius'))
            while(True):
                temp_fah = input("Por favor, digite {} o valor da temperatura em grau Fahrenheit: ".format('apenas'.upper()))
                if (temp_fah.isdigit()):
                    temp_fah = float(temp_fah)
                    temp_cel = round((5 * (temp_fah - 32)) / 9,2)
                    print("A temperatura {}°F graus Fahrenheit equivale a {}°C graus Celsius".format(temp_fah, temp_cel))
                    break
                else:
                    print(" ", end='\n')
        break

print("Obrigado por utilizar o conversor de temperatura")

print(" ", end='\n')
input("Aperte {} para encerrar".format(""'enter'"".upper()))