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
driver.get('https://www.techwithtim.net/')

content_class = 'content__CardContentContainer-sc-1nrnigk-0'
tutorials_taglist = 'tag__TagContainer-sc-3f52y0-0'
tutorials_list = 'tutorials__TutorialsList-sc-179hc97-2'
get_started_btn = 'tutorial__ButtonContainer-sc-1rebzxr-6 cXbQGi'


driver.get('https://www.techwithtim.net/')
# link = driver.find_element(By.LINK_TEXT, 'Tutorials')
# link.click()

try:
    # Turorials
    WebDriverWait(driver, 5).until( 
       EC.presence_of_element_located((By.CLASS_NAME, 'content__CardContentContainer-sc-1nrnigk-0'))
    )
    link_1 = driver.find_element(By.CLASS_NAME, 'content__CardContentContainer-sc-1nrnigk-0')
    link_1.click()
    
    list_course = driver.find_element(By.CLASS_NAME, 'tutorials__TutorialsList-sc-179hc97-2')
    # print(list_course.text)

    # Get started
    b_1 = list_course.find_element(By.CLASS_NAME, 'tutorial__TutorialCardContainer-sc-1rebzxr-0')
    # print("Found div:", b_1.text)

    b_2 = b_1.find_element(By.CLASS_NAME, 'flex__FlexContainer-sc-8vtkwv-0')
    print("Found div b_2:", b_2.text)

    b_3 = b_2.find_element(By.CLASS_NAME, 'tutorial__ButtonContainer-sc-1rebzxr-6')
    b_3_a_tag = b_3.find_element(By.TAG_NAME, "a")
    href_value = b_3_a_tag.get_attribute("href")
    print("Href value:", href_value)
    driver.get(href_value)
except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()

time.sleep(10)
driver.quit()