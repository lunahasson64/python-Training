import time
from kerem_qa.zara_project.zara_pages.locetors import product_page_locetors


class product():

    def __init__(self, driver):
        self.driver = driver


    def return_to_main_page(self):
        zara_button = self.driver.find_element(*product_page_locetors.ZARA_BUTTON)
        zara_button.click()


    def avg_prices(self):
        prices = self.driver.find_elements(*product_page_locetors.PRICES)
        total = 0
        for price in range(min(5, len(prices))):
            price_text = prices[price].text
            lines = price_text.split("\n")
            last_prices = lines[-1].strip()
            print(last_prices)
            if "$" in last_prices:
                clean_price = last_prices.replace("$", "").strip()
                clean_price = float(clean_price)
                total += clean_price
            else:
                print("Skipping non-price line:", last_prices)
        print(f"total: {total}$")
        return total


    def find_israel_in_offices_page(self):
        israel_button = self.driver.find_element(*product_page_locetors.ISRAEL_BUTTON)
        assert israel_button.is_displayed(), "Israel office is not displayed"
        print(israel_button.text)



    def woman_man_and_compare_prices(self):
        buttons = self.driver.find_elements(*product_page_locetors.BUTTONS)
        # woman_button = buttons[0]
        # woman_button.click()
        for button in buttons:
            if button.text.strip() == "Woman":
                button.click()
                break
        price_item_woman = self.driver.find_elements(*product_page_locetors.PRICE_ITEM_WOMAN)
        price_text_woman = price_item_woman[0].text
        lines_woman = price_text_woman.split("\n")
        last_prices_woman = lines_woman[-1].strip()
        print(f"price item for woman {last_prices_woman}")

        time.sleep(3)
        man_button = self.driver.find_elements(*product_page_locetors.MAN_BUTTON)[1]
        man_button.click()
        price_item_man = self.driver.find_elements(*product_page_locetors.PRICE_ITEM_MAN)
        price_text_man = price_item_man[0].text
        lines_man = price_text_man.split("\n")
        last_prices_man = lines_man[-1].strip()
        print(f"price item for man {last_prices_man}")

        if "$" in last_prices_woman:
            woman_price_number = float(last_prices_woman.replace("$", "").strip())

        if "$" in last_prices_man:
            man_price_number = float(last_prices_man.replace("$", "").strip())

        if woman_price_number > man_price_number:
            print("WOMAN is more expensive")
        elif woman_price_number < man_price_number:
            print("MAN is more expensive")
        else:
            print("Prices are same")















