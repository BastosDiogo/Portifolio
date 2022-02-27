from classes_ import Eleicao,Eleitor,Candidato,ComissaoEleitoral
import pandas as pd

print('Bem vindo ao programa de eleição da CIPA\n','Para fazer a eleição, vamos seguir algumas etapas. São elas:',sep='')
print('    1°) Criar a elição\n','    2°) Inserir os membros da comissão eleitoral\n',
      '    3°) Inserir os candidatos\n','    4°) Inserir os eleitores\n',sep='')

input('Pressione {} para continuar'.format("'enter'".upper()))
print('Muito bem, vamos criar a eleição da CIPA, para isso, digite o ano da eleição.\n')

while(True):
      print('Digite o ano da eleição:')
      ano = input('->')
      print('Obrigado pelo envio, agora digite a data da eleição, no formato dd/mm/aaaa.\n','Digite a data:',sep='')
      data = input('->')

      print(f'Ok, muito obrigado. Apenas para confirmar, o ano da sua eleição foi {ano} e a data foi {data}?')
      print('Digite "S" para sim e "N" para não')
      s_ou_n = input('->')
      s_ou_n = s_ou_n.lower()

      if(not ano.isspace() and not data.isspace() and len(ano) != 0  and len(data) != 0):
            if('s' in s_ou_n):
                  try:
                        eleicao = Eleicao(ano, data)
                        break
                  except TypeError:
                        print('Você digitou o ANO ou a DATA no formato não adequado.\n', 'Por favor tente novamente\n', '\n',sep='')
            else:
                  print('Tudo bem então\n')
      else:
            print('Você digitou valores embranco\n')

tabela = pd.read_excel('Base_eleitores_teste.xlsx')
total_eleitores = tabela[tabela.columns[0]].count() #ou  total_eleitores = len(tabela.index)
eleitores = []
candidatos = []
for cont in range(0,total_eleitores):
      nome_eleitor = tabela.loc[cont,'Nome']
      matricula_eleitor = tabela.loc[cont,'Matrícula']
      data_admissao_eleitor = tabela.loc[cont,'Data de admissão']
      tipo_eleitor = tabela.loc[cont,'Candidato']
      eleitor = Eleitor(nome_eleitor,matricula_eleitor,data_admissao_eleitor)
      print(nome_eleitor,matricula_eleitor,data_admissao_eleitor)
      eleitores.append(eleitor)
      eleicao.adicionar_eleitores(eleitor)
      if('s' in tipo_eleitor or 'S' in tipo_eleitor):
            candidato = Candidato(nome_eleitor,matricula_eleitor,data_admissao_eleitor)
            candidatos.append(candidato)
      else:
            pass

print('Qual dessas pessoas, fazem parte da Comissão Eleitora?')
for cont in range(0,len(eleitores)):
      print(f'{cont+1}-) {eleitores[cont].nome_eleitor}')
print(f'{cont+2}-) Nenhuma dessas pessoas acima')
comissao_membros = []
while(True):
      opcao = input('Digite o número da opção: ')
      try:
            opcao = int(opcao)
            break
      except ValueError:
            print('Você inseriu um número não exsitente nas opções\n','digite novamente a opção',sep='')

if(opcao == cont+2):
      print('Então, por favor insira a quantidade de Membros da Comissão Eleitoral')
      quantidade = input('Digite o número de membros: ')
      quantidade = int(quantidade)
      for cont in range(0,quantidade):
            print('\nInsira o nome do membro:')
            nome_eleitor = input('Nome do membro: ')
            print('\nInsira o matrícula do membro:')
            matricula_eleitor = input('Matrícula do membro: ')
            print('\nInsira o data de admissao do membro:')
            data_admissao_eleitor = input('data de admissão dd/mm/aaaa: ')
            eleitor = Eleitor(nome_eleitor,matricula_eleitor,data_admissao_eleitor)
            comissao = ComissaoEleitoral(eleitor,ano)
            comissao_membros.append(comissao)
            print(f'Ok, membro {nome_eleitor} adicionado com sucesso')


else:
      while('s' in s_ou_n.lower()):
            opcao = opcao - 1
            eleitor = eleitores[opcao]
            comissao = ComissaoEleitoral(eleitor, ano)
            comissao_membros.append(comissao)
            print(f'\nEleitor {eleitor.nome_eleitor} foi adicionado com sucesso\n',
                  'Deseja adiconar mais algum membro da Comissão eleitoral?', sep='')
            s_ou_n = input('Digite "S" para sim ou "N" para não: ')
            print('\nOk, digite o número da opção:')
            while(True):
                  opcao = input('Digite o número: ')
                  try:
                        opcao = int(opcao)
                        break
                  except ValueError:
                        print('Você inseriu um número não exsitente nas opções\n','digite novamente a opção',sep='')

            if(opcao > len(eleitores)):
                  print('Você escoulher a opção "Nenhuma das opções acima" isso não é uma opção válida',
                        'Deseja adiconar mais algum membro da Comissão eleitoral?\n')
                  s_ou_n = input('Digite "S" para sim ou "N" para não: ')
            else:
                  pass
