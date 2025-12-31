from kerem_qa.zara_project.zara_pages.locetors import product_page_locetors


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def return_to_main_page(self):
        zara_button = self.driver.find_element(*product_page_locetors.ZARA_BUTTON)
        zara_button.click()
