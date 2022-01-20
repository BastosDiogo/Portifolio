import pyautogui
import time

print('Por favor, insira a data do relatório no formato:')
print('dd/mm/aaaa. Exemplo: 11/01/2022')
print('Qualquer formato além disso, {} aceito'.format('não'.upper()))

data = input(".->")

print(' ')
pyautogui.PAUSE = 0.5
pyautogui.hotkey('winleft','d')
pyautogui.alert("O programa vai iniciar")
pyautogui.press('winleft')
time.sleep(1)
pyautogui.write('crome')
pyautogui.press('enter')

time.sleep(2)
pyautogui.doubleClick(1174, 47) # Maximizar a tela
time.sleep(2)

pyautogui.write(r'www.adpweb.com.br/ssonns/login_v2.asp')
time.sleep(2)
pyautogui.press('enter')

time.sleep(2)
pyautogui.click(668,483) # Entrou na ADP, ja com loging senha
time.sleep(2)
pyautogui.click(1019,382) # Escolheu a empresa 001 na ADP
time.sleep(2)
pyautogui.click(1023,396) # Entrou a empresa 001 na ADP
time.sleep(5)

pyautogui.moveTo(210,197)
time.sleep(3)
pyautogui.click(221,258) # Selecionar o campo de "Administração de saúde"
time.sleep(5)

pyautogui.click(91,506) # Selecionar "e-Social"
time.sleep(2)
pyautogui.click(358,428) # Selecionar "Inconsistências e-Social"
time.sleep(3)
pyautogui.click(174,327) # Selecionar o campo "Empresa"
time.sleep(1)
pyautogui.click(214,481) # Selecionar o campo "Todas as empresas"
time.sleep(1)
pyautogui.click(153,655) # Clicar no "concluir"
time.sleep(1)

pyautogui.click(389,398) # Campo de escrita da data
time.sleep(1)
pyautogui.write(data) #escrever a data
time.sleep(2)
pyautogui.click(91,654) # Clicar no "concluir"
time.sleep(1)
pyautogui.click(466,196) # Clicar em "processos"
time.sleep(1)

pyautogui.alert("O programa acabou")