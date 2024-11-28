from selenium import webdriver
from selenium.webdriver.chrome.service import Service # set up chrome driver service 
import unittest # built-in python lib
from selenium import webdriver
import page
import time

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print('Setting up.')
        self.service = Service(executable_path='../chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get('https://www.python.org/')

    # functions with 'test_' prefix will automatically be called
    def not_be_called(self):
        print('Not be called')
        assert False 

    # def test_example_1(self):
    #     print('Running test 1')
    #     assert True 

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.does_title_match('Python')

    # def test_search_python(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.does_title_match()
    #     mainPage.search_text_element = 'pycon'
    #     mainPage.click_go_button()
    #     search_result_page = page.SearchResultsPage(self.driver)
    #     time.sleep(10)
    #     assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()