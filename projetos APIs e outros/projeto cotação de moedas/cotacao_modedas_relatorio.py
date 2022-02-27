import requests
import pandas as pd
from datetime import date

cotacoes = requests.get(r'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()

moedas = ['USDBRL','EURBRL','BTCBRL']
classificacao = ['Alta','Atual','Baixa']

relatorio = {'Moeda':['USDBRL','EURBRL','BTCBRL'],'Alta':'','Atual':'','Baixa':''}
planilha = pd.DataFrame(relatorio)
names = ['high','bid','low']
imprir = {moedas[0]:'',moedas[1]:'',moedas[2]:''}
for tipo in range(0,len(moedas)):
    cotacao_alta = cotacoes[moedas[tipo]]['high']
    cotacao_atual = cotacoes[moedas[tipo]]['bid']
    cotacao_baixa = cotacoes[moedas[tipo]]['low']
    dados = [cotacao_alta,cotacao_atual,cotacao_baixa]
    print(f'Modea {moedas[tipo]}:',f'    Alta: {cotacao_alta}',f'    Atual: {cotacao_atual}',f'    Baixa: {cotacao_baixa}',sep='')

    for index in range(0,len(dados)):
        planilha.loc[tipo,classificacao[index]] = dados[index]
data_arquivo = '{}-{:02d}-{}'.format(date.today().day, date.today().month, date.today().year)
planilha.to_excel(f'Cotação_Moedas_{data_arquivo}.xlsx',index=False)
