
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
                with open('C:/Users/Diogo/Documents/GitHub/Portifolio/exercicio com arquivos/entrada.txt',
                          encoding='latin-1',mode='r') as arquivo:
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

                cabecalho = 'ACME Inc.               Uso do espaço em disco pelos usuários\n'
                separador = '-------------------------------------------------------------\n'
                colunas =   'Nr.Usuário              Espaço utilizado                % do uso\n'

                nomes_imprimir = []

                with open('C:/Users/Diogo/Documents/GitHub/Portifolio/exercicio com arquivos/relatório.txt',
                          encoding='latin-1',mode='a+') as arquivo_2:
                        arquivo_2.seek(0)
                        arquivo_2.writelines(cabecalho)
                        arquivo_2.writelines(separador)
                        arquivo_2.writelines('\n')
                        arquivo_2.writelines(colunas)
                        arquivo_2.writelines('\n')
                        for x in range(0,len(nomes)):
                                linhas = '{}            {:7.2f} MB                  {:7.2f}%\n'.format(nomes[x],numeros[x]/1000000,percentual[x]).replace('.',',')
                                arquivo_2.writelines(linhas)
                        arquivo_2.writelines('\n')
                        arquivo_2.writelines('Espaço total ocupado: {:7.2f} MB\n'.format(total_numeros/1000000).replace('.',','))
                        arquivo_2.writelines('Espaço médio ocupado: {:.2f}  MB\n'.format(media_ocupacao/1000000).replace('.',','))

                print(' ',end='\n')
                print(f'Seu relatporio foi criado e enviado para o local:C:/Users/Diogo/Documents/GitHub/Portifolio/exercicio com arquivos/,'
                      f' com o nome de relatório.txt')
                print(' ',end='\n')
                input('Aperte {} para continuar'.format('"enter"'.upper()))
                break