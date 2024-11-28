from selenium import webdriver
from selenium.webdriver.chrome.service import Service # set up chrome driver service 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigates the browser to the specified URL.
driver.get('https://google.com')

# Waiting for Page Elements
WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
)

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.clear()
input_element.send_keys("donald trump" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'baomoi'))
)

# links = driver.find.elements(By.PARTIAL_LINK_TEXT, 'donald trump')
link = driver.find_element(By.PARTIAL_LINK_TEXT, 'baomoi')
link.click()

time.sleep(10)
driver.quit()