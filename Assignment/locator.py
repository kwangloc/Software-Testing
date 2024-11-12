from selenium.webdriver.common.by import By

class MainPageLocators(object):
    RIGHT_ITEMS = (By.CLASS_NAME, 'nav-item--right')
    ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, 'ul.navbar-nav > li:nth-of-type(3)')
    A_TAGS_IN_3RD_LI = (By.CLASS_NAME, 'dropdown-item')

    ACCOUNT_LOGOUT_DROPDOWN = (By.CSS_SELECTOR, 'ul.navbar-nav > li:nth-child(3)')
    LOGOUT_LI = (By.CSS_SELECTOR, 'ul > li:nth-child(5)')

class SignupPageLocators(object):
    FIRSTNAME_INPUT = (By.ID, 'firstname')
    LASTNAME_INPUT = (By.ID, 'last_name')
    COUNTRY_DIV = (By.CLASS_NAME, 'filter-option')
    COUNTRY_INNER_DIV = (By.CLASS_NAME, 'bs-searchbox')
    COUNTRY_INPUT = (By.CLASS_NAME, 'form-control')
    PHONE_INPUT = (By.ID, 'phone')
    EMAIL_INPUT = (By.ID, 'user_email')
    PASSWORD_INPUT = (By.ID, 'password')
    CAPTCHA_DIV = (By.CLASS_NAME, 'g-recaptcha')
    SUBMIT_BTN = (By.ID, 'submitBTN')
    
class LoginPageLocators(object):
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'submitBTN')

