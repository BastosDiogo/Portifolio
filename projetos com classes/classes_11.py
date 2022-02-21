# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#
# Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível
# no tanque.
# O consumo é especificado no construtor e o nível de combustível inicial é 0.
# Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
# meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
# meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
# meuFusca.andar(100);            # anda 100 quilômetros.
# meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.

class Carro():
    def __init__(self,nome_do_carro,km_x_Litro):
        self.__nome_do_carro = str(nome_do_carro).capitalize()
        self.__km_x_Litro = float(km_x_Litro)
        self.__tanque_capacidade = 0

    @property
    def tanque_capacidade(self):
        return round(self.__tanque_capacidade,1)

    @property
    def km_x_Litro(self):
        return self.__km_x_Litro

    @property
    def nome_docarro(self):
        return self.__nome_do_carro

    def abastecer(self,combustivel): # Método para adicionar combustível
        self.__tanque_capacidade = self.__tanque_capacidade + combustivel
        return f'Seu tanque foi abastecido com {combustivel}.'

    def nivel_combustivel(self):
        return f'O nível de combustível do seu carro é {round(self.__tanque_capacidade,1)} Litros'

    def andar(self,distancia_percorrida):
        self.__tanque_capacidade = self.__tanque_capacidade - (self.km_x_Litro/distancia_percorrida)

    def __str__(self):
        return f'O carro {self.nome_docarro}, faz {self.km_x_Litro} Km/L, ' \
               f'está atualmente com {self.tanque_capacidade} Litros de combustível'

fusca = Carro('Picape Sandero',15)
fusca.abastecer(20)
fusca.andar(100)
print(fusca.nivel_combustivel(),'\n')
print(fusca)