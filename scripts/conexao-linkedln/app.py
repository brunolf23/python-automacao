import pyautogui
import time

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
time.sleep(2)

# abrir linkedln, escrever login e senha