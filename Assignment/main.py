from selenium import webdriver
from selenium.webdriver.chrome.service import Service # set up chrome driver service 
import unittest # built-in python lib
from selenium import webdriver
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

    def test_signup(self):
        test_signup_results = []
        for index, row in self.data.iterrows():
            user = {col: row[col] for col in self.columns_signup if pd.notna(row[col])}
            try:
                self.driver.get(self.homepage_url)
                mainPage = page.MainPage(self.driver)
                assert mainPage.does_title_match()
                mainPage.go_signup_page()
                signup_page = page.SignupPage(self.driver)
                assert signup_page.does_title_match()
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
                assert mainPage.does_title_match()
                mainPage.go_login_page()
                login_page = page.LoginPage(self.driver)
                assert login_page.does_title_match()
                login_page.fill_n_submit(user)
                time.sleep(1)
                login_page.log_out()
                test_login_results.append('passed')
                assert True
            except Exception as err:
                print("Loi roi:", row)
                test_login_results.append('failed')
                pass
                # assert False
                
        print(test_login_results)

    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestingPHPTravels('test_signup'))
    # suite.addTest(TestingPHPTravels('test_login'))
    return suite

if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())