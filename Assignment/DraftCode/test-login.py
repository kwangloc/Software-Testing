from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import unittest
import time

login_test_data = [
    {"email": "", "password": "demouser"},
    {"email": "user@phptravels.com", "password": ""},
    {"email": "user@", "password": "demouser"},
    {"email": "user", "password": "demouser"},
    {"email": "user@phptravels.com", "password": "demouser"},
]   
test_results = []

class TestPHPTravelsLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(binary_path))
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.url = "https://phptravels.net/login"

    def tearDown(self):
        self.driver.quit()

    def test_login_case_1(self):
        with self.subTest("Test Case 1 : Test with empty email"):
            data = login_test_data[0]
            self.driver.get(self.url)
            time.sleep(2)
            self.driver.find_element(By.ID, "email").send_keys(data["email"])
            self.driver.find_element(By.ID, "password").send_keys(data["password"])
            time.sleep(2)
            btnLogin = self.driver.find_element(By.ID, "submitBTN")
            btnLogin.click()
            time.sleep(3)
            test_result = "Not Run"
            if "Dashboard" in self.driver.title:
                test_result = "Passed"
            else:
                test_result = "Failed"

            test_results.append(("Test Case 1:", test_result))

    def test_login_case_2(self):
        with self.subTest("Test Case 2 : Test with empty password"):
            data = login_test_data[1]
            self.driver.get(self.url)
            time.sleep(2)
            self.driver.find_element(By.ID, "email").send_keys(data["email"])
            self.driver.find_element(By.ID, "password").send_keys(data["password"])
            time.sleep(2)
            btnLogin = self.driver.find_element(By.ID, "submitBTN")
            btnLogin.click()
            time.sleep(3)
            test_result = "Not Run"
            if "Dashboard" in self.driver.title:
                test_result = "Passed"
            else:
                test_result = "Failed"

            test_results.append(("Test Case 2:", test_result))
    
    def test_login_case_3(self):
        with self.subTest("Test Case 3 : Test with Incorrectly formatted emails"):
            data = login_test_data[2]
            self.driver.get(self.url)
            time.sleep(2)
            self.driver.find_element(By.ID, "email").send_keys(data["email"])
            self.driver.find_element(By.ID, "password").send_keys(data["password"])
            time.sleep(2)
            btnLogin = self.driver.find_element(By.ID, "submitBTN")
            btnLogin.click()
            time.sleep(3)
            test_result = "Not Run"
            if "Dashboard" in self.driver.title:
                test_result = "Passed"
            else:
                test_result = "Failed"

            test_results.append(("Test Case 3:", test_result))
    
    def test_login_case_4(self):
        with self.subTest("Test Case 4 : Test with Incorrectly formatted emails 2"):
            data = login_test_data[3]
            self.driver.get(self.url)
            time.sleep(2)
            self.driver.find_element(By.ID, "email").send_keys(data["email"])
            self.driver.find_element(By.ID, "password").send_keys(data["password"])
            time.sleep(2)
            btnLogin = self.driver.find_element(By.ID, "submitBTN")
            btnLogin.click()
            time.sleep(3)
            test_result = "Not Run"
            if "Dashboard" in self.driver.title:
                test_result = "Passed"
            else:
                test_result = "Failed"

            test_results.append(("Test Case 4:", test_result))

    def test_login_case_5(self):
        with self.subTest("Test Case 5 : Test with correct acccount"):
            data = login_test_data[4]
            self.driver.get(self.url)
            time.sleep(2)
            self.driver.find_element(By.ID, "email").send_keys(data["email"])
            self.driver.find_element(By.ID, "password").send_keys(data["password"])
            time.sleep(2)
            btnLogin = self.driver.find_element(By.ID, "submitBTN")
            btnLogin.click()
            time.sleep(3)
            test_result = "Not Run"
            if "Dashboard" in self.driver.title:
                test_result = "Passed"
            else:
                test_result = "Failed"

            test_results.append(("Test Case 5:", test_result))


def print_test_results():
    print("\nTest Results:")
    for test_case_name, result in test_results:
        print("========================================")
        print(f"{test_case_name}")
        print(f"Result: {result}\n")

def execute_tests():
    unittest.main(exit=False)


if __name__ == "__main__":
    execute_tests()
    print_test_results()