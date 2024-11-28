from selenium import webdriver
from selenium.webdriver.chrome.service import Service # set up chrome driver service 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # Get Login/Signup URL
    WebDriverWait(driver, 5).until( 
       EC.presence_of_element_located((By.CLASS_NAME, 'nav-item--right'))
    )
    items_right = driver.find_element(By.CLASS_NAME, 'nav-item--right')
    print(items_right.text)

    third_li = items_right.find_element(By.CSS_SELECTOR, 'ul.navbar-nav > li:nth-of-type(3)')
    print(third_li.text)

    a_tags_in_third_li = third_li.find_elements(By.CLASS_NAME, 'dropdown-item')
    a_tag_login = a_tags_in_third_li[0]
    a_tag_signup = a_tags_in_third_li[1]

    login_url = a_tag_login.get_attribute("href")
    signup_url = a_tag_signup.get_attribute("href")
    print(login_url)
    print(signup_url)

    # Direct to Signup
    driver.get(signup_url)
    time.sleep(3)
    # firstname
    input_firstname = driver.find_element(By.ID, 'firstname')
    input_firstname.send_keys('ABC')
    # time.sleep(3)
    # lastname
    input_lastname = driver.find_element(By.ID, 'last_name')
    input_lastname.send_keys('ABC')
    # time.sleep(3)
    # lastname
    div_country = driver.find_element(By.CLASS_NAME, 'filter-option')
    div_country.click()

    div_country_inner = driver.find_element(By.CLASS_NAME, 'bs-searchbox')
    input_country = div_country_inner.find_element(By.CLASS_NAME, 'form-control')
    input_country.send_keys('viet nam' + Keys.ENTER)
    # time.sleep(3)
    # phone
    input_phone = driver.find_element(By.ID, 'phone')
    input_phone.send_keys('0123456789')
    # time.sleep(3)
    # email
    input_email = driver.find_element(By.ID, 'user_email')
    input_email.send_keys('abc@gmail.com')
    # time.sleep(3)
    # password

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('123456')

    # time.sleep(3)
    # capcha
    # div_captcha = driver.find_element(By.CLASS_NAME, 'g-recaptcha')
    # div_captcha.click()
    # input('Please solve CAPTCHA manually. Then press ENTER to continue.')

    # enable btn_submit

    submitBTN = driver.find_element(By.ID, "submitBTN")
    driver.execute_script("arguments[0].removeAttribute('disabled')", submitBTN)
    driver.execute_script("arguments[0].click();", submitBTN)

    # submit
    # btn_submit = driver.find_element(By.ID, 'submitBTN')
    # is_btn_submit_disabled = btn_submit.get_attribute("disabled") is not None
    # print(is_btn_submit_disabled)
    # if not is_btn_submit_disabled:
    #     btn_submit.click()

except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()

time.sleep(3)
driver.close()