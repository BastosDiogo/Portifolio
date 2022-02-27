from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

print('Insera seu loginng:')
loging = input('->')
print('Agora insera sua senha')
senha = input('-->')

pyautogui.alert("O programa será iniciado, clique em 'OK'" )
unidade_adp = ['052','056','057',
               '058','059','060','061','062','063','064','065','069','070','072','074','078','079','080','081',
               '083','084','088','089','090','107','108','109','118','119','130','134','135','136','139','140',
               '142','143','147','149','152','153','154']

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
    navegador.find_element(By.XPATH, botao_enter).send_keys(Keys.ENTER)
    for unidade in unidade_adp:
        pyautogui.click(906,399)      # Selecionar o campo de unidade adp
        pyautogui.hotkey('ctrl','a')
        pyautogui.write(unidade)  # Selecionar a unidade adp desejada
        time.sleep(1)
        pyautogui.click(1024,391)       # Dar 'enter' na unidade escolhida
        time.sleep(5)

        pyautogui.moveTo(209,208)       # mover o cursor pela primeira vez
        time.sleep(1)
        pyautogui.click(237, 312)        # Clicar na aba 'RH'
        time.sleep(5)
        pyautogui.click(240, 290)       # Clicar no 'Cadastro e Parâmestros'
        time.sleep(5)

        pyautogui.click(113, 339)       # Clicar na aba 'Tabelas e Fornecedores'
        time.sleep(3)

        pyautogui.click(336, 442)       # Clicar na aba 'Técnicas de Medida'
        time.sleep(3)

        roda = 0
        avalicao = 'AVALIAÇÃO QUALITATIVA'
        codigo_avaliacao = '12'
        while(roda <=1):
            pyautogui.click(91, 656)       # Clicar no botão 'incluir'
            time.sleep(3)
            pyautogui.click(326, 310)       # Clicar na caixa de texto  'Código'
            time.sleep(1)
            pyautogui.hotkey('ctrl','a')
            time.sleep(1)
            pyautogui.write(codigo_avaliacao)           # Digitar o código do Tipo de Avaliação
            time.sleep(1)
            pyautogui.click(490, 349)       # Clicar na caixa de texto  'Título'
            time.sleep(1)
            pyautogui.write(avalicao)       # Digitar o Título da avaliação
            time.sleep(1)
            pyautogui.click(450, 414)       # Clicar na caixa de texto  'Descrição'
            time.sleep(1)
            pyautogui.write(avalicao)       # Digitar a Descrição da avaliação
            time.sleep(1)
            pyautogui.click(408, 458)       # Clicar na bolinha 'Qualitativo'
            time.sleep(1)
            pyautogui.click(75, 656)       # Clicar no botão 'Concluir'
            time.sleep(2)
            roda = roda + 1
            avalicao = 'NR-17-RISCO ERGONÔMICO (QUALITATIVO)'
            codigo_avaliacao = '13'

        time.sleep(3)
        pyautogui.click(458, 146)  # Clicar para alterar acesso
        time.sleep(1)
        pyautogui.click(452, 181)  # Clicar em 'Seleção de cliente/empresa'
        time.sleep(3)

contador = contador + 1

pyautogui.alert("O programa foi finalizado com sucesso. Obrigado por utilizá-lo")