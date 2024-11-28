from selenium import webdriver
from selenium.webdriver.chrome.service import Service # set up chrome driver service 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

# var
cookie_url = 'https://orteil.dashnet.org/cookieclicker/'
cookie_id = 'bigCookie'
cookies_count_id = 'cookies' # num of cookies
products_id = 'products'
product_price_prefix = 'productPrice'
product_prefix = 'product'

# get URL
driver.get(cookie_url)
driver.implicitly_wait(5)

# choose language
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
languague = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
languague.click()

# pre-defined elements
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, products_id))
)
products_price_element = [driver.find_element(By.ID, product_price_prefix + str(i)) for i in range(2, -1, -1)]
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie_element = driver.find_element(By.ID, cookie_id)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookies_count_id))
)
cookies_count_element = driver.find_element(By.ID, cookies_count_id)

for i in range(50):
    # click cookie action
    click_cookie_action = ActionChains(driver)
    click_cookie_action.click(cookie_element)
    click_cookie_action.perform()

    cookies_count = int(cookies_count_element.text.split(" ")[0].replace(",",""))
    print('cookies_count:', cookies_count)

    for product in products_price_element:
        print('product:', product.text)

        product_price_text = product.text.replace(",", "")
        if not product_price_text.isdigit():
            continue
        product_price = int(product_price_text) 
        print('product_price:', product_price)

        if (cookies_count >= product_price):
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(product)
            upgrade_action.click()
            upgrade_action.perform()
            break

# time.sleep(10)
driver.quit()