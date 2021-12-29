#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que
# custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a-) comprar apenas latas de 18 litros;
# b-) comprar apenas galões de 3,6 litros;
# c-) misturar latas e galões, de forma que o desperdício de tinta seja menor.
#   Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

print(" ", end='\n')
print("EXERCÍCIO 17 - Estrutura Sequencial")
print("Link dos exercícios: https://wiki.python.org.br/EstruturaSequencial")
print(" ", end='\n')

print("Bem vido ao calculador de tintas")
print("Consideraçõs:")
print("1-) 1 litro para cada 6 metros quadrados. Ou seja 1L/ 6m²")
print("2-) Forma de venda das tintas:")
print("     I-)  latas de 18 litros, que custam R$ 80,00 cada")
print("     II-) Galões de 3,6 litros, que custam R$ 25,00 cada")

print("Você já tem o valor da área da parede?")
conta = input("{} ou {}? ".format("sim".capitalize(),"não".capitalize()))
if('n' in conta.lower()):
    print("Tudo bem, vou precisar do {} e {} da sua parede".format('comprimento'.upper(), 'largura'.upper()))
    print(" ", end='\n')
    while(True):
        comprimento = input("Por favor digite {} o valor do {} em metros: ".format('apenas'.upper(), 'comprimento'.upper()))
        largura = input("Agora, digite {} o valor da {} em metros: ".format('apenas'.upper(), 'largura'.upper()))
        print(" ",end='\n')
        try:
            if('-' not in comprimento and '-' not in largura):
                comprimento = float(comprimento.replace(",", "."))
                largura = float(largura.replace(",", "."))
                print("O {} da sua parade é {}m".format('comprimento'.upper(), comprimento))
                print("A {} da sua parade é {}m".format('largura'.upper(), largura))
                area_calculada = 0.01 if (comprimento * largura)<= 0.01 else round(comprimento * largura,2)
                print("A {} da sua parede é igua a {}m²".format('área'.upper(), area_calculada))
                break

            else:
                print(" ", end='\n')
                print("Você digitou valores não computáveis,por favor digite {} os valores das medidas".format('apenas'.upper()))
                print("Por exemplo, se sua parede tem 12,50m de largura e 3,70m de comprimento, digite:")
                print("12,50 e 3,70")
                print(" ", end='\n')

        except ValueError:
            print(" ", end='\n')
            print("Por favor digite {} os valores das medidas".format('apenas'.upper()))
            print("Por exemplo, se sua parede tem 12,50m de largura e 3,70m de comprimento, digite:")
            print("12,50 e 3,70")
            print(" ", end='\n')

else:
    print(" ", end='\n')
    while(True):
        area_usuario = input("Ok, digite então {} o valor da área em metros quadrados: ".format('apenas'.upper()))
        try:
            if ('-' not in area_usuario):
                area_usuario = float(area_usuario.replace(",", ".")) #Para aceitar números com ',' e transformar em '.'
                while (True):
                    print("Sua parede possui uma {} de {}m²?".format('área'.upper(), area_usuario))
                    print("Sim ou Não?")
                    conferir_area = input("-> ")
                    if('s' in conferir_area.lower()):
                        print("Ok, área computada")
                        break
                    else:
                        print("Nesse caso, redigite a área correta:")
                        area_usuario = input("-2> ")
                        area_usuario = float(area_usuario.replace(",", "."))
                break
            else:
                print(" ", end='\n')
                print("Por favor digite {} o valor da área".format('apenas'.upper()))
                print("Por exemplo, se sua parede tem 30,5m² área, digite:")
                print("30,5")
                print(" ", end='\n')

        except ValueError:
            print(" ", end='\n')
            print("Por favor digite {} o valor da área".format('apenas'.upper()))
            print("Por exemplo, se sua parede tem 30,5m² área, digite:")
            print("30,5")
            print(" ", end='\n')

print(" ", end='\n')
print("Tudo certo, de acordo com as considerações sitadas, para a área da sua parede temos os seguintes cenários")
print("Cenário a: Comprar apenas latas de 18 litros, sendo que cada uma custa R$ 80,00 (R$ 4,44/Litro)")
print("Cenário b: Comprar apenas galões de 3,6 litros, sendo que cada um custa R$ 25,00 (R$ 6,945/Litro)")
print("Cenário c: Misturar latas e galões")
input("Aperte {} para continuar".format(""'Enter'"".upper()))

