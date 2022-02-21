import csv

print("Bem-vindo ao calculador de espaço em mémória")

while(True):
        print('Você preencheu os dados de entrada no narquivo "entrada.txt"?')
        print("sim ou não?")
        resposta = input("-> ")
        if('n' in resposta.lower() or resposta == '' or  resposta.isspace()):
                print("Por favor, volte e faça o preenchimento do arquivo, caso contário não será possível emitir"
                      " o relatório de espaço utilizado")
                print(' ', end='\n')
                input('Aperte {} para continuar'.format('"enter"'.upper()))
        else:
                nome_arquivo = 'entrada.txt'
                endereco =f'C:/Users/Diogo/Documents/GitHub/Portifolio/exercicio com arquivos/{nome_arquivo}'
                with open(endereco,encoding='latin-1',mode='r') as arquivo:
                        arquivo.seek(0)
                        lista = arquivo.readlines()
                        limpa = []
                        for dados in lista:
                                limpa.append(dados.rsplit(" ",1))

                numeros = []
                nomes = []
                total_numeros = 0
                for contador in range (0,len(limpa)):
                        numeros.append(float(limpa[contador][1]))
                        total_numeros = total_numeros + float(limpa[contador][1])
                        nomes.append(limpa[contador][0])

                percentual = []
                media_ocupacao = round(total_numeros/len(numeros),2)
                for valor in range(0,len(numeros)):
                        percentual.append(round((numeros[valor]*100/total_numeros),2))

                cabecalho = ['ACME Inc.;Uso do espaço em disco pelos usuários']
                separador = [' ']
                colunas =   ['Nr.Usuário;Espaço utilizado (MB);% do uso']

                nome_arquivo = 'saida.csv'
                endereco = f'C:/Users/Diogo/Documents/GitHub/Portifolio/exercicio com arquivos/{nome_arquivo}'
                with open(endereco,encoding='latin-1',mode='w+',newline= '') as arquivo_2:
                        arquivo_2.seek(0)
                        escrita = csv.writer(arquivo_2)#delimiter = ' ')
                        escrita.writerow(cabecalho)
                        escrita.writerow(separador)
                        escrita.writerow(colunas)

                        for contador in range(0, len(nomes)):
                                linhas = ['{};{:7.2f};{:7.2f}'.format(nomes[contador], numeros[contador] / 1000000, percentual[contador])]
                                escrita.writerow(linhas)

                        escrita.writerow([' '])
                        escrita.writerow(['Espaço total ocupado (MB):;{:7.2f}'.format(total_numeros / 1000000)])
                        escrita.writerow(['Espaço médio ocupado (MB):;{:.2f}'.format(media_ocupacao / 1000000)])

                break

input('O programa foi executado com sucesso, pressione {} para encerrar'.format('"enter"'.upper()))