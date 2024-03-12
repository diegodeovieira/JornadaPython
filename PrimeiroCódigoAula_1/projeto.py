import pyautogui
import time

pyautogui.PAUSE = 0.8
pyautogui.time

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=478, y=354)
pyautogui.write('jornadapython@outlook.com')

pyautogui.press('tab')
pyautogui.write('passoword')

pyautogui.click(x=633, y=475)
time.sleep(3)

import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)


for linha in tabela.index:

    pyautogui.click(x=504, y=260)

    codigo = tabela.loc[linha, 'codigo']

    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']

    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']

    pyautogui.write(tipo)
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(1000)