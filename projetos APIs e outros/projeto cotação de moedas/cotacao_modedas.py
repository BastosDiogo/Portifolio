import requests

cotacoes = requests.get(r'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json() # <----------- É um dicionário Pynton agora. Então temos que chamar pelo "Nome"

moedas = ['USDBRL','EURBRL','BTCBRL']
for tipo in range(0,len(moedas)):
    cotacao_alta = cotacoes[moedas[tipo]]['high']
    cotacao_atual = cotacoes[moedas[tipo]]['bid']
    cotacao_baixa = cotacoes[moedas[tipo]]['low']
    print(f'Modea {moedas[tipo]}:',f'    Alta: {cotacao_alta}',f'    Atual: {cotacao_atual}',f'    Baixa: {cotacao_baixa}',sep='')
