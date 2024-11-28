from selenium import webdriver
from selenium.webdriver.chrome.service import Service # set up chrome driver service 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

service = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigates the browser to the specified URL.
driver.get('https://phptravels.net/')

# Set fullscreen viewport
driver.maximize_window()
viewport_width = driver.execute_script("return window.innerWidth;")
viewport_height = driver.execute_script("return window.innerHeight;")
print(f"Fullscreen viewport width: {viewport_width}")
print(f"Fullscreen viewport height: {viewport_height}")

try:
    WebDriverWait(driver, 5).until( 
       EC.presence_of_element_located((By.CLASS_NAME, 'nav-item--right'))
    )
    items_right = driver.find_element(By.CLASS_NAME, 'nav-item--right')
    third_li = items_right.find_element(By.CSS_SELECTOR, 'ul.navbar-nav > li:nth-of-type(3)')

    a_tags_in_third_li = third_li.find_elements(By.CLASS_NAME, 'dropdown-item')
    a_tag_login = a_tags_in_third_li[0]
    a_tag_signup = a_tags_in_third_li[1]

    login_url = a_tag_login.get_attribute("href")
    signup_url = a_tag_signup.get_attribute("href")

    driver.get(login_url)

    # email
    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys('joeyjoeyjoey102@gmail.com')
    # password
    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('123456789a')
    # log in button
    btn_login = driver.find_element(By.ID, 'submitBTN')
    btn_login.click()
    print('Done login')
    # log out
    driver.implicitly_wait(5)

    out_items_right = driver.find_element(By.CLASS_NAME, 'nav-item--right')
    logout_link = out_items_right.find_element(By.XPATH, './/a[contains(text(), "Logout")]')
    logout_href = logout_link.get_attribute('href')
    print("Logout href:", logout_href)

except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()

time.sleep(3)
driver.close()