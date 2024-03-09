import keyboard
import pyautogui as py
import time
import clipboard

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

# clica em buscar no linkedin e digita python (no meu caso estou fazendo uma busca para conexões com pessoas que tbm usam python)
py.click(x=514, y=149)
py.write("Python")
py.press("enter")
time.sleep(7)

# clica na aba pessoas
py.click(x=435, y=342)
time.sleep(1)

py.click(x=1130, y=376)
time.sleep(1)
py.doubleClick(1085, y=238) # seleciono o nome da pessoa para fazer uma copia
py.hotkey("ctrl", "c")
texto = clipboard.paste()
py.click(x=980, y=344)
time.sleep(2)
keyboard.write(f"Olá {texto},tudo bem? Obrigado pela conexão.") # Digite o texto junto com o nome da pessoa
time.sleep(1)
py.click(x=1178, y=526)
