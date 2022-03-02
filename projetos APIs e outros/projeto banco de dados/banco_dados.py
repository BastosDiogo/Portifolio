import banco_dados_operacoes

print('Benvindo ao programa de atualização de dados do Banco de dados "Cadastro-Teste"\nLink do banco de dados:https://console.firebase.google.com/u/0/project/cadastro-teste-c9246/database/cadastro-teste-c9246-default-rtdb/data\n')
print('Para fruto de testes, utilize a senha:\n123456\n\nSelecione o que deseja fazer:')
print('Digite "1" para cadastrar cliente novos clientes\nDigite "2" para obter os dados de um cliente\n'
      'Digite "3" para todos os dados dos clientes\nDigite "4" para atualizar dos dados de um cliente\n'
      'Digite "5" para excluir um cliente\n')

while (True):
      try:
            opcao = input('Digite o número da opção desejada:\n')
            opcao = int(opcao)
            break
      except ValueError:
            print('Você não digitou uma oção válida. Por favor tente novamente')

if(opcao == 1):
      print('Por favor digite o NOME, CPF e a CIDADE do cliente')
      nome = input('Digete o NOME do cliente: ')
      cpf = input('Digete o CPF do cliente: ')
      cidade = input('Digete a CIDADE do cliente: ')
      banco_dados_operacoes.cadastrar_cliente(nome, cpf, cidade)
elif(opcao == 2):
      print('Para essa opção, você deverá ter o nome do local onde os dados do cliente estão salvos.'
            '\nVocê tem esse local?')
      s_ou_n = input('Digite "S" para sim ou "N" para não:\nDigite: ')
      if('s' in s_ou_n.lower()):
            print('Ok, Digite o local:')
            local = input('Local: ')
            banco_dados_operacoes._getter_cliente(local)
      else:
            print('Sem problemas, segue os dados dos clientes:')
            banco_dados_operacoes.mostrar_todos_clientes()
            local = input('\nDigite o local do cliente desejado:\n')
            banco_dados_operacoes._getter_cliente(local)

elif(opcao == 3):
      banco_dados_operacoes.mostrar_todos_clientes()

elif(opcao == 4):
      banco_dados_operacoes.atualizar_cliente()

elif(opcao == 5):
      print('Para essa opção, você deverá ter o nome do local onde os dados do cliente estão salvos.'
            '\nVocê tem esse local?')
      s_ou_n = input('Digite "S" para sim ou "N" para não:\nDigite: ')
      if ('s' in s_ou_n.lower()):
            print('Ok, Digite o local:')
            local = input('Local: ')
            banco_dados_operacoes.excluir_cliente(local)
      else:
            print('Sem problemas, segue os dados dos clientes:')
            banco_dados_operacoes.mostrar_todos_clientes()
            local = input('\nDigite o local do cliente desejado:\n')
            banco_dados_operacoes.excluir_cliente(local)


