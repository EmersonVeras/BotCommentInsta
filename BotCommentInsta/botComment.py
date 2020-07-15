import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\user\Desktop\Trabalhos em Python\geckodriver"
        )
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
    
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.get("https://www.instagram.com/p/CCBbs40BQIi/") 

        for i in range(1,2):

                        driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")

        try:
                comments = [
                    
                        "Comentário" #Adicione vários comentários


                ]
                
                

                for i in range(0,967): #modificar dependendo do número de comentários
                    x = comments[i]
                    print(i)

                    driver.find_element_by_class_name("Ypffh").click()
                    comment_input_box = driver.find_element_by_class_name("Ypffh").send_keys(x)
                    
                    
                    time.sleep(random.randint(2, 3))
            
                    
                
                    driver.find_element_by_xpath(
                         "//button[contains(text(), 'Publicar')]"
                    ).click()
                    time.sleep(random.randint(65,68))   #Modifique o time baseado no seu desejo

        except Exception as e:
                print(e)
                time.sleep(5)


# Entre com o usuário e senha aqui
Bot = InstagramBot("Id do instagram", "Senha")
Bot.login()