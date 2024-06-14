import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


osname = input("Put in PC user name (Admin) to access cookies: ")
osname = str(osname)


chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
userdatadir = f"C:/Users/{osname}/AppData/Local/Google/Chrome/User Data/Default"
chrome_options.add_argument(f"--user-data-dir={userdatadir}")
profile = "Default"
chrome_options.add_argument(f"--profile-directory={profile}")


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get('______________')
time.sleep(7)

i = 0
max_clicks = 90000
while i < max_clicks:
    try:
        
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//button[@class="mdl-button mdl-js-button mdl-button--disabled"]'))
        )
        
        for button in buttons:
            try:
                actionschains = ActionChains(driver)
                actionschains.double_click(button).perform()
                i += 1
                if i >= max_clicks:
                    break
                time.sleep(2)
            except Exception as e:
                print(f"An error occurred during clicking button: {e}")
                continue

        
        time.sleep(120)

    except Exception as e:
        print(f"An error occurred while finding buttons: {e}")

driver.quit()
