import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class welcom_page():

    def __init__(self, driver):
        self.driver = driver

    def click_on_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        first_search_button = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content").click()
        secound_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
        secound_search_button.click()
        secound_search_button.send_keys("shirt")
        secound_search_button.send_keys(Keys.ENTER)

        prices = self.driver.find_elements(By.CSS_SELECTOR,"ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")
        for i in range(5):
            price_text = prices[i].text
            lines = price_text.split("\n")
            last_price = lines[-1].strip()
            print(last_price)




    def find_fild_woman_man_kids(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        self.driver.find_element(By.CLASS_NAME, "layout-header-icon__icon").click()

        woman_button = self.driver.find_element(By.LINK_TEXT, "WOMAN")
        print(woman_button.text)

        man_button = self.driver.find_element(By.LINK_TEXT, "MAN")
        print(man_button.text)

        kids_button = self.driver.find_element(By.LINK_TEXT, "KIDS")
        print(kids_button.text)

        woman_button.click()
        NEW_COLLECTION_button = self.driver.find_element(By.LINK_TEXT, "NEW COLLECTION")
        NEW_COLLECTION_button.click()
        shoes_button = self.driver.find_element(By.LINK_TEXT, "SHOES")
        shoes_button.click()
        url = self.driver.current_url
        assert url == "https://www.zara.com/us/en/s-woman-shoes-"in url,"shoes url did not work"


    def help_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        help_button = self.driver.find_element(By.LINK_TEXT, "Help")
        help_button.click()


    def shopping_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
        Shopping_bag_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "SHOPPING BAG")
        Shopping_bag_button.click()
        url = self.driver.current_url
        assert url == "https://www.zara.com/us/en/shop/cart", ("URL did not change after login")
        Shopping_bag_button_text = Shopping_bag_button.text
        is_pass = '[0]' in Shopping_bag_button_text
        assert is_pass, "Shopping bag is not empty"













    # first_message = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']").click()
    # main_search_button = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content").click()
    # second_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
    # second_search_button.send_keys("shoes")
    # second_search_button.send_keys(Keys.ENTER)
    # prices = self.driver.find_elements(By.CLASS_NAME, "money-amount__main")
    # first_price = prices[0].text
    # print(first_price)