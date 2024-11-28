from selenium import webdriver
from selenium.webdriver.chrome.service import Service # set up chrome driver service 
import unittest # built-in python lib
import page
import time
import pandas as pd

class TestingPHPTravels(unittest.TestCase):
    homepage_url = 'https://phptravels.net/'
    test_signup_input_file = 'test_case.xlsx'  
    test_signup_output_file = 'test_signup_result.xlsx'
    sheet_login = 'login'
    sheet_signup = 'signup'
    sheet_test = 'test_signup'
    columns_signup = ['email', 'password', 'firstname', 'lastname', 'country', 'phone']
    columns_login = ['email', 'password']

    def setUp(self):
        print('Setting up.')
        self.service = Service(executable_path='../chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        # self.driver.get(self.homepage_url)
        self.data = pd.read_excel(self.test_signup_input_file, sheet_name=self.sheet_test)

    def test_example(self):
        try:
            self.driver.get(self.homepage_url)
            testPage = page.TestPage(self.driver)
            self.assertTrue(testPage.does_title_match(), "Test page title does not match.")
        except Exception as err:
            print("Loi roi:", err)
            self.fail("Test failed due to an exception.")

    def test_signup(self):
        test_signup_results = []
        for index, row in self.data.iterrows():
            user = {col: row[col] for col in self.columns_signup if pd.notna(row[col])}
            try:
                # Go to main page and check the title
                self.driver.get(self.homepage_url)
                mainPage = page.MainPage(self.driver)
                assert mainPage.does_title_match()

                # Navigate to signup page and check the title
                mainPage.go_signup_page()
                signup_page = page.SignupPage(self.driver)
                assert signup_page.does_title_match()

                # Fill and submit signup form
                signup_page.fill_n_submit(user)
                time.sleep(1)
                test_signup_results.append('passed')
                assert signup_page.is_signup_success()
            except Exception as err:
                print("Loi roi:", err)
                test_signup_results.append('failed')
                pass
                # assert False
        print(test_signup_results)

    def test_login(self):
        test_login_results = []
        # for i in range(5):
        for index, row in self.data.iterrows():
            user = {col: row[col] for col in self.columns_login if pd.notna(row[col])}
            try:
                self.driver.get(self.homepage_url)
                mainPage = page.MainPage(self.driver)
                self.assertTrue(mainPage.does_title_match(), "Main page title does not match.")
                mainPage.go_login_page()
                login_page = page.LoginPage(self.driver)
                self.assertTrue(login_page.does_title_match(), "Login page title does not match.")
                login_page.fill_n_submit(user)
                time.sleep(1)
                self.assertTrue(login_page.is_logged_in(), "Login failed for user.")

                login_page.log_out()
                test_login_results.append('passed')
            except AssertionError as ae:
                print(f"Assertion failed for row {index}: {ae}")
                test_login_results.append('failed')
            except Exception as err:
                print(f"Error encountered for row {index}: {err}")
                test_login_results.append('failed')
                # pass
                # assert False
                
        print(test_login_results)

    def tearDown(self):
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestingPHPTravels('test_example'))
    # suite.addTest(TestingPHPTravels('test_signup'))
    # suite.addTest(TestingPHPTravels('test_login'))
    return suite

if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())