import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from kerem_qa.zara_project.globals import PRODUCT


class welcom_page():

    def __init__(self, driver):
        self.driver = driver

    def search_of_item(self, item):
        first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        first_search_button = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content").click()
        secound_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
        secound_search_button.click()
        secound_search_button.send_keys(item)
        secound_search_button.send_keys(Keys.ENTER)



    def find_fild_woman_man_kids(self):
        first_message  = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        three_lines_in_main_page = self.driver.find_element(By.CLASS_NAME, "layout-header-icon__icon").click()

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
        first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        login_button = self.driver.find_element(By.CSS_SELECTOR, "li[class='layout-header-action layout-header-action--type-text layout-header-action-account']")
        login_button.click()


    def shopping_page(self):
        first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        Shopping_bag_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "SHOPPING BAG")
        Shopping_bag_button.click()
        url = self.driver.current_url
        assert url == "https://www.zara.com/us/en/shop/cart", ("URL did not change after login")
        Shopping_bag_button_text = Shopping_bag_button.text
        is_pass = '[0]' in Shopping_bag_button_text
        assert is_pass, "Shopping bag is not empty"



    def offices_button(self):
        first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        first_search_button = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content").click()
        offices_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "OFFICE")
        offices_button.click()
        url = self.driver.current_url
        assert "https://www.zara.com/us/en/z-company"in url, ("URL did not change after click on offices button")


    def search_product(self, product):
        first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        first_search_button = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content").click()
        secound_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
        secound_search_button.click()
        secound_search_button.send_keys(PRODUCT)
        secound_search_button.send_keys(Keys.ENTER)






















    # first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
    # main_search_button = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content").click()
    # second_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
    # second_search_button.send_keys("shoes")
    # second_search_button.send_keys(Keys.ENTER)
    # prices = self.driver.find_elements(By.CLASS_NAME, "money-amount__main")
    # first_price = prices[0].text
    # print(first_price)