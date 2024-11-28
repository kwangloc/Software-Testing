from locator import *
from element import BasePageElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Element
class InputEmailElement(BasePageElement):
    locator_id = 'email'

class InputPasswordElement(BasePageElement):
    locator_id = 'password'

# Base page
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# Other pages
class MainPage(BasePage):
    # MainPage action methods come here.
    # search_text_element = SearchTextElement()

    def does_title_match(self):
        return 'PHPTRAVELS' in self.driver.title
   
    def go_signup_page(self):
        items_right = self.driver.find_element(*MainPageLocators.RIGHT_ITEMS)
        third_li = items_right.find_element(*MainPageLocators.ACCOUNT_DROPDOWN)

        a_tags_in_third_li = third_li.find_elements(*MainPageLocators.A_TAGS_IN_3RD_LI)
        a_tag_signup = a_tags_in_third_li[1]

        signup_url = a_tag_signup.get_attribute("href")
        self.driver.get(signup_url)

    def go_login_page(self):
        items_right = self.driver.find_element(*MainPageLocators.RIGHT_ITEMS)
        third_li = items_right.find_element(*MainPageLocators.ACCOUNT_DROPDOWN)

        a_tags_in_third_li = third_li.find_elements(*MainPageLocators.A_TAGS_IN_3RD_LI)
        a_tag_login = a_tags_in_third_li[0]

        login_href = a_tag_login.get_attribute("href")
        self.driver.get(login_href)

class LoginPage(BasePage):
    # SearchResultsPage action methods come here.
    input_email_element = InputEmailElement()
    input_password_element = InputPasswordElement()

    def does_title_match(self):
        return 'Login' in self.driver.title

    def fill_n_submit(self, user):
        print('user:', user)
        # email
        input_email = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        input_email.send_keys(user['Email'])
        # password
        input_password = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        input_password.send_keys(user['Password'])
        # log in button
        btn_login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        btn_login.click()

    def is_logged_in(self):
        print('self.driver.title:', self.driver.title)
        # return 'Dashboard' in self.driver.title
        #
        if 'Dashboard' in self.driver.title:
            return True
        else:
            return False


    def log_out(self):
        self.driver.implicitly_wait(3)
        out_items_right = self.driver.find_element(By.CLASS_NAME, 'nav-item--right')
        logout_link = out_items_right.find_element(By.XPATH, './/a[contains(text(), "Logout")]')
        logout_href = logout_link.get_attribute('href')
        self.driver.get(logout_href)
        # print("Logout href:", logout_href)


class SignupPage(BasePage):
    # SearchResultsPage action methods come here.

    def does_title_match(self):
        return 'Signup' in self.driver.title

    def fill_n_submit(self, user):
        print('user', user)
        # firstname
        try:
            input_firstname = self.driver.find_element(*SignupPageLocators.FIRSTNAME_INPUT)
            input_firstname.send_keys(user['Firstname'])
            # lastname
            input_lastname = self.driver.find_element(*SignupPageLocators.LASTNAME_INPUT)
            input_lastname.send_keys(user['Lastname'])
            # lastname
            div_country = self.driver.find_element(*SignupPageLocators.COUNTRY_DIV)
            div_country.click()

            div_country_inner = self.driver.find_element(*SignupPageLocators.COUNTRY_INNER_DIV)
            input_country = div_country_inner.find_element(*SignupPageLocators.COUNTRY_INPUT)
            input_country.send_keys(user['Country'] + Keys.ENTER)
            # phone
            input_phone = self.driver.find_element(*SignupPageLocators.PHONE_INPUT)

            phone_tmp = '0' + str(user['Phone'])
            # if user['phone'] != '':
            #     phone_tmp = '0' + str(user['Phone'])
            # else:
            #     phone_tmp = ''

            input_phone.send_keys(phone_tmp)
            # email
            input_email = self.driver.find_element(*SignupPageLocators.EMAIL_INPUT)
            input_email.send_keys(user['Email'])
            # password
            input_password = self.driver.find_element(*SignupPageLocators.PASSWORD_INPUT)
            input_password.send_keys(user['Password'])

            print('>>>>>>>>>>>>>>>>done filling')
            
            # btn_submit = self.driver.find_element(By.ID, *SignupPageLocators.SUBMIT_BTN)
            # self.driver.execute_script("arguments[0].removeAttribute('disabled')", btn_submit)
            # self.driver.execute_script("arguments[0].click();", btn_submit)

            submitBTN = self.driver.find_element(By.ID, "submitBTN")
            self.driver.execute_script("arguments[0].removeAttribute('disabled')", submitBTN)
            self.driver.execute_script("arguments[0].click();", submitBTN)

            return True

            # capcha
            # div_captcha = self.driver.find_element(*SignupPageLocators.CAPTCHA_DIV)
            # div_captcha.click()
            # input('Please solve CAPTCHA manually. Then press ENTER to continue.')
            # time.sleep(2)
            # # submit
            # btn_submit = self.driver.find_element(*SignupPageLocators.SUBMIT_BTN)
            # is_btn_submit_disabled = btn_submit.get_attribute("disabled") is not None
            # if is_btn_submit_disabled:
            #     print("Submit button is disabled. Check for form validation errors.")
            #     self.driver.save_screenshot("submit_button_disabled.png")
            #     return False 
            # else:
            #     btn_submit.click()
            #     return True 

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            self.driver.save_screenshot("element_not_found.png")
            return False
        except Exception as e:
            # print(f"An error occurred at fill_n_submit(): {e}")
            self.driver.save_screenshot("submission_error.png")
            return False
    def is_signup_success(self):
        return 'Signup Success' in self.driver.title
    

class TestPage(BasePage):

    def does_title_match(self):
        return 'ww' in self.driver.title
