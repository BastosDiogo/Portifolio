import requests

print('Seja bem-vido ao localizador de CEPs.')
while(True):
    try:
        cep = input('Digite o CEP desesejado, no formato xx.xxx-xxx.\nDigite o CEP: ')
        cep = cep.replace('.', '').replace('-', '')
        if(len(cep) == 8):
            teste = int(cep)
        else:
            raise ValueError

        break
    except ValueError:
        print('Você não digitou um valor válido.Por favor tente novamente.\n')

cep_api = requests.get(f' https://cep.awesomeapi.com.br/json/{cep}')
cep_api = cep_api.json()

endereco = f"{cep_api['address']}, {cep_api['district']}, {cep_api['city']}, {cep_api['state']}"

print(endereco)
