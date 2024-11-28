import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        # Khởi tạo trình duyệt
        self.driver = webdriver.Chrome()  # Hoặc sử dụng webdriver.Firefox() tùy vào trình duyệt bạn chọn
        self.driver.implicitly_wait(10)  # Chờ tối đa 10 giây để tìm thấy phần tử

    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        
        # Tìm thanh tìm kiếm và nhập từ khóa
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("unittest với Selenium Python")
        search_box.send_keys(Keys.RETURN)

        # Đợi trang tải
        time.sleep(2)

        # Kiểm tra có kết quả tìm kiếm xuất hiện
        self.assertIn("unittest", driver.page_source)

    def tearDown(self):
        # Đóng trình duyệt sau mỗi bài kiểm thử
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
