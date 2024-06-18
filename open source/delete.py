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

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--log-level=3")
userdatadir = f"C:/Users/{osname}/AppData/Local/Google/Chrome/User Data/Default"
chrome_options.add_argument(f"--user-data-dir={userdatadir}")
profile = "Default"
chrome_options.add_argument(f"--profile-directory={profile}")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def matches_additional_requirements(text):
    has_cyrillic = bool(re.search(r'[А-Яа-я]', text))
    has_latin = bool(re.search(r'[A-Za-z]', text))
    no_spaces = ' ' not in text
    has_numbers = bool(re.search(r'[0-9]', text))

    return len(text) > 4 and has_cyrillic and has_latin and no_spaces and has_numbers

def chysla(text):
    has_numbers1 = bool(re.search(r'[0-9]', text))
    no_spaces = ' ' not in text
    return len(text) > 6 and has_numbers1 and no_spaces

def eng_rus(text):
    has_cyrillic = bool(re.search(r'[А-Яа-я]', text))
    has_latin = bool(re.search(r'[A-Za-z]', text))
    no_spaces = ' ' not in text
    return len(text) > 6 and has_cyrillic and has_latin and no_spaces
 

keywords = ['https://', 'РОЛМИ', '***', '.com', '.net', 'web.', '.ru' 'ЛЕГЕНДА РОЛМИ', "ЛЕГЕНДЫ РОЛМИ", 'asd', 't.me', "***"]

driver.get('https://role-me.ru/my/roles')
time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

for element in elements:
    element_text = element.text
    if any(keyword in element_text for keyword in keywords) or matches_additional_requirements(element_text) or chysla(element_text) or eng_rus(element_text) or len(element_text) < 2:
        parent_element = element.find_element(By.XPATH, '..')
        
        button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
        button1.click()
        
        button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
        button2.click()


driver.get('https://role-me.ru/my/roles?filter=&offset=20')
time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

for element in elements:
    element_text = element.text
    if any(keyword in element_text for keyword in keywords) or matches_additional_requirements(element_text) or chysla(element_text) or eng_rus(element_text) or len(element_text) < 2:

        parent_element = element.find_element(By.XPATH, '..')
        
        button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
        button1.click()
        
        button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
        button2.click()


driver.get('https://role-me.ru/my/roles?filter=&offset=40')

time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

for element in elements:
    element_text = element.text
    if any(keyword in element_text for keyword in keywords) or matches_additional_requirements(element_text) or chysla(element_text) or eng_rus(element_text) or len(element_text) < 2:
        parent_element = element.find_element(By.XPATH, '..')
        
        button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
        button1.click()
        
        button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
        button2.click()



driver.get('https://role-me.ru/my/roles?filter=del')

time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

for element in elements:
    element_text = element.text
    if any(keyword in element_text for keyword in keywords) or matches_additional_requirements(element_text) or chysla(element_text) or eng_rus(element_text) or len(element_text) < 2:
        parent_element = element.find_element(By.XPATH, '..')
        
        button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
        button1.click()
        
        button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
        button2.click()

driver.get('https://role-me.ru/my/roles?filter=del&offset=20')
time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

for element in elements:
    element_text = element.text
    if any(keyword in element_text for keyword in keywords) or matches_additional_requirements(element_text) or chysla(element_text) or eng_rus(element_text) or len(element_text) < 2:
        parent_element = element.find_element(By.XPATH, '..')
        
        button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
        button1.click()
        
        button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
        button2.click()


driver.get('https://role-me.ru/my/roles?filter=del&offset=40')
time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'mdl-card__supporting-text.mdl-card--border.games-text.js-link')

for element in elements:
    element_text = element.text
    if any(keyword in element_text for keyword in keywords) or matches_additional_requirements(element_text) or chysla(element_text) or eng_rus(element_text) or len(element_text) < 2:
        parent_element = element.find_element(By.XPATH, '..')
        
        button1 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-button--icon mdl-js-button mdl-button--colored"]')
        button1.click()
        
        button2 = parent_element.find_element(By.XPATH, './/button[@class="pull-right mdl-button mdl-js-button mdl-button--colored" and @data-upgraded=",MaterialButton"]')
        button2.click()



driver.quit()


