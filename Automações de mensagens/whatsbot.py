# Basicamente essa estrutura da seguinte forma 

# 1 Navega até seu Whats 

# 2 Busca o contato ou Grupo 

# 3 Envia as mensagens para o selecionado 


from selenium import webdriver 
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys  import Keys

# Caminho até o Zap
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(20)

# escolher contato ou grupo
contatos = ['seu contatos']
mensagem = ['Mansagem escolhida']

#Definição do contato
def buscar_contato(contato):
  campo_pesquisa =  driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
  time.sleep(3)
  campo_pesquisa.click()
  campo_pesquisa.send_keys(contato)
  campo_pesquisa.send_keys(Keys.ENTER)
  
#Definição da mensagem
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