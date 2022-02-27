
class Eleitor():
    cod_classe = 0
    def __init__(self,nome_usuario,matricula_usuario,data_adimicao):
        self._nome = str(nome_usuario).capitalize()
        self._matricula = int(matricula_usuario)
        self._adimissao = data_adimicao
        self._tipo_hierarquia = 0 # Código de conferência se o Objeto é eleitor

    @property
    def nome_eleitor(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula

    @property
    def data_admissao(self):
        return self._adimissao

    def dados_eleitor(self):
        print(f'Dados do usuário:\n',f'    Nome: {self._nome}:\n',
              f'    Matrícula: {self._matricula}\n',f'    Data de adimissão: {self._adimissao}')

    @classmethod
    def cod_classe_w(cls):
        return f'{cls.cod_classe}'

    @property
    def tipo_hierarquia(self):
        return self._tipo_hierarquia

class Candidato(Eleitor):
    def __init__(self,nome_usuario,matricula_usuario,data_adimicao):
        super(Candidato, self).__init__(nome_usuario,matricula_usuario,data_adimicao)
        self._eleitores = []
        self._tipo_hierarquia = 1
        print(f'{self._nome} foi adicionado como candidato com sucesso')

    # def ver_eleitores(self,nome_usuario : 'Colocar o objeto Eleitor, Canditado ou COmissão'):
    #     if(nome_usuario.tipo_hierarquia >= 1):
    #         print('Os eleitores são:')
    #         for x in range(0,len(self._eleitores)):
    #             print(f'    {self._eleitores[x].nome_eleitor}')
    #     else:
    #         print(f'O usuário {nome_usuario.nome_eleitor} não tem acesso a essa informação')
    #
    # def votar(self,nome_usuario : 'Objeto Eleitor ou Candidato'):
    #     if(len(self._eleitores) == 0 or not nome_usuario in self._eleitores):
    #         self._eleitores.append(nome_usuario)
    #         print('Voto computado')
    #     else:
    #         print(f'O eleitor {nome_usuario.nome_eleitor} já votou. Esse voto não será computado')


class ComissaoEleitoral():
    cod_classe = 2 # Código de conferência se o Objeto é Comissão eleitoral
    def __init__(self,membros : 'Inserir a variável do Objeto Eleitores',vigencia_cipa):
        self._vigencia = vigencia_cipa
        self._membros = membros
        self._tipo_hierarquia = 1  # Código de conferência se o Objeto é Comissão eleitoral

    @property
    def vigencia(self):
        return self._vigencia

    @property
    def membros(self):
        return self._membros.dados_eleitor

    @property
    def tipo_hierarquia(self):
        return self._tipo_hierarquia

class Eleicao():
    def __init__(self,descricao,data_eleicao):
        self._descricao = str(descricao).capitalize()
        self._data_eleicao = str(data_eleicao)
        self._votos = {}
        self._eleitores_totais = []
        self._candidatos_totais = []
        self._membros_cipa_total = []
        self._conferencia_candidato = []
        self._conferencia_voto = []
        print(f'A {self._descricao} foi criada')

    @property
    def descricao_cipa(self):
        return self._descricao

    def adicionar_candidato(self,nome_candidato):
        if (len(self._candidatos_totais) == 0 or not nome_candidato in self._candidatos_totais
                and nome_candidato.tipo_hierarquia == 1):
            self._candidatos_totais.append(nome_candidato)
            print('Canditado adicionado')
        else:
            print(f'O candidato {nome_candidato.nome_eleitor} já costa como cadastrado, ou você tentou adicionar um nome que NÃO É CANDIDATO\n',
                  'Favor inserir {} candidato'.format('outro'.upper()),sep='')

    def adicionar_eleitores(self,nome_eleitor):
        if (len(self._eleitores_totais) == 0 or not nome_eleitor in self._eleitores_totais):
            self._eleitores_totais.append(nome_eleitor)
            print('Eleitor adicionado')
        else:
            print(f'O eleitor {nome_eleitor.nome_eleitor} já costa como castrado. Favor inserir outro eleitor')

    def adicionar_membro_cipa(self,nome_eleitor):
        if (len(self._membros_cipa_total) == 0 or not nome_eleitor in self._membros_cipa_total):
            self._membros_cipa_total.append(nome_eleitor)
            print(f'Obrigado, membro da CIPA {nome_eleitor} adicionado com sucesso')
        else:
            print(f'O membro {nome_eleitor.nome_eleitor} já costa como castrado. Favor inserir outro eleitor')


        #self._membros_cipa_total

    def ver_eleitores(self,nome_usuario : 'Colocar o objeto Eleitor, Canditado ou COmissão'):
        if(nome_usuario.tipo_hierarquia >= 1):
            print('Os eleitores são:')
            for x in range(0,len(self._eleitores_totais)):
                #print(f'    {self._eleitores_totais[x].nome_eleitor}')
                return self._eleitores_totais[x].dados_eleitor
        else:
            print(f'O usuário {nome_usuario.nome_eleitor} não tem acesso a essa informação')

    def votar(self,nome_usuario : 'Objeto Eleitor ou Candidato', nome_candidato):
        if(len(self._eleitores_totais) != 0 and nome_usuario in self._eleitores_totais or nome_usuario in self._candidatos_totais
                and nome_candidato in self._candidatos_totais and nome_usuario not in self._votos):
            self._votos[nome_usuario] = nome_candidato
            self._conferencia_voto.append(nome_candidato)
            # self._votos = {}
            # self._eleitores_totais.append(nome_usuario)
            print('Voto computado')

        elif(nome_candidato not in self._candidatos_totais):
            print('O candidato escolhido, não consta na lista de candidatos')

        else:
            print(f'O eleitor {nome_usuario.nome_eleitor} já votou. Esse voto não será computado')

    def conferir_votos(self,nome_usuario):
        if(nome_usuario.tipo_hierarquia >= 1):
            for x in self._eleitores_totais:
                if(x in self._votos):
                    print(f'O candidato {x.nome_eleitor} teve {self._conferencia_voto.count(x)} votos')

                    # canditado = x
                    # voto = self._votos.get(x)
                    # self._conferencia_candidato.append(canditado)
                    # self._conferencia_voto.append(voto)

                    #self._conferencia_candidato = []
                    #self._conferencia_voto = []

                else:
                    print(f'O candidato {x.nome_eleitor} não teve votos')
                    #print('Não tem')
            for imprimir in range(0,len(self._conferencia_candidato)):
                print(f'Canditado {self._conferencia_candidato[imprimir]}, votos: {self._conferencia_voto[imprimir]}')

            # self._votos = {}
            # self._eleitores_totais = []
            # self._candidatos_totais = []

        else:
            print(f'O usuário {nome_usuario.nome_eleitor} não tem acesso a essa informação')






# 1º Eleitores: #matriculas tem que ser diferentes
ronaldo = Eleitor('ronaldo','001','12/01/2021')
marcelo = Eleitor('marcelo','002','01/01/2021')
luana   = Eleitor('luana','003','05/11/2019')
joana   = Eleitor('joana','004','03/07/2018')

# 2º Criar os candidatos:
arnaldo = Candidato('arnaldo','005','12/02/2018')
fernanda = Candidato('fernanda','006','01/02/2017')

# 3º Criar a eleição:
eleicao = Eleicao('Eleição CIPA 2022','01/01/2022')

# 4º Adicionar os canditados criados a eleição:
eleicao.adicionar_candidato(arnaldo)
eleicao.adicionar_candidato(fernanda)

# 5º Adicionar os eleitores criados a eleição:
eleicao.adicionar_eleitores(ronaldo)
eleicao.adicionar_eleitores(marcelo)
eleicao.adicionar_eleitores(luana)
eleicao.adicionar_eleitores(joana)

# 6º Comissão eleitoral votação:
rafael = ComissaoEleitoral('rafael','31/01/2022')

# 7º Iniciar votação:
eleicao.votar(luana,luana)
eleicao.votar(luana,arnaldo)
eleicao.votar(luana,arnaldo)
eleicao.votar(arnaldo,arnaldo)
eleicao.votar(arnaldo,arnaldo)

eleicao.conferir_votos(rafael)

