import time
from kerem_qa.zara_project.zara_pages.locetors import product_page_locetors


class ProductPage():

    def __init__(self, driver):
        self.driver = driver


    def avg_prices(self):
        time.sleep(3)
        prices = self.driver.find_elements(*product_page_locetors.PRICES)
        total = 0
        for price in range(10, 15):
            price_text = prices[price].text
            split_price_test = price_text.split("\n")
            last_price = split_price_test[-1].strip()
            print(f"last price : {last_price}")
            if "$" in last_price:
                clean_price = last_price.replace("$", "").strip()
                clean_price = float(clean_price)
                total += clean_price
            else:
                print("This price is incorrect")
        print(f"total: {total}$")
        return total


    def find_israel_in_offices_page(self):
        israel_button = self.driver.find_element(*product_page_locetors.ISRAEL_BUTTON)
        print(f"israel office : {israel_button.text}")
        return israel_button




    def get_woman_price(self):
        buttons = self.driver.find_elements(*product_page_locetors.BUTTONS)
        for button in buttons:
            if button == "Woman":
                button.click()
                break
        time.sleep(3)
        price_item_woman = self.driver.find_elements(*product_page_locetors.PRICE_ITEM_WOMAN)
        if len(price_item_woman) > 0:
            price_text_woman = price_item_woman[0].text
        else:
            print("No woman price found")
            return None
        split_price_text_woman = price_text_woman.split("\n")
        last_prices_woman = split_price_text_woman[-1].strip()
        print(f"price item for woman {last_prices_woman}")
        if "$" in last_prices_woman:
            return float(last_prices_woman.replace("$", "").strip())


    def get_man_price(self):
        buttons = self.driver.find_elements(*product_page_locetors.MAN_BUTTON)
        for button in buttons:
            if button == "Man":
                button.click()
                break
        time.sleep(3)
        price_item_man = self.driver.find_elements(*product_page_locetors.PRICE_ITEM_MAN)
        if len(price_item_man) > 0:
            price_text_man = price_item_man[0].text
        else:
            print("No woman price found")
            return None
        lines_man = price_text_man.split("\n")
        last_prices_man = lines_man[-1].strip()
        print(f"price item for man {last_prices_man}")
        if "$" in last_prices_man:
            return float(last_prices_man.replace("$", "").strip())























