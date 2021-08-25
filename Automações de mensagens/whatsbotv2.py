# Basicamente essa estrutura da seguinte forma 

# 1 Navega até seu Whats 

# 2 Busca o contato ou Grupo 

# 3 Envia as mensagens para o selecionado 

import os
import time
import base64

from json import loads
from json import dumps

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Caminho até o Zap
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')

time.sleep(3)

canvas = driver.find_element_by_xpath('//canvas[contains(@aria-label, "Scan me!")]')

# get the canvas as a PNG base64 string
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

# decode
canvas_png = base64.b64decode(canvas_base64)
time.sleep(3)
# save to a file
with open(r"canvas.png", 'wb') as f:
    f.write(canvas_png)

time.sleep(5)
cookies = driver.get_cookies()
if not os.path.isfile('cookies.txt'):
    with open('cookies.txt', 'w') as f:
        f.write(dumps(cookies))
else:
    with open('cookies.txt', 'r') as f:
        cookies = loads(f.read())
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.refresh()
time.sleep(5)

# escolher contato ou grupo
contatos = ['Contato para enviar a msg']
mensagem = ['Mensagem a ser enviada']


# Definição do contato
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


# Definição da mensagem
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# pesquisa copyable-text selectable-text

# campo de mensagens "copyable-text selectable-text" como o campo de mensagem é igual coloca a chave em [1] tendo em vista que o Python
# lê de 0 a 1
