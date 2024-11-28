# tutorial 2

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

try:

    WebDriverWait(driver, 5).until( 
       EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
    )
    input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
    input_element.clear()
    input_element.send_keys("donald trump" + Keys.ENTER)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'baomoi'))
    )

    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'baomoi')
    link.click()

    list_content = driver.find_element(By.CLASS_NAME, 'content-list')
    cards = list_content.find_elements(By.CLASS_NAME, 'bm-card')
    for card in cards:
        # Locate the card content
        card_content = card.find_element(By.CLASS_NAME, 'bm-card-content')
        
        # Locate the card header (title)
        card_header = card_content.find_element(By.CLASS_NAME, 'bm-card-header')
        
        # Extract and print the title text
        title = card_header.text
        print(title)
   
except:
    driver.quit()

# links = driver.find.elements(By.PARTIAL_LINK_TEXT, 'donald trump')




# print(driver.page_source)

# page-tag main-container 
# articles title: css-8xl60i css-1l4w6pd css-1bdu3ax css-1i8vfl5 css-e1lvw9 a css-nsjm9t

# try

time.sleep(20)
driver.quit()