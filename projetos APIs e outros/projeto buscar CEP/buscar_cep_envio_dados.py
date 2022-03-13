import requests
import pandas as pd

print('Seja bem-vido ao localizador de CEPs.')
tabela = pd.read_excel('Entrada.xlsx')
teste = [0 for abaixo_de_8 in tabela['CEP'] if len(str(abaixo_de_8)) < 8]

for dado in range(0,len(tabela)):
    if(0 in teste):
        print(f'A planilha que você está utilizando, está com um dado irregular no local {tabela["Local"][dado]}.\n')
        break
    else:
        cep = tabela['CEP'][dado]
        cep = str(cep).replace('.', '').replace('-', '')
        try:
            cep_api = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
            cep_api = cep_api.json()
            endereco = f"{cep_api['address']}, {cep_api['district']}, {cep_api['city']}, {cep_api['state']}"
            tabela.loc[dado, 'Endereço'] = endereco
            tabela.loc[dado, 'Estado'] = cep_api['state']
        except KeyError:
            print(f'O CEP {cep} não existe. Por favor altere sua planilha e tente novamente')
            break

print(f'\n{tabela}')
tabela.to_excel('Entrada.xlsx', index=False)