if('n'in conta.lower()):
    litros_tinta = 0.1 if round(((area_calculada*1.10)/6),0) <= 0.1 else round(((area_calculada *1.10)/6),0)
    area_usada = 0.1 if area_calculada <= 0.1 else round(area_calculada,2)
else:
    litros_tinta = 0.1 if round(((area_usuario*1.10)/6),0) <= 0.1 else round(((area_usuario*1.10)/6),0)
    area_usada =   0.1 if area_usuario <= 0.1 else round(area_usuario,2)

print(" ", end='\n')
print("Sua parede de {}m², requer {}L de tinta".format(area_usada,litros_tinta))
print(" ", end='\n')

if(litros_tinta >= 2 and litros_tinta <= 10):
    cenario_a_latas = 1
    cenario_b_latas = round((litros_tinta / 3.6), 0) + 1 if (litros_tinta / 3.6) - round((litros_tinta / 3.6), 0) > 0\
        else round((litros_tinta / 3.6), 0)
    cenario_c_latas = 0

elif(litros_tinta < 2):
    cenario_a_latas = 1
    cenario_b_latas = 1
    cenario_c_latas = 0

elif (litros_tinta > 10 and litros_tinta < 19):
    cenario_a_latas = 1
    cenario_b_latas = round((litros_tinta / 3.6), 0) + 1 if (litros_tinta / 3.6) - round((litros_tinta / 3.6), 0) > 0\
        else round((litros_tinta / 3.6), 0)
    cenario_c_latas = 0

elif(litros_tinta >= 19):
    cenario_a_latas = round((litros_tinta / 18), 0) + 1 if (litros_tinta / 18) - round((litros_tinta / 18), 0) > 0\
        else round((litros_tinta / 18), 0)
    cenario_b_latas = round((litros_tinta / 3.6), 0) + 1 if (litros_tinta / 3.6) - round((litros_tinta / 3.6), 0) > 0\
        else round((litros_tinta / 3.6), 0)
    cenario_c_latas = round(litros_tinta / 18, 0)
    cenario_c_latas_2 = litros_tinta % 18

valor_a = cenario_a_latas * 80
valor_b = cenario_b_latas * 25 #cálculo do cenário c está mais abaixo

print("Cenário {}:".format('a'))
print("    {} latas de {}L.".format(cenario_a_latas,'18'))
print("    Total de R${:3.2f}.".format(valor_a))
input("Aperte {} para continuar".format(""'enter'"".upper()))
print(" ", end='\n')

print("Cenário {}:".format('b'))
print("    {} latas de {}L.".format(cenario_b_latas,'3.6'))
print("    Total de R${:3.2f}.".format(valor_b))
input("Aperte {} para continuar".format(""'enter'"".upper()))
print(" ", end='\n')

print("Cenário {}:".format('c'))
if(cenario_c_latas > 0):
    print("    {} latas de {}L.".format(cenario_c_latas, '18'))
    print("    {} latas de {}L.".format(cenario_c_latas_2, '3.6'))
    valor_c = (cenario_c_latas * 80) + (cenario_c_latas_2 * 25)
    print("    Total de R${:3.2f}.".format(valor_c))
else:
    print("Cenário c inviável".upper())
    print("Para calcular o cenário c seria necessário um volume mínio de 19L ou mais de tinta")
    print("Sua parede requer apenas {}L".format(litros_tinta))
    valor_c = 10000000000000

input("Aperte {} para continuar".format(""'enter'"".upper()))
print(" ", end='\n')

cenarios = {valor_a :"Cenário a",valor_b : "Cenário b", valor_c : "Cenário c"}
valores = [valor_a,valor_b,valor_c]
verificar = min(valores)
print("menor valor é", verificar)
print("O melhor cenário é o {}, com o valor de R${:3.2f}".format(cenarios[verificar], verificar))
print(" ", end='\n')
input("Obrigado por usar o programa! Aperte {} para encerrar".format(""'enter'"".upper()))
