from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="robo"
)

class newbot:
      def __init__(self,newbot):
            self.driver = webdriver.Chrome("C://Users//Emerson Rodrigues//Documents//MEGA//EMERSONBKP//driver//chromedriver.exe")

      def bolsadados(self):
            try:
                  site = "https://artigos.toroinvestimentos.com.br/bolsa-de-valores-hoje-ibovespa"
                  self.driver.get(site)
                  self.driver.implicitly_wait(20)

                  e=0
                  while True:

                        #O robo vai capturar dos dados das principais bolsas e depois inserir no bd
                       petr4=self.find_element_by_xpath('//*[@id="indice-bovespa"]/table/tbody/tr[1]/td[2]/span[2]').text

                       itub4=self.find_element_by_xpath('//*[@id="indice-bovespa"]/table/tbody/tr[2]/td[2]/span[2]').text

                       vale3=self.find_element_by_xpath('//*[@id="indice-bovespa"]/table/tbody/tr[3]/td[2]/span[2]').text

                       time.sleep(10)

                       mycursor = mydb.cursor()

                       sql = "INSERT INTO dados(petr4,itub4,vale3) VALUES (%s,%s,%s)"
                       val = (petr4,itub4,vale3)
                       mycursor.execute(sql,val)

                       mydb.commit()


                       e+=1
                       if(e>1):
                         e=0

                       
            except:
                self.driver.quit()
              
