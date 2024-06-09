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

# Get the OS name for the user
osname = input("Put in PC user name (Admin) to access cookies: ")
osname = str(osname)

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=500,500")
userdatadir = f"C:/Users/{osname}/AppData/Local/Google/Chrome/User Data/Default"
chrome_options.add_argument(f"--user-data-dir={userdatadir}")
profile = "Default"
chrome_options.add_argument(f"--profile-directory={profile}")

# Setup Chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the target URL
driver.get('https://role-me.ru/my/ideas')
time.sleep(7)

i = 0
max_clicks = 500
while i < max_clicks:
    try:
        # Find all buttons with the specified class
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
                time.sleep(1)
            except Exception as e:
                print(f"An error occurred during clicking button: {e}")
                continue
    except Exception as e:
        print(f"An error occurred while finding buttons: {e}")

driver.quit()