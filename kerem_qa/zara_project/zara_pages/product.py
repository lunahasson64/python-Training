import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from kerem_qa.zara_project.globals import ITEM_SHOPPING_BAG


class product():

    def __init__(self, driver):
        self.driver = driver


    def return_to_main_page(self):
        zara_button = self.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.zara.com/us/']")
        zara_button.click()


    def avg_prices(self):
        prices = self.driver.find_elements(By.CSS_SELECTOR,"ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")
        total = 0
        for i in range(5):
            price_text = prices[i].text
            lines = price_text.split("\n")
            last_prices = lines[-1].strip()
            print(last_prices)
            clean_price = last_prices.replace("$", "").strip()
            float_price = float(clean_price)
            total += float_price
        print(f"$ {total}")


    def find_israel_in_offices_page(self):
        israel_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Israel")
        assert israel_button.is_displayed(), "Israel office is not displayed"
        print(israel_button.text)



    def woman_man_and_compare_prices(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, "search-sections-bar__section")
        # woman_button = buttons[0]
        # woman_button.click()
        for button in buttons:
            if button.text.strip() == "Woman":
                button.click()
                break
        price_item_woman = self.driver.find_elements(By.CSS_SELECTOR, "ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")
        price_text_woman = price_item_woman[0].text
        lines_woman = price_text_woman.split("\n")
        last_prices_woman = lines_woman[-1].strip()
        print(last_prices_woman)

        man_button = self.driver.find_elements(By.CSS_SELECTOR, "button[data-qa-action='search-section-change']")[1].click()
        price_item_man = self.driver.find_elements(By.CSS_SELECTOR, "ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")
        price_text_man = price_item_man[0].text
        lines_man = price_text_man.split("\n")
        last_prices_man = lines_man[-1].strip()
        print(last_prices_man)

        woman_price_number = float(last_prices_woman.replace("$", "").strip())
        man_price_number = float(last_prices_man.replace("$", "").strip())

        if woman_price_number > man_price_number:
            print("WOMAN is more expensive")
        elif woman_price_number < man_price_number:
            print("MAN is more expensive")
        else:
            print("Prices are same")




    def add_to_shopping_bag(self, ITEM_SHOPPING_BAG):
        time.sleep(3)
        first_search_button = self.driver.find_element(By.CSS_SELECTOR, "a[data-qa-id='header-search-text-link']")
        first_search_button.click()
        secound_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
        secound_search_button.click()
        secound_search_button.send_keys(ITEM_SHOPPING_BAG)
        secound_search_button.send_keys(Keys.ENTER)
        first_shoes = self.driver.find_element(By.CSS_SELECTOR, "li[class='product-grid-product _product product-grid-product--is-not-template product-grid-product--ZOOM2-columns product-grid-product--0th-column']")
        first_shoes.click()
        add_shoes = self.driver.find_element(By.CSS_SELECTOR, "button[class='zds-button product-detail-cart-buttons__button zds-button--secondary zds-button--large']")
        add_shoes_drop_down = Select(add_shoes)
        add_shoes_drop_down.select_by_index(1)










