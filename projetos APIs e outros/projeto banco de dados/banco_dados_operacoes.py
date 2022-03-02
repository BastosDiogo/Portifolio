import json
import requests

def cadastrar_cliente(nome, cpf, cidade):
    informacao = {"Nome": nome, "CPF": cpf, "Cidade": cidade}
    upload = json.dumps(informacao)
    requisicao = requests.post("https://cadastro-teste-c9246-default-rtdb.firebaseio.com/.json", data=upload)
    requisicao = requisicao.json()
    print(f'Cadastro realizdo com sucesso. Os dados do cliente {informacao["Nome"]} estão armazenados no local: {requisicao["name"]}\n')

def _getter_cliente(local_cliente : 'Link que advém da página de base de dados'):
    upload = local_cliente
    #requisicao = requests.get(f"{upload}/.json")
    requisicao = requests.get(f"https://cadastro-teste-c9246-default-rtdb.firebaseio.com/{upload}/.json")
    requisicao = requisicao.json()
    print(f'Os dados do cliente são:')
    for dado in requisicao:
        print(f'\t{dado}: {requisicao[dado]}')
    return requisicao

def mostrar_todos_clientes():
    requisicao = requests.get(f"https://cadastro-teste-c9246-default-rtdb.firebaseio.com/.json")
    requisicao = requisicao.json()
    contador = 1
    campos = ["Nome","CPF","Cidade"]
    for dados in requisicao:
        endereco = f"https://cadastro-teste-c9246-default-rtdb.firebaseio.com/{dados}/.json"
        requisicao_2 = requests.get(endereco)
        requisicao_2 = requisicao_2.json()
        print(f'{contador}º Dado:\n\tLocal: {dados}')
        for camp in range(0, len(campos)):
            print(f'\t\t{campos[camp]}: {requisicao_2[campos[camp]]}')
        contador += 1

def excluir_cliente(local_cliente : 'Link que advém da página de base de dados'):
    senha = input('Digite sua senha:\nSenha: ')
    teste = '123456'
    if(teste == senha):
        dados = _getter_cliente(local_cliente)
        print(f'Os daddos do cliente {dados["Nome"]} foram excluídos com sucesso.')
        requisicao = requests.delete(f"https://cadastro-teste-c9246-default-rtdb.firebaseio.com/{local_cliente}/.json")
    else:
        print('Sua senha está incorreta. Exclusão de dados {}.'.format("não realizada".upper()))

def atualizar_cliente():
    senha = input('Digite sua senha:\nSenha: ')
    teste = '123456'
    #mostrar_todos_clientes()
    if (teste == senha):
        local = input('\nSelecione o local a ser alterado:\nLocal Escolhido:')
        requisicao = requests.get(f"https://cadastro-teste-c9246-default-rtdb.firebaseio.com/.json")
        requisicao = requisicao.json()
        contador = 1
        campos = ["Nome", "CPF", "Cidade"]
        endereco = f"https://cadastro-teste-c9246-default-rtdb.firebaseio.com/{local}/.json"
        requisicao_2 = requests.get(endereco)
        requisicao_2 = requisicao_2.json()
        print(f'Dados selecionados:\n{requisicao_2}\n')
        print('Senha confirmada\nDigite "1" para alterar o nome do cliente\nDigite "2" para alterar o CPF\nDigite "3" para alterar a cidade\n')
        while (True):
            try:
                trocar = input('Digite a opção:')
                trocar = int(trocar)
                break
            except ValueError:
                print('Você não digitou uma oção válida. Por favor tente novamente')

        if (trocar == 1):
            novo_nome = input('Agora digite o novo NOME:\nNovo nome: ')
            requisicao_2['Nome'] = novo_nome
            print(requisicao_2)
            upload = json.dumps(requisicao_2)
            requisicao = requests.patch(endereco, data=upload)
            requisicao = requisicao.json()
            print(f'Atualização realizda com sucesso\n')

        elif(trocar == 2):
            novo_cpf = input('Agora digite o novo CPF:\nNovo CPF: ')
            requisicao_2['CPF'] = novo_cpf
            print(requisicao_2)
            upload = json.dumps(requisicao_2)
            requisicao = requests.patch(endereco, data=upload)
            requisicao = requisicao.json()
            print(f'Atualização realizda com sucesso\n')

        else:
            nova_cidade = input('Agora digite a nova CIDADE:\nNova Cidade: ')
            requisicao_2['Cidade'] = nova_cidade
            print(requisicao_2)
            upload = json.dumps(requisicao_2)
            requisicao = requests.patch(endereco, data=upload)
            requisicao = requisicao.json()
            print(f'Atualização realizda com sucesso\n')
    else:
        print('Sua senha está incorreta. Exclusão de dados {}.'.format("não realizada".upper()))
