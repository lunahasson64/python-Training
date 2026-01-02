from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from kerem_qa.zara_project.globals import PRODUCT
from kerem_qa.zara_project.zara_pages.locetors import welcome_page_locetors


class WelcomePage():

    def __init__(self, driver):
        self.driver = driver

    def search_of_item(self, item):
        first_search_button = self.driver.find_element(*welcome_page_locetors.FIRST_SEARCH_BUTTON)
        first_search_button.click()
        second_search_button = self.driver.find_element(*welcome_page_locetors.SECOND_SEARCH_BUTTON)
        second_search_button.click()
        second_search_button.send_keys(item)
        second_search_button.send_keys(Keys.ENTER)



    def find_woman_man_kids_buttons(self):
        three_lines_in_main_page = self.driver.find_element(*welcome_page_locetors.THREE_LINES_IN_MAIN_PAGE)
        three_lines_in_main_page.click()

        woman_button = self.driver.find_element(By.LINK_TEXT, "WOMAN")
        print(woman_button.text)

        man_button = self.driver.find_element(By.LINK_TEXT, "MAN")
        print(man_button.text)

        kids_button = self.driver.find_element(By.LINK_TEXT, "KIDS")
        print(kids_button.text)

        return woman_button, man_button, kids_button



    def login_page(self):
        login_button = self.driver.find_element(*welcome_page_locetors.LOGIN_BUTTON)
        login_button.click()



    def offices_button(self):
        first_search_button = self.driver.find_element(*welcome_page_locetors.FIRST_SEARCH_BUTTON)
        first_search_button.click()
        offices_button = self.driver.find_element(*welcome_page_locetors.OFFICES_BUTTON)
        offices_button.click()




    def search_product(self, product):
        first_search_button = self.driver.find_element(*welcome_page_locetors.FIRST_SEARCH_BUTTON)
        first_search_button.click()
        second_search_button = self.driver.find_element(*welcome_page_locetors.SECOND_SEARCH_BUTTON)
        second_search_button.click()
        second_search_button.send_keys(PRODUCT)
        second_search_button.send_keys(Keys.ENTER)


    def close_pop_up_message(self):
        first_message = self.driver.find_element(*welcome_page_locetors.FIRST_MESSAGE)
        first_message.click()
