import pyautogui as py
import time

py.PAUSE = 0.3

# abrir o navegador (chrome)
py.press("win")
py.write("Chrome")
py.press("enter")
time.sleep(2)

# abrir linkedIn, digitar o email e senha (já deixei salvo o email e senha no navegador)
py.write("https://www.linkedin.com/home")
py.press("enter")
time.sleep(2)

# clica em buscar e digita python (no meu caso estou fazendo uma busca para conexões com pessoas que tbm usam python)
py.click(x=514, y=149)
py.write("headhunter")
py.press("enter")
time.sleep(5)

# clica na aba pessoas e depois clica em conectar (tem como configurar para mandar uma mensagem para pessoa)
py.click(x=435, y=342)
time.sleep(1)
py.click(x=1130, y=376)
time.sleep(1)
py.click(x=980, y=344)
#py.write(" digite uma msg ")
time.sleep(1)
py.click(x=1178, y=526)
