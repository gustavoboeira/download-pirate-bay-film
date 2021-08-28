from time import time
import pyautogui


filme = input('Insira o nome do filme: ')

def botfilme(filme):
    pyautogui.alert('Código começando, não mexa em nada.')
    pyautogui.PAUSE = 1.5

    pyautogui.press('win')
    pyautogui.write('brave')
    pyautogui.press('enter')
    pyautogui.write('https://thepiratebay.org/index.html')
    pyautogui.press('enter')

    pyautogui.write(filme)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    pyautogui.press('enter')
    pyautogui.moveTo(935, 265)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.moveTo(1154, 216)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.press('win')
    pyautogui.write('utorrent')
    pyautogui.press('enter')

    pyautogui.moveTo(452, 219)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.moveTo(815, 440)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.moveTo(1086, 645)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

botfilme(filme)