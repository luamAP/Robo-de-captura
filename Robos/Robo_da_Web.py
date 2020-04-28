#Importando bibliotecas
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Robô_em_ação:
    def __init__(self):
        #super(object, self).__init__(*args))
        self.navegador = webdriver.Firefox(executable_path='C:\\Users\\llape\\Desktop\\VERTENTE TESTE\\Instaladores\\Drivers\\geckodriver.exe')

    def pop_up(self):
        '''
        Metodo que facha uma caixa de dialogo

        return: None
        '''

        #self.navegador.switch_to_alert()
        print(self.navegador.title)
        
        pop_up = self.navegador.find_element_by_xpath('//*[@id="onesignal-popover-dialog"]')
        print(type(pop_up))
        self.navegador.switch_to_frame(pop_up)
        #botao_NAO = self.navegador.find_elements_by_xpath('//*[@id="onesignal-popover-cancel-button"]')
           
        caixa.dismiss()

        return None

    def ação_login(self):
        '''
        Loga no site.

        '''
        
        self.navegador.get('https://www.estrategiaconcursos.com.br/')
        time.sleep(10)

        #pop_up()
        #self.navegador.find_elements_by_xpath('//*[@id="onesignal-popover-cancel-button"]').click() 

        self.navegador.find_element_by_xpath('/html/body/header/div/div/div/div[1]/a').click()
        self.navegador.find_element_by_xpath('/html/body/header/div/div/div/div[1]/div/form/div/div[5]/div[2]/a').click()

        email = self.navegador.find_element_by_xpath('//*[@id="identifierId"]')
        email.send_keys('luamlap27.9')
        email.submit()

        senha = self.navegador.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        senha.send_keys('jaspekde27')
        senha.submit()

    def localizar_curso(self):
        '''
        Localiza o curso
        '''
        self.navegador.find_element_by_xpath('/html/body/nav[2]/div/ul/li[1]/a')


if __name__ == '__main__':
    acoes = Robô_em_ação()
    acoes.ação_login()

    if input() == '0':
        acoes.navegador.close()