print('Ok, agora que acabamos de inserir a Comissão elitoral devido a sua base de funcionários, vamos inserir os canditados')
print('Verifique se eleitores:')
print('Os candidatos são:\n')

for cand in range(0,len(candidatos)):
      print(f'    {cand+1}-) {candidatos[cand].nome_eleitor}')
while(True):
      print('\nExiste mais algum outro candidato?')
      s_ou_n = input('Digite "S" para sim ou "N" para não: ')
      if('s' in s_ou_n.lower()):
            print('\nInsira o nome do candidato:')
            nome_candidato = input('Nome do candidato: ')
            print('\nInsira o matrícula do candidato:')
            matricula_candidato = input('Matrícula do candidato: ')
            print('\nInsira o data de admissao do membro:')
            data_admissao_candidato = input('data de admissão dd/mm/aaaa: ')
            candidato = Candidato(nome_candidato, matricula_candidato, data_admissao_candidato)
            candidatos.append(candidato)
            break
      else:
            print('Ok, sem mais candidatos. Vamos verficar as etapas\n')


print('São sela:','    1°) Criar a elição\n','    2°) Inserir os membros da comissão eleitoral\n',
      '    3°) Inserir os candidatos\n','    4°) Inserir os eleitores\n',sep='')

print('1°) Criar a elição:',f'    Eleição criada: {eleicao.descricao_cipa}',sep='')
print('\n2°) Inserir os membros da comissão eleitoral. Membros da Comissão')
for index in range(0,len(comissao_membros)):
      print(f'{index + 1}-) {comissao_membros[index].membros}')
print('\n3°) Inserir os candidatos. Candidatos:')
for index in range(0,len(candidatos)):
      print(f'{index + 1}-) {candidatos[index].nome_eleitor}')
      num = index + 1
      num_candidatos = {candidatos[index].nome_eleitor: num}
print('\n4°) Inserir os eleitores. Eleitores:')
for index in range(0,len(eleitores)):
      print(f'{index + 1}-) {eleitores[index].nome_eleitor}')

print('\nAgora que está tudo pronto, vamos votar.')
while(True):
      opcao = input('Digite o número do seu candidato: ')
      try:
            opcao = int(opcao)
            break
      except ValueError:
            print('Você inseriu um número não exsitente nas opções\n', 'digite novamente a opção', sep='')

print('Para votar, basta digitar sua matrícula.')
for num_votacao in range(0,len(eleitores)):
      mat_confere = input('Digite sua matrícula: ')
      contem = False
      while(contem == False):
            for mat in range(0, len(eleitores)):
                  contem = True                      if mat_confere == eleitores[mat].matricula else False
                  nome = eleitores[mat].nome_eleitor if mat_confere == eleitores[mat].matricula else 0
            if(contem == True):
                  print(f'Sua matrícula foi identificada. {nome} pode votar')
                  votar = input('Digite o número do candidato: ')
                  if(votar in num_votacao):
                        print(f'Você votou em: {num_candidatos[votar]}')
                        votar = votar - 1
                        candidato_votado = candidatos[votar]

            else:
                  print('Sua matrícula não foi encontrada, você não pode votar.')





#
#
# print('\n',f'Agora que a eleição {eleicao.descricao_cipa} foi criada, vamos inserir a base de eleitores:',sep='')
# print('Qual é o total de eleitores?')
# while(True):
#       total_eleitores = input('->')
#       try:
#             total_eleitores = int(total_eleitores)
#             break
#       except ValueError:
#             print('Você digitou um valor inválido, por favor tente novamente')
#
# for cont in range(0,total_eleitores):
#       print(f'Por favor digite o nome do {cont+1}º eleitor')
#       nome_eleitor = input('->')
#       print('  Tudo bem, agora digite a matrícula do eleitor')
#       matricuala_eleitor = input('  -->')
#       print('  Perfeito, agora digite a matrícula do eleitor')
#       admicao_eleitor = input('  --->')
#
#       eleitor = Eleitor()
#
#
#
# print('\n',f'Agora que a eleição {eleicao.descricao_cipa} foi criada, vamos inserir os Membros da Comissão Elitoral:',sep='')
# print('Quantos membros são no total?')
# while(True):
#       total_memmbros = input('->')
#       try:
#             total_memmbros = int(total_memmbros)
#             break
#       except ValueError:
#             print('Você digitou um valor inválido, por favor tente novamente')
# membros_cipa = []
# for cont in range(0,total_memmbros):
#       print(f'Por favor digite o {cont+1}º membro')
#       nome_membro = input('->')
#       membro = ComissaoEleitoral(nome_membro,ano)
#
#       eleicao.adicionar_membro_cipa(membro)
#       membros_cipa.append(membro)
#
#       #print(f'O membro {nome_eleitor.nome_eleitor} já costa como castrado. Favor inserir outro eleitor')
#
