from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

print('Insera seu loginng:')
loging = input('->')
print('Agora insera sua senha')
senha = input('-->')

print('Ok,agora digite a unidade ADP desejada')
nova_unidade = 'sim'
unidade_adp = []
while('s' in nova_unidade):
    unid_incluir = input('Digitar unidade ADP: ')
    unidade_adp.append(unid_incluir)
    nova_unidade = input('\nDeseja incluir uma nova unidade ADP? ')
    nova_unidade.lower()

lista_funcoes = ['20133','20134','20135','20136','20181','20304','20307','20309','20329','20335','20339','20341','20354','20355','20374','20379','20380','20381','20391','20399','20403','20404','20415']

pyautogui.alert("O programa será iniciado, clique em 'OK'" )
contador = 0
while(contador <= len(unidade_adp)):
    navegador = webdriver.Chrome()
    site = r'https://www.adpweb.com.br/ssonns/login_v2.asp'
    site_login = r'https://expert.brasil.adp.com/ipclogin/1/loginform.html?TYPE=33554433&REALMOID=06-000a1470-e058-1656-b22f-441e0bf0d04d&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=jKCbBo2iXmPsA0rq7iagICXFbbwYt9UvfBpgtMIzDmy9OoXI6rviphUJYrlLzFqY&TARGET=-SM-HTTPS%3a%2f%2fexpert%2ebrasil%2eadp%2ecom%2fadpweb%2flogin_expert_v2%2easp%3fenv%3d%26app%3d'
    navegador.get(site_login)
    preguica = 0
    while(preguica == 0):
        pyautogui.doubleClick(502, 38)  # Maximizar a tela
        time.sleep(2)
        preguica = preguica + 1

    campo_usuario = r'//*[@id="login"]'
    campo_senha = r'//*[@id="login-pw"]'
    botao_enter = r'/html/body/div/div/section[1]/div/form/div[3]/div/button'

    # Entrar com logging e senha
    navegador.find_element(By.XPATH, campo_usuario).send_keys(f'{loging}')
    navegador.find_element(By.XPATH, campo_senha).send_keys(f'{senha}')
    # navegador.find_element(By.XPATH, '/html/body/div/div/section[1]/div/form/div[3]/div/button').send_keys(Keys.ENTER)
    navegador.find_element(By.XPATH, botao_enter).send_keys(Keys.ENTER)
    for w in unidade_adp:
        pyautogui.click(906,399)      # Selecionar o campo de unidade adp
        pyautogui.hotkey('ctrl','a')
        pyautogui.write(w)  # Selecionar a unidade adp desejada
        time.sleep(1)
        pyautogui.click(1024,391)       # Dar 'enter' na unidade escolhida
        time.sleep(5)

        pyautogui.moveTo(209,208)       # mover o cursor pela primeira vez
        time.sleep(2)

        pyautogui.click(237, 287)       # Clicar no 'Administração de segurança'
        time.sleep(5)

        pyautogui.click(170, 314)       # Clicar na aba 'Mapeamento de Riscos e Lanc. Medições'
        time.sleep(3)
        pyautogui.scroll(-1000)
        time.sleep(1)

        pyautogui.click(362, 176)       # Clicar na aba 'Risco da função'
        time.sleep(3)
        print(f'Funções da undiade {w}')

        for x in lista_funcoes:
            pyautogui.click(496, 287)  # Selecionar a caixa de texto para digiar a função
            time.sleep(1)
            pyautogui.write(x)
            time.sleep(1)
            pyautogui.click(1262, 289)  # Clicar no botão 'pesquisar'
            time.sleep(3)
            pyautogui.click(88, 340)  # Selecionar a função digitada
            time.sleep(2)
            pyautogui.click(133, 364)  # Selecionar o risco
            time.sleep(3)
            pyautogui.click(752, 292)  # Selecionar a aba 'laudo'
            time.sleep(3)
            pyautogui.click(189, 465)  # Selecionar o 'cód. laudo'
            time.sleep(1)
            pyautogui.click(746, 296)  # Selecionar a aba 'Dados complementares'
            time.sleep(2)
            pyautogui.click(979, 591)  # Selecionar a lupa
            time.sleep(2)
            pyautogui.click(182, 316)  # Clicar no tipo de avaliação
            time.sleep(2)
            pyautogui.click(86, 655)  # Clicar no botão 'concluir' para dar ok no laudo.
            time.sleep(2)
            pyautogui.click(86, 655)  # Clicar no botão 'concluir' para dar ok no laudo.
            time.sleep(2.5)
            pyautogui.click(155, 657)  # Clicar no botão 'anterior' para retornar ao início e escolher uma nova função
            time.sleep(3)
            print(f'Função {x} incluida')

        time.sleep(4)
        pyautogui.click(458, 146)  # Clicar para alterar acesso
        time.sleep(2)
        pyautogui.click(452, 181)  # Clicar em 'Seleção de cliente/empresa'
        time.sleep(3)

contador = contador + 1

pyautogui.alert("O programa foi finalizado com sucesso. Obrigado por utilizá-lo")