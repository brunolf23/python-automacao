import pyautogui
import time

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(2)

# abrir linkedln, escrever login e senha
pyautogui.write("https://www.linkedin.com/feed/")
pyautogui.press("enter")

pyautogui.click("x=602, y=345")