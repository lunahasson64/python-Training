from kerem_qa.zara_project.zara_pages.locetors import product_page_locetors


class ProductPage():

    def __init__(self, driver):
        self.driver = driver


    def avg_prices(self):
        prices = self.driver.find_elements(*product_page_locetors.PRICES)
        total = 0
        for price in range(min(5, len(prices))):
            price_text = prices[price].text
            split_price_test = price_text.split("\n")
            last_price = split_price_test[-1].strip()
            print(last_price)
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
        assert israel_button.is_displayed(), "Israel office is not found"
        print(israel_button.text)




    def woman_price(self):
        buttons = self.driver.find_elements(*product_page_locetors.BUTTONS)
        for button in buttons:
            if button.text.strip() == "Woman":
                button.click()
                break
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


    def man_price(self):
        buttons = self.driver.find_elements(*product_page_locetors.MAN_BUTTON)
        for button in buttons:
            if button.text.strip() == "Man":
                button.click()
                break
        price_item_man = self.driver.find_elements(*product_page_locetors.PRICE_ITEM_MAN)
        if len(price_item_man) > 0:
            price_text_man = price_item_man[0].text
        else:
            print("No woman price found")
            return None
        # price_item_man = self.driver.find_elements(*product_page_locetors.PRICE_ITEM_MAN)
        # price_text_man = price_item_man[0].text
        lines_man = price_text_man.split("\n")
        last_prices_man = lines_man[-1].strip()
        print(f"price item for man {last_prices_man}")
        if "$" in last_prices_man:
            return float(last_prices_man.replace("$", "").strip())























