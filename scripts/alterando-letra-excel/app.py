# adicionar uma letra dentro de uma lista

import pyautogui as py
import time

time.sleep(6)

while True:
    # copiar a coluna desejada e colar
    py.hotkey("ctrl", "c")
    time.sleep(1)
    py.hotkey("alt", "tab")
    time.sleep(1)
    py.hotkey("ctrl", "v")
    py.press("backspace")
    py.press("space")
    py.write("@")
    time.sleep(1)
    # copiar a segunda coluna desejada e colar
    py.hotkey("alt", "tab")
    py.press("left")
    py.hotkey("ctrl", "c")
    time.sleep(1)
    py.hotkey("alt", "tab")
    time.sleep(1)
    py.hotkey("ctrl", "v")
    # preparar para a rotação infinita
    py.hotkey("alt", "tab")
    py.press("down")
    py.press("right")
    time.sleep(1)