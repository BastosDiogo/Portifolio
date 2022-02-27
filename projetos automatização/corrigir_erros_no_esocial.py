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
unidade_adp = input('Digitar unidade ADP: ')
print('Por fim, digite o total de erros a serem corrigidos')
erros = input('Todal de erros: ')
erros = int(erros)

pyautogui.alert("O programa será iniciado, clique em 'OK'" )
navegador = webdriver.Chrome()
site = r'https://www.adpweb.com.br/ssonns/login_v2.asp'
site_login = r'https://expert.brasil.adp.com/ipclogin/1/loginform.html?TYPE=33554433&REALMOID=06-000a1470-e058-1656-b22f-441e0bf0d04d&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=jKCbBo2iXmPsA0rq7iagICXFbbwYt9UvfBpgtMIzDmy9OoXI6rviphUJYrlLzFqY&TARGET=-SM-HTTPS%3a%2f%2fexpert%2ebrasil%2eadp%2ecom%2fadpweb%2flogin_expert_v2%2easp%3fenv%3d%26app%3d'
navegador.get(site_login)

campo_usuario = r'//*[@id="login"]'
campo_senha = r'//*[@id="login-pw"]'
botao_enter = r'/html/body/div/div/section[1]/div/form/div[3]/div/button'

# Entrar com logging e senha
navegador.find_element(By.XPATH, campo_usuario).send_keys(f'{loging}')
navegador.find_element(By.XPATH, campo_senha).send_keys(f'{senha}')
navegador.find_element(By.XPATH, botao_enter).send_keys(Keys.ENTER)

pyautogui.click(798,417)
pyautogui.hotkey('ctrl','a')
pyautogui.write(unidade_adp)
time.sleep(1)
pyautogui.click(871,409)
time.sleep(5)
pyautogui.click(867,431)

time.sleep(2)
pyautogui.doubleClick(502, 38) # Maximizar a tela
time.sleep(2)

pyautogui.moveTo(209,208)
time.sleep(5)
pyautogui.click(263,276) # Selecionar o campo de "Administração de saúde"
time.sleep(5)

pyautogui.click(89,520) # Selecionar "e-Social"
time.sleep(5)

pyautogui.click(368,417) # Selecionar "Area de trabalho do eSocial"
time.sleep(10)

contador = 0
while(contador <= erros):
    pyautogui.click(258,601) # Clicar no primeiro erro"
    time.sleep(5)
    pyautogui.click(653,294) # Clicar na aba 'erro' "
    time.sleep(5)
    pyautogui.click(295,411) # Clicar 'situação' "
    time.sleep(5)
    pyautogui.click(370,446) # Escolher 'forçar envio' "
    time.sleep(5)
    pyautogui.click(451,454) # Clicar 'atribuir' "
    time.sleep(5)
    pyautogui.click(88,659) # Clicar 'concluido' "
    time.sleep(12)
    contador = contador + 1

pyautogui.alert("O programa foi finalizado com sucesso. Obrigado por utilizá-lo")
