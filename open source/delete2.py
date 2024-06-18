import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

osname = input("Put in PC user name (Admin) to access cookies: ")
osname = str(osname)
filter_word = input("Какое слово вы хотите отфильтровать из ваших записок? ")
filter_word = str(filter_word)

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
userdatadir = f"C:/Users/{osname}/AppData/Local/Google/Chrome/User Data/Default"
chrome_options.add_argument(f"--user-data-dir={userdatadir}")
profile = "Default"
chrome_options.add_argument(f"--profile-directory={profile}")
chrome_options.add_argument("--log-level=3")


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://role-me.ru/my/roles')
    time.sleep(4) 

    elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

    for element in elements:
        element_text = element.text
        if filter_word in element_text:
            try:
               
                parent_element = element.find_element(By.XPATH, './ancestor::div[contains(@class, "mdl-card")]')
                
               
                button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
                button1.click()

                

                button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
                button2.click()
            except Exception as e:
                print(f"Error interacting with element: {e}")
    driver.get('https://role-me.ru/my/roles?filter=del')
    time.sleep(4) 
    elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

    for element in elements:
        element_text = element.text
        if filter_word in element_text:
            try:
               
                parent_element = element.find_element(By.XPATH, './ancestor::div[contains(@class, "mdl-card")]')
                
               
                button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
                button1.click()

                

                button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
                button2.click()
            except Exception as e:
                print(f"Error interacting with element: {e}")
finally:
    driver.quit()