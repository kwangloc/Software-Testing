from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    DONATE_BUTTON = (By.CLASS_NAME, 'donate-button')
    DOCS_OPT = (By.CLASS_NAME, 'docs-meta')

class SearchResultsPageLocators(object):
    pass