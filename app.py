from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


# colocar o valor na planilha

# abrir o navegador
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# acessar o site
driver.get('https://sitepreco1.netlify.app/')

# encontrar o abacate
# anotar o valor
precos_site_1 = driver.find_elements(By.XPATH, '//h6[@class="price_heading"]')
preco_final_site_1 = precos_site_1[3].text.split(' ')[1]


# acessar o site
driver.get('https://sitepreco2.netlify.app/')

# encontrar o abacate
precos_site_2 = driver.find_elements(By.XPATH, "//h5")
preco_final_site_2 = precos_site_2[3].text.split('$')[1]

# acessar o site
driver.get('https://sitepreco3.netlify.app/')

# encontrar o abacate
precos_site_3 = driver.find_elements(
    By.XPATH, '//div[@class="featured__item__text"]//h5')
preco_final_site_3 = precos_site_3[2].text.split('$')[1]

# anotar o valor
with open('precos.csv', 'w', newline='', encoding='utf-8') as arquivo:
    arquivo.write(f'site,preço{os.linesep}')
    arquivo.write(
        f'https://sitepreco1.netlify.app/,{preco_final_site_1}{os.linesep}')
    arquivo.write(
        f'https://sitepreco2.netlify.app/,{preco_final_site_2}{os.linesep}')
    arquivo.write(
        f'https://sitepreco3.netlify.app/,{preco_final_site_3}{os.linesep}')
