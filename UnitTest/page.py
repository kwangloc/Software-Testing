from locator import *
from element import BasePageElement

# Element
class SearchTextElement(BasePageElement):
    locator = 'q' # name

# Base page
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# Other pages
class MainPage(BasePage):
    # MainPage action methods come here.
    search_text_element = SearchTextElement()

    def does_title_match(self, title):
        # return "Python" in self.driver.title
        return title in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON) # unpack tuple
        element.click()
    
class SearchResultsPage(BasePage):
    # SearchResultsPage action methods come here.
    def is_results_found(self):
        return 'No results found.' not in self.driver.page_source
    