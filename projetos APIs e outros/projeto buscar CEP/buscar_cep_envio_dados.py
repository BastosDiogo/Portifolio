import requests
import pandas as pd

print('Seja bem-vido ao localizador de CEPs.')
tabela = pd.read_excel('Entrada.xlsx')
for dado in range(0,len(tabela)):
    cep = tabela['CEP'][dado]
    cep = cep.replace('.', '').replace('-', '')
    try:
        cep = cep.replace('.', '').replace('-', '')
        if(len(cep) == 8):
            teste = int(cep)
            print(f'CEP lido: {cep}')
        else:
            raise ValueError

    except ValueError:
        print(f'A planilha que você está utilizando, está com um dado irregular no local{tabela["Local"][dado]}.\n')

    cep_api = requests.get(f' https://cep.awesomeapi.com.br/json/{cep}')
    cep_api = cep_api.json()
    endereco = f"{cep_api['address']}, {cep_api['district']}, {cep_api['city']}, {cep_api['state']}"
    tabela.loc[dado, 'Endereço'] = endereco
    tabela.loc[dado, 'Estado'] = cep_api['state']

print(f'\n{tabela}')

tabela.to_excel('Entrada.xlsx',index=False)