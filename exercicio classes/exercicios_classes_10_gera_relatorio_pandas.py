# Faça um programa completo utilizando classes e métodos que:
# a-) Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#       tipoCombustivel.
#       valorLitro
#       quantidadeCombustivel
# b-) Possua no mínimo esses métodos:
#       abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#       abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#       alterarValor( ) – altera o valor do litro do combustível.
#       alterarCombustivel( ) – altera o tipo do combustível.
#       alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

import pandas as pd
from datetime import date

try:
    tabela = pd.read_csv('Registro de alterações.csv',encoding='latin_1')

except FileNotFoundError:
    colunas = ['Tipo combustível;Novo valor por litro;Data da alteração']
    df = pd.DataFrame(columns=colunas)
    df.to_csv('Registro de alterações.csv',encoding='latin_1',index=False)

class Posto_combustivel():
    def __init__(self,tipo_combustivel,valor_por_litro,tanque_litros):
        self.__tipo_combustivel = str(tipo_combustivel).capitalize()
        self.__valor_por_litro = valor_por_litro
        self.__tanque_litros = round(tanque_litros,2)

    @property
    def valor_por_litro(self):
        return self.__valor_por_litro

    @property
    def tanque_litros(self):
        return self.__tanque_litros

    @property
    def tipo_combustive(self):
        return self.__tipo_combustivel

    def abastaecer_por_litros(self,listros_para_abastercer):
        valor_pagar = listros_para_abastercer * self.valor_por_litro
        self.__tanque_litros = self.__tanque_litros - listros_para_abastercer
        return print('O veículo foi abastecido com {} litros de {}. Você deve pagar R$ {:.2f}\n'
                     .format(listros_para_abastercer,self.tipo_combustive,valor_pagar))

    def abastecer_por_valor(self,valor_para_abastecer):
        listros_para_abastercer = round(valor_para_abastecer/self.valor_por_litro,2)
        self.__tanque_litros = self.__tanque_litros - listros_para_abastercer
        return  print('O veículo foi abastecido com {} litros de {}. Você pagou R$ {:.2f}\n'
                      .format(listros_para_abastercer,self.tipo_combustive,valor_para_abastecer))

    def alterar_valor_combustivel(self,novo_valor_combustivel):
        data_atual = '{}/{:02d}/{}'.format(date.today().day,date.today().month,date.today().year)
        self.__valor_por_litro = novo_valor_combustivel
        atualizar = pd.read_csv('Registro de alterações.csv',encoding='latin_1')
        atualizar.loc[len(atualizar)] = [f'{self.tipo_combustive};{novo_valor_combustivel};{data_atual}']
        atualizar.to_csv('Registro de alterações.csv',encoding='latin_1',index=False)

        return print('O valor foi alterado para R$ {:.2f}\n'.format(self.__valor_por_litro))

# Exemplos funcionais:
gasolina = Posto_combustivel('gasolina',3.56,500)
gasolina.abastecer_por_valor(35.60)
gasolina.abastaecer_por_litros(10)
print(gasolina.tanque_litros,'\n')
gasolina.alterar_valor_combustivel(1.50)
gasolina.abastaecer_por_litros(10)

alcool = Posto_combustivel('Álcool',2.51,50)
alcool.alterar_valor_combustivel(2.54)
disel = Posto_combustivel('disel',1.25,60)
disel.alterar_valor_combustivel(0.98)
