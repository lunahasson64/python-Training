from selenium.webdriver.common.by import By


class product():

    def __init__(self, driver):
        self.driver = driver


    def return_main_page(self):
        self.driver.find_element(By.CLASS_NAME, "layout-header-logo__icon")

