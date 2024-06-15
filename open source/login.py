import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

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

def monitor_browser(driver):
    while True:
        try:
            driver.current_window_handle
            time.sleep(1)
        except WebDriverException:
            os._exit(0)  

monitor_thread = threading.Thread(target=monitor_browser, args=(driver,))
monitor_thread.daemon = True  
monitor_thread.start()

driver.get('______________________')

time.sleep(700)

driver.quit()