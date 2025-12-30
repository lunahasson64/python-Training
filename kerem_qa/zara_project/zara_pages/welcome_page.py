
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from kerem_qa.zara_project.globals import PRODUCT
from kerem_qa.zara_project.zara_pages.locetors import welcome_page_locetors


class welcome_page():

    def __init__(self, driver):
        self.driver = driver

    def search_of_item(self, item):
        first_search_button = self.driver.find_element(*welcome_page_locetors.FIRST_SEARCH_BUTTON)
        first_search_button.click()
        secound_search_button = self.driver.find_element(*welcome_page_locetors.SECOUND_SEARCH_BUTTON)
        secound_search_button.click()
        secound_search_button.send_keys(item)
        secound_search_button.send_keys(Keys.ENTER)



    def find_fild_woman_man_kids(self):
        three_lines_in_main_page = self.driver.find_element(*welcome_page_locetors.THREE_LINES_IN_MAIN_PAGE)
        three_lines_in_main_page.click()

        woman_button = self.driver.find_element(By.LINK_TEXT, "WOMAN")
        print(woman_button.text)
        assert woman_button.text == "WOMAN","woman button is not  correctly"

        man_button = self.driver.find_element(By.LINK_TEXT, "MAN")
        print(man_button.text)
        assert man_button.text == "MAN","man button is not  correctly"

        kids_button = self.driver.find_element(By.LINK_TEXT, "KIDS")
        print(kids_button.text)
        assert kids_button.text == "KIDS","kids button is not  correctly"



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
        secound_search_button = self.driver.find_element(*welcome_page_locetors.SECOUND_SEARCH_BUTTON)
        secound_search_button.click()
        secound_search_button.send_keys(PRODUCT)
        secound_search_button.send_keys(Keys.ENTER)


    def pop_up_message(self):
        first_message = self.driver.find_element(*welcome_page_locetors.FIRST_MESSAGE)
        first_message.click()






















    # first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
    # main_search_button = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content").click()
    # second_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
    # second_search_button.send_keys("shoes")
    # second_search_button.send_keys(Keys.ENTER)
    # prices = self.driver.find_elements(By.CLASS_NAME, "money-amount__main")
    # first_price = prices[0].text
    # print(first_price)