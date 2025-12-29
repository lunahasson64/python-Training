from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class product():

    def __init__(self, driver):
        self.driver = driver


    def return_to_main_page(self):
        zara_button = self.driver.find_element(By.CLASS_NAME, "hlp-header__logo-img")
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
        woman_button = buttons[0]
        woman_button.click()
        # for button in buttons:
        #     if button.text.strip() == "Woman":
        #         button.click()
        #         break
        price_item_woman = self.driver.find_elements(By.CLASS_NAME, "price-current__amount")
        price_text_woman = price_item_woman[0].text
        man_button = buttons[1]
        man_button.click()
        price_item_man = self.driver.find_elements(By.CLASS_NAME, "money-amount__main")
        price_text_man = price_item_man[0].text
        print(price_text_man)


    def add_to_shopping_bag(self,ITEMM ):
        secound_search_button = self.driver.find_element(By.ID, "search-home-form-combo-input")
        secound_search_button.click()
        secound_search_button.send_keys(ITEMM)
        secound_search_button.send_keys(Keys.ENTER)